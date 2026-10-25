# Laboratorio Canvas · Narrativa I (UFV) — instrucciones de trabajo

Repositorio de **experimentación** para el Canvas de la asignatura Narrativa I. Piezas sueltas que se incrustan en Canvas mediante iframe.
Publicación: GitHub Pages → `https://innapufv.github.io/laboratorio-canvas/<carpeta>/`

**No confundir con `INNAPUFV/formacion-ia`** (Portal de Formación en IA, curso 44179). Nada de este repositorio se enlaza desde el portal ni al revés.

## Estructura
```
assets/          ufv.css (copia propia, independiente de formacion-ia) + contacto.jpg
  fonts/         Cooper Hewitt Heavy y Light (woff2, latin; licencia OFL en OFL-CooperHewitt.txt)
portada/         portada HTML del curso (página de inicio de Canvas)
plan-trabajo/    plan de trabajo interactivo de Narrativa Periodística I (27 sesiones)
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
`portada/index.html` → página de inicio del curso de Canvas **Narrativa Periodística I** (con la «I»). **No usa el estilo UFV**: sigue la identidad de marca de la asignatura (proyecto → `claude/Identidad visual de marca (guía unificada).md`): amarillo `#FDDA48`, negro `#0F1010`, gris carbón `#393836`; **Anton** (titulares) / **Cooper Hewitt Heavy** (rótulos y encabezados; sustituye a Garet desde el 25/10/2026) / **Open Sans** (texto). No usa `ufv.css`.
- Cooper Hewitt Heavy se carga desde `../assets/fonts/` con `@font-face` (reserva: Open Sans 800). Ya aplicada (25/10/2026).
- **Orden por necesidad del alumno, en cuatro secciones con rótulo numerado** (`h2.seccion`; las tarjetas son `h3`): 01 Empieza aquí (Plan de trabajo · Guía docente · ¿Quién es tu profesor?) · 02 Estudia (Unidades temáticas · Cuadernos) · 03 Practica (PlumIA · Ejercicios y videolecciones · Aprende jugando) · 04 Resuelve tus dudas (ACN BOT · Tutoría con el profesor) + aviso de IA. **Todas las tarjetas comparten estructura**: cuadro amarillo con icono (o la foto del profesor) → título → subtítulo → acción. PlumIA lleva la P plumilla en el cuadro y su logotipo como título; ACN BOT, la estrella de Gemini. Las tarjetas carbón de IA (PlumIA, ACN BOT) van en la columna izquierda, alineadas con la banda negra de Cuadernos (Gemini Notebook): forman un eje oscuro a la izquierda.
- Logos de terceros siempre en una sola tinta (blanco sobre carbón o negro, negro sobre claro).
- Enlaces en el bloque `ENLACES` (todos en pestaña nueva, `noopener noreferrer`); vacío = «Próximamente».
- Logos (Gemini, estrella de Gemini, Gemini Notebook): SVG en una tinta, vectorizados de los originales e incrustados en el propio HTML como `<symbol>` al principio del `<body>`; toman el color del texto (`currentColor`). Ojo: **NotebookLM ahora se llama Gemini Notebook**.
- **PlumIA** (antes «Practica con IA»): logotipo oficial copiado de `INNAPUFV/plumia` (SVG de la P plumilla + «lum» e «IA» en Anton), centrado; subtítulo «Tu copiloto de redacción». Enlace en `ENLACES.plumia`.
- Se usa como **página de inicio** de Canvas, donde la columna lateral derecha estrecha el contenido (≈600–700 px): las filas de tres y de dos tarjetas siguen en fila hasta 520 px. Altura medida: 1505–1681 px entre 540 y 1300 px de ancho → iframe 1720. Sin `scrolling="no"`, para que en el móvil (≈2560 px de alto) se pueda desplazar dentro.
- Foto del profesor: JPG cuadrado 240×240 incrustado en base64 en el HTML (busca «FOTO del profesor»), en el cuadro que en las demás tarjetas ocupa el icono amarillo. El bloque del profesor enlaza a la página de Canvas «Profesor y enfoque de la asignatura».

| Carpeta | Pieza | iframe |
|---|---|---|
| `portada/` | Portada del curso Narrativa Periodística I | 1720 |

## Plan de trabajo
`plan-trabajo/index.html` → plan de trabajo interactivo 2026–2027 (página de Canvas «Plan de trabajo interactivo»). Titular H1: «Plan de trabajo»; la asignatura va en la entradilla. Misma identidad de marca que la portada, ya con **Cooper Hewitt Heavy** desde `../assets/fonts/` (reserva Open Sans 800).
- Cada sesión es una pareja de tarjetas (`.pair`): presencial (`pres`, `pres eval` = práctica evaluable, `pres exam` = examen) y virtual (`virt`). Se abren con el ratón o el foco; clic/Enter las fija; Escape las cierra.
- La pareja de la semana en curso se marca sola con «Esta semana» (según `data-fecha`).
- En móvil (≤540 px) las tarjetas pasan a una columna, así que la página es más alta que el iframe: el iframe va **sin** `scrolling="no"` para que en móvil se pueda desplazar dentro.

| Carpeta | Pieza | iframe |
|---|---|---|
| `plan-trabajo/` | Plan de trabajo interactivo de Narrativa Periodística I | 4820 |
