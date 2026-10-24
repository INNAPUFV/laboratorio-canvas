# Laboratorio Canvas · Narrativa I (UFV) — instrucciones de trabajo

Repositorio de **experimentación** para el Canvas de la asignatura Narrativa I. Piezas sueltas que se incrustan en Canvas mediante iframe.
Publicación: GitHub Pages → `https://innapufv.github.io/laboratorio-canvas/<carpeta>/`

**No confundir con `INNAPUFV/formacion-ia`** (Portal de Formación en IA, curso 44179). Nada de este repositorio se enlaza desde el portal ni al revés.

## Estructura
```
assets/          ufv.css (copia propia, independiente de formacion-ia) + contacto.jpg
portada/         portada HTML del curso (página de inicio de Canvas)
comunicaciones/  anuncios, banners de tablero y correos
multimedia/      recursos didácticos interactivos (animaciones, reproductores…)
```

## Normas fijas
- **Estilo UFV** (guía en el proyecto «Avance en IA para el modelo formativo» → `claude/Guía de estilo web UFV.md`).
- **Siempre no indexable, TODOS los .html sin excepción**: `<meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noimageindex">` (+ googlebot, bingbot). Comprobarlo antes de cada subida.
- Si cambia `assets/ufv.css`, actualizar `?v=AAAAMMDDHHMM` en el enlace de todas las páginas que la usan (caché de GitHub Pages: 10 min).
- Altura del iframe: medir la página a 820 px de ancho y redondear hacia arriba (+30 px). Dar el iframe con `?v=N` cuando haya que forzar la recarga.
- Commits en español; la usuaria trabaja en Windows (recargar con Ctrl+F5).

## Comunicaciones
**`comunicaciones/gemini-alumnos/` está duplicada en `INNAPUFV/formacion-ia`** (mismo contenido, publicado en las dos direcciones): cualquier cambio se aplica en ambos repositorios.

Cada comunicación en su subcarpeta:
- `index.html` → anuncio de Canvas por iframe (sin logo ni pie, `ufv.css`, `ENLACES`, no indexable).
- `tablero.html` (opcional) → banner compacto para el tablero: ocupa el 100 % del alto del iframe y cabe en 280 px de 320 a 1000 px de ancho.
- `correo.html` → correo para Outlook (tablas, estilos en línea, 600 px, logo en base64). No usa `ufv.css`.

| Carpeta | Pieza | iframe |
|---|---|---|
| `comunicaciones/gemini-alumnos/` | Licencias de Gemini y Gemini Notebook para alumnos (oct. 2026) | anuncio 1760 · tablero 280 |

## Multimedia
Piezas autónomas (no usan `ufv.css`; fuentes UFV desde Google Fonts).

| Carpeta | Pieza | iframe |
|---|---|---|
| `multimedia/principios-animacion/` | Los 12 principios de la animación con una pelota de baloncesto: reproductor en canvas JS (capítulos, fotograma a fotograma, 0,25×) + MP4 descargable | 600 |

## Portada del curso
`portada/index.html` → página de inicio del curso de Canvas **Narrativa Periodística**. **No usa el estilo UFV**: sigue la identidad de los anuncios y de PlumIA (proyecto → `claude/Identidad visual (anuncios y PlumIA).md`): amarillo `#FDDA48`, negro `#0F1010`, gris carbón `#393836`; Anton / Garet (Montserrat de reserva) / Open Sans. No usa `ufv.css`.
- Enlaces en el bloque `ENLACES` (todos en pestaña nueva, `noopener noreferrer`); vacío = «Próximamente».
- Foto del profesor: `portada/profesor.jpg` (si no existe, se ve un icono genérico de perfil). El bloque del profesor enlaza a su perfil de LinkedIn.

| Carpeta | Pieza | iframe |
|---|---|---|
| `portada/` | Portada del curso Narrativa Periodística | 1360 |
