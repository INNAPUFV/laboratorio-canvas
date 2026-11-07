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
profesor/        cabecera del profesor (Javier de la Rosa) con retrato animado y enlace a LinkedIn
cuadernos/       accesos a los cuadernos de Gemini Notebook (general y bibliografía)
ejercicios/      ejercicios y videolecciones (3 videolecciones + 5 ejercicios)
unidades/        unidades temáticas con los banners animados de cada unidad (media/: MP4 + JPG)
anuncio/         anuncios de la asignatura con su identidad de marca (una subcarpeta por anuncio)
comunicaciones/  comunicaciones con estilo UFV: anuncios, banners de tablero y correos
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
- Cada sesión es una pareja de tarjetas (`.pair`): presencial (`pres`, `pres eval` = práctica evaluable, `pres exam` = examen) y virtual (`virt`). La práctica evaluable lleva un recuadro interior de 3 px en **Rojo ACN `#FF5757`** (`--red`), para no confundirse con el recuadro negro exterior de «Esta semana», que se mueve cada semana. Se abren con el ratón o el foco; clic/Enter las fija; Escape las cierra.
- La pareja de la semana en curso se marca sola con «Esta semana» (según `data-fecha`).
- **Estructura de cada tarjeta** (`div.card`): un `button.toggle` invisible que cubre la tarjeta y la abre o fija (lleva `aria-expanded` y el `aria-label`), y por encima el contenido (`.front` / `.back`, `z-index:2`). Así un enlace puede ir dentro de `.back` sin estar dentro del botón.
- **Enlaces a tareas de Canvas** en la tarjeta virtual: al final de `.back`, `<a class="tarea" href="…/courses/70362/assignments/NNN" target="_blank" rel="noopener noreferrer">Texto · Unidad N <svg…></a>`; en `.front`, la etiqueta `<span class="tag">Tarea en Canvas</span>`; y en el `aria-label` del botón, «, con enlace a la tarea en Canvas». El enlace solo se ve y se puede pulsar con la tarjeta abierta (ratón: al pasar; móvil: primer toque abre, segundo toque en el botón amarillo navega; teclado: Tab abre y Tab de nuevo llega al enlace). Usar siempre la dirección base de la tarea (`/assignments/NNN`), no `/launch` ni `/taking/…`, que son de un intento concreto.
- Tareas enlazadas: sesión 4 → Evalúa tu conocimiento · Unidad 1 (579130); sesión 8 → Evalúa tu conocimiento · Unidad 2 (579116). Pendiente: sesión 13 → Unidad 3.
- En móvil (≤540 px) las tarjetas pasan a una columna, así que la página es más alta que el iframe: el iframe va **sin** `scrolling="no"` para que en móvil se pueda desplazar dentro.

| Carpeta | Pieza | iframe |
|---|---|---|
| `plan-trabajo/` | Plan de trabajo interactivo de Narrativa Periodística I | 4900 |

## Anuncios de la asignatura
`anuncio/<sesion-NN-tema>/index.html` → anuncios de Narrativa Periodística I para Canvas, con la **identidad de marca de la asignatura** (no el estilo UFV de `comunicaciones/`). Guía: proyecto → `claude/Identidad visual (anuncios y PlumIA).md` y `claude/Identidad visual de marca (guía unificada).md`.
- **Referencia / plantilla:** `anuncio/sesion-07-mesa-redonda/`. Para un anuncio nuevo, copiar esa carpeta y cambiar contenidos, número de sesión (etiqueta, `content:"07"` del número tenue y pie), fechas, lugar y enlaces. Los anteriores no se tocan (sus iframes deben seguir igual).
- Estructura: cabecera (asignatura / curso + «Anuncio · Sesión NN») → bloque amarillo (entradilla, titular Anton, subtítulo; número tenue en Anton) → **franja de datos en negro puro** (cuándo / dónde) → «¿Qué vamos a hacer?» → actividad práctica con **banda de símbolo en negro puro** → dos tarjetas (clara y **negro puro**) → aviso → pie con lema.
- **Negro puro `#0F1010` en los anuncios** (franja de datos, banda, tarjeta oscura); el carbón `#393836` es para interfaces (portada, PlumIA). No mezclarlos como fondos contiguos.
- Fuentes: Anton y Open Sans de Google Fonts; Cooper Hewitt Heavy y Light desde `../../assets/fonts/`.
- Enlaces a tareas de Canvas en pestaña nueva (`target="_blank" rel="noopener noreferrer"`). Iframe sin `scrolling="no"` (en el móvil la página es más alta).

