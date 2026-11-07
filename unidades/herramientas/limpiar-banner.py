import sys, subprocess, numpy as np
from PIL import Image, ImageSequence
from scipy import ndimage as nd
import cv2
gif, out = sys.argv[1], sys.argv[2]
inicio = int(sys.argv[3]) if len(sys.argv) > 3 else 0  # ms que se recortan al principio
im = Image.open(gif)
frames, durs = [], []
for f in ImageSequence.Iterator(im):
    frames.append(np.asarray(f.convert('RGB')).copy()); durs.append(f.info.get('duration', 40) or 40)
H, W, _ = frames[0].shape
# máscara fija del texto (del último fotograma) y anillo de amarillo a su alrededor, para los fundidos
def capas(a):
    ai=a.astype(int); Y=(ai[...,0]>225)&(ai[...,1]>195)&(ai[...,2]<120)
    lab,k=nd.label(Y); big=lab==(np.argmax(nd.sum(Y,lab,range(1,k+1)))+1)
    return Y,big
_,bigF=capas(frames[-1])
MF=nd.binary_dilation(nd.binary_fill_holes(bigF)&~bigF,iterations=4)
MF=nd.binary_closing(MF,iterations=6)
RING=nd.binary_dilation(MF,iterations=10)&~nd.binary_dilation(MF,iterations=3)&bigF
def limpia(a):
    a = fundido(a)
    ai = a.astype(int)
    Y = (ai[...,0] > 225) & (ai[...,1] > 195) & (ai[...,2] < 120)
    if Y.mean() < .05: return a
    lab, k = nd.label(Y)
    big = lab == (np.argmax(nd.sum(Y, lab, range(1, k+1))) + 1)
    hueco = nd.binary_fill_holes(big) & ~big
    if not hueco.any(): return a
    m = nd.binary_dilation(hueco, iterations=3) & nd.binary_fill_holes(nd.binary_dilation(big, iterations=1))
    b = a.copy(); b[m] = np.median(a[big], axis=0).astype(np.uint8)
    return cv2.inpaint(b, (m*255).astype(np.uint8), 6, cv2.INPAINT_TELEA)
def fundido(a):
    # tapa la zona del texto con el color del anillo que la rodea (sirve durante los fundidos de entrada)
    anillo=a[RING].astype(int)
    if anillo.std(axis=0).max()>14: return a
    b=a.copy(); b[MF]=np.median(anillo,axis=0).astype(np.uint8)
    return cv2.inpaint(b,(MF*255).astype(np.uint8),6,cv2.INPAINT_TELEA)
# remuestreo a 25 fps
total = sum(durs); t_ini = np.cumsum([0] + durs[:-1])
p = subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r','25','-i','-',
    '-vf','scale=800:-2:flags=lanczos','-c:v','libx264','-preset','veryfast','-crf','27','-pix_fmt','yuv420p','-movflags','+faststart','-an',out], stdin=subprocess.PIPE)
cache = {}
for t in range(inicio, total, 40):
    i = int(np.searchsorted(t_ini, t, side='right') - 1)
    if i not in cache: cache = {i: limpia(frames[i])}
    p.stdin.write(cache[i].tobytes())
p.stdin.close(); p.wait(); print(out, 'ok')
