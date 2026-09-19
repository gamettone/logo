# Cómo se hizo el logo de gamettone

gamettone es la organización de GitHub hermana de infranettone, dedicada a juegos. Su logo parte del de infranettone (`logo-infranettone.png`): el mismo panettone cortado, pero con algo relacionado con juegos en el interior en lugar de servidores.

## Archivos

| Archivo | Qué es | Herramienta | Tamaño |
|---|---|---|---|
| `logo-infranettone.png` | Logo original de infranettone, usado como base | — | 400×400 PNG |
| **`logo-gamettone-comercial.jpeg`** | **Logo oficial.** Panettone con un mando de consola dentro, sin marcas ni personajes | Google Gemini | 1024×1024 JPEG |
| `logo-gamettone-gemini-full-no-comercial.jpeg` | Versión detallada con una estantería gamer (consolas, juegos y personajes reales). Solo para uso no comercial | Google Gemini | 1024×1024 JPEG |
| `logo-gamettone-python-pil.png` | Primer boceto hecho con código | Python + Pillow (`make_logo.py`) | 400×400 PNG |
| `make_logo.py` | Script que genera el boceto | — | — |

## Logo oficial: `logo-gamettone-comercial.jpeg`

- **Cómo se hizo:** con Google Gemini (modelo de imagen "Nano Banana"), editando `logo-infranettone.png` en varias iteraciones.
- **Contenido:** el panettone de infranettone con un mando de consola oscuro que ocupa el hueco. Tiene dos joysticks, una cruceta y cuatro botones de colores. Alrededor del mando se ve la miga del bizcocho.
- **Por qué es el oficial:** se hizo para no infringir los derechos de ninguna empresa. Por eso no aparecen personajes, logotipos ni nombres de juegos o consolas.
- **Tamaño pequeño:** al ser un único elemento grande, se reconoce bien en tamaños pequeños, como el avatar de GitHub.
- **Formato:** fondo blanco, sin transparencia.

### Revisión de derechos pendiente

El diseño del mando recuerda mucho al de Xbox. Los botones Y, X, B y A llevan letras y los mismos colores que el mando de Xbox, y la forma del cuerpo es muy parecida. Para que el logo sea genérico del todo, se recomienda pedir a Gemini botones sin letras (o con símbolos propios) y un mando de forma menos reconocible.

## Versión no comercial: `logo-gamettone-gemini-full-no-comercial.jpeg`

Esta versión convierte el hueco en una estantería gamer. Dentro hay:

- un monitor CRT con un simulador de vuelo;
- consolas: PS2, PS3, Wii, Nintendo DS y Game Boy Advance;
- cajas etiquetadas NES, SNES, N64, GAME BOY, GBA, PlayStation y PC;
- un PC con refrigeración líquida y luces azules, con ratón y alfombrilla;
- piezas de Tetris;
- figuras y guiños a Mario, GTA San Andreas, Gran Turismo 4 y Rocket League.

Muestra marcas y personajes con derechos, así que **no debe usarse como logo oficial**. Además, en tamaños pequeños los detalles no se distinguen.

## Otras herramientas de IA posibles

| Herramienta | Por qué |
|---|---|
| **Google Gemini ("Nano Banana")** | La usada. Edita una parte de la imagen sin tocar el resto y mantiene el estilo. |
| ChatGPT (generación de imágenes de GPT) | Alternativa fiel al estilo, aunque a veces redibuja la imagen entera. |
| FLUX Kontext (Black Forest Labs) | Pensada para editar con una instrucción. Se usa desde Replicate, fal.ai o ComfyUI. |
| Adobe Firefly / Photoshop "Relleno generativo" | Seleccionas solo el hueco y describes lo que quieres dentro. |
| Midjourney | Buena para explorar ideas, pero peor editando una imagen exacta. |

## Boceto inicial: `logo-gamettone-python-pil.png`

Antes de usar Gemini se hizo un boceto con código para tener una idea de cómo quedaría. Tiene el mismo panettone, con un mando de consola dibujado en el hueco.

### Cómo regenerarlo

```bash
pip install pillow
python3 make_logo.py   # lee logo-infranettone.png y escribe logo-gamettone-python-pil.png
```

### Pasos (`make_logo.py`)

Todo se hace con Python 3 y Pillow, sin ninguna IA de imágenes.

1. **Detectar el hueco.** En la zona del corte (x 100–300, y 125–330), se marca como "interior" todo píxel que no tenga el color cálido del bizcocho.
2. **Borrar los LEDs sueltos.** Con un relleno por inundación desde el borde, solo se conservan los píxeles cálidos conectados con el bizcocho. Así se eliminan los LEDs y el cable del original.
3. **Suavizar la máscara.** Filtros de mínimo y máximo para quitar ruido, y un desenfoque de 0,8 px en el borde.
4. **Rellenar el interior.** Degradado marrón oscuro, como un hueco en sombra.
5. **Dibujar el mando.** Con formas geométricas a 4 veces el tamaño, reducidas luego con LANCZOS. Incluye:
   - la cruceta y los dos joysticks;
   - los botones de start y select;
   - cuatro botones de colores;
   - un LED naranja con brillo;
   - una sombra debajo.
6. **Componer.** El mando se superpone al panettone vaciado.

### Limitaciones del boceto

- El estilo plano del mando no encaja del todo con la ilustración del panettone.
- Queda un pequeño resto dorado del cable original en la parte de abajo del hueco.