| Carpeta | Pieza | iframe |
|---|---|---|
| `anuncio/sesion-07-mesa-redonda/` | Sesión 7 · Mesa redonda «La IA y la protección de la persona desde una mirada basada en virtudes» (23/10/2026) | 1440 |
| `anuncio/nuevo-diseno/` | Nota informativa «Nuevo diseño, mismos contenidos» (26/10/2026). Miniatura animada de la portada: los mismos 10 accesos pasan del orden antiguo a las cuatro secciones (FLIP con Web Animations; se reproduce una vez al verse; botones Antes/Ahora; respeta `prefers-reduced-motion`) | 1520 |
| `anuncio/evalua-unidad-2/` | Recordatorio compacto: «Evalúa tu conocimiento» de la Unidad 2, plazo hasta el jueves 5/11/2026 a las 23:59, con cuenta atrás (hora de Madrid) y botón a la tarea 579116. Variante «recordatorio» de dos bloques (amarillo + negro puro): la actividad es el titular (Anton) con la unidad en etiqueta negra grande; «Aún estás a tiempo» encabeza el bloque del plazo; debajo, bloque de repaso (banda negra con logo de Gemini Notebook + botón secundario) al cuaderno de la Unidad 2 con cuestionarios y fichas | 750 |

## Profesor
`profesor/index.html` → cabecera apaisada y compacta para la página de Canvas «Profesor y enfoque de la asignatura». Identidad de marca de la asignatura.
- Un solo bloque amarillo en horizontal: a la izquierda, el retrato (foto de Javier de la Rosa, JPG 360×360 en base64) con la animación del antiguo GIF rehecha en CSS/SVG: dos arcos blancos que giran en sentidos opuestos, un aro que orbita y un «+» que gira. A la derecha, «Profesor de la asignatura», nombre en Anton en una línea, el lema «Para buscar la verdad es necesario creer en ella» con tres triángulos que se encienden en secuencia, y el botón de LinkedIn en negro puro (logo en una tinta, pestaña nueva). Respeta `prefers-reduced-motion`.
- En móvil (≤600 px) el retrato pasa arriba.
- **Sin año académico** en la cabecera (solo «Narrativa Periodística I»), para que sirva todos los cursos sin cambios.

| Carpeta | Pieza | iframe |
|---|---|---|
| `profesor/` | Cabecera del profesor con retrato animado y enlace a LinkedIn | 410 |

## Cuadernos
`cuadernos/index.html` → página compacta para la página de Canvas «Cuaderno general de la asignatura y bibliografía» (a la que enlaza la tarjeta Cuadernos de la portada). Sustituye a las dos imágenes con «NotebookLM».
- Texto mínimo y sin repetir «cuaderno» (Notebook ya lo dice): etiqueta «Estudia», titular «Gemini Notebook» + «Pregunta a la IA y repasa con las fuentes de la asignatura», y dos tarjetas carbón con filete amarillo: cuadro amarillo con el logo de Gemini Notebook, título en Anton («General» / «Bibliografía»), una línea («Todos los materiales del curso» / «Fuentes y lecturas de referencia») y «Abrir ↗»; número tenue 01/02. Sin año académico.
- Enlaces: general → `notebook.google.com/notebook/653e92f2-…`; bibliografía → `notebook.google.com/notebook/412e9b0f-…/preview`.

| Carpeta | Pieza | iframe |
|---|---|---|
| `cuadernos/` | Cuadernos de la asignatura en Gemini Notebook (general y bibliografía) | 340 |

## Ejercicios y videolecciones
`ejercicios/index.html` → página para la página de Canvas «Ejercicios y videolecciones» (a la que enlaza la portada). Sustituye a los banners de imagen. Identidad de marca de la asignatura.
- Cabecera «Ejercicios y videolecciones» + «Mira · Practica · Aprende». Dos secciones con rótulo numerado, como la portada: **01 Mira · Videolecciones** (3 tarjetas carbón con botón de reproducir amarillo: **0 La estructura de la noticia** · 1 Cabeza de titulación · 2 La entradilla; la antigua «Clase online / Videolección 3 · Cómo hacer titulares» se ha quitado) y **02 Practica · Ejercicios** (5 tarjetas blancas con número grande en Anton: 1 Cabeza de titulación · 2 Cabeza de titulación y entradilla · 3 Jerarquización y ordenación lógica · 4 Cobertura de una rueda de prensa · 5 Cobertura informativa).
- Enlaces en el bloque `ENLACES` (claves `vl0`–`vl2`, `ej1`–`ej5`; pestaña nueva); vacío = «Próximamente». Tareas de Canvas con la dirección base (`/assignments/NNN`, sin `/launch`, `/taking/…` ni `?display=…`): VL0 627763 · VL1 579070 · VL2 579071 · Ej1 579025 · Ej2 579027 · Ej3 579024 · Ej4 579010 · Ej5 579014.
- Los cinco ejercicios en una fila hasta 700 px; las videolecciones en fila hasta 600 px. Sin año académico.

| Carpeta | Pieza | iframe |
|---|---|---|
| `ejercicios/` | Ejercicios y videolecciones | 780 |

## Unidades temáticas
`unidades/index.html` → página para la página de Canvas «Unidades temáticas» (a la que enlaza el banner de la portada). Identidad de marca de la asignatura.
- Cabecera: banner carbón con filete amarillo, «Unidades temáticas» en Anton y el lema «Estudia. Practica. Aprende.» en amarillo (como en la portada).
- Cuatro tarjetas 2×2 que **conservan los banners animados originales de cada unidad** (1 Los géneros periodísticos · 2 La noticia · 3 La estructura de la noticia · 4 El estilo periodístico informativo), con un pie blanco (filete negro de 2 px, «Unidad N», título en Anton y acción).
- **Los GIF originales (18–29 MB cada uno, ~93 MB en total) se convirtieron a MP4** H.264 de 800 px (`media/u1…u4.mp4`, 0,2–0,5 MB; ~1,3 MB en total) con imagen fija `media/u1…u4.jpg` (`poster`). `<video muted loop playsinline preload="none">`: se cargan y reproducen solo mientras están a la vista (IntersectionObserver) y se pausan fuera; con `prefers-reduced-motion` queda la imagen fija.
- **Banners sin texto**: se ha borrado de los vídeos el «Unidad N» y el título que llevaban dentro de la mancha amarilla (el nombre ya va en el pie de la tarjeta). Script `unidades/herramientas/limpiar-banner.py` (Python con Pillow, SciPy y OpenCV; requiere ffmpeg): detecta fotograma a fotograma el texto encerrado en la mancha amarilla y lo rellena siguiendo el degradado (inpainting), remuestrea a 25 fps y codifica a MP4 de 800 px. Uso: `python3 limpiar-banner.py banner.gif media/uN.mp4 [ms_a_recortar_al_inicio]`. Las unidades 2 y 4 se recortan 600 ms al principio (fundido de entrada). Imagen fija: `ffmpeg -ss <segundo> -i media/uN.mp4 -frames:v 1 -q:v 5 media/uN.jpg`.
- Enlaces en el bloque `ENLACES` (claves `u1`–`u4`; pestaña nueva); vacío = «Próximamente». Páginas de Canvas `…/courses/70362/pages/unidad-1` … `unidad-4`.

| Carpeta | Pieza | iframe |
|---|---|---|
| `unidades/` | Unidades temáticas con banners animados | 990 |
