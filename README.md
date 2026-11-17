# Proyecto 3: Narrativa visual integrada · Equipo 3

**Visualización I · Universidad Externado de Colombia** · Docentes: Adriana Pineda y Paola Moreno
**Integrantes:** Alejandro Pardo Costo y Juan Tomás Rincón Pinzón

> **¿Ganan lo mismo con el mismo título?** Diferencias de ingreso laboral entre mujeres y hombres con educación superior en Colombia (GEIH, enero–julio 2026), contadas para mujeres jóvenes que entran al mercado laboral.

| | |
|---|---|
| **Audiencia** | Mujeres de 18 a 28 años que terminan o acaban de terminar un programa técnico, tecnológico o universitario y van a buscar su primer empleo. |
| **Pregunta** | ¿Qué diferencias de ingreso laboral se observan entre mujeres y hombres con educación superior en Colombia (enero–julio 2026) y cómo varían según la edad y el departamento? |
| **La Gran Idea** | **El título no iguala el pago.** Con el mismo nivel educativo, las mujeres reciben 13,7 % menos por hora que los hombres. Al comenzar la vida laboral (18 a 28 años) la diferencia es menor, 7,4 %, pero en el grupo de 29 a 40 años es casi el doble y aparece en casi todos los sectores y en la mayoría de los departamentos. |

## Estructura

```
proyecto3-narrativa-visual/
├── README.md                     ← este LEEME: cómo reproducir todo
├── LEEME_TOMAS.md                ← tareas de Power BI
├── requirements.txt              ← dependencias de Python
├── datos/
│   ├── originales/               ← SIN modificar
│   │   ├── geih_2026/            ← DANE GEIH 2026, enero–julio (Características generales + Ocupados), zip
│   │   └── cartografia/          ← DANE MGN, municipios (shapefile, WGS84)
│   └── procesados/               ← generados por el notebook (insumo del mapa en R)
├── powerbi/                      ← dashboard .pbix (Power BI)
├── python/                       ← notebook (Seaborn + Plotly) y html/ con los Plotly exportados
├── r/                            ← R Markdown del mapa y salidas/ (PNG + HTML)
├── presentacion/                 ← presentación narrativa en HTML y PDF (10 diapositivas) e img/
├── docs/                         ← definiciones compartidas, anexo de IA, guion de exposición, instrucciones
├── scripts/armar_entregables.py  ← copia los productos finales a entregables/
└── entregables/                  ← copia final con la convención Equipo3_Proyecto3_* (lo que se envía por correo)
```

## Cómo reproducir

Orden: **1. Python → 2. R → 3. Presentación.** Power BI es independiente.

### 1. Python (notebook)
Requiere Python 3.10 o superior.
```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter nbconvert --to notebook --execute --inplace python/Equipo3_Proyecto3_Analisis.ipynb
```
- También se puede abrir en VS Code o Colab y usar "Ejecutar todas"; la primera celda instala lo necesario.
- El notebook lee el zip de `datos/originales/geih_2026/` con rutas relativas y escribe:
  - `datos/procesados/brecha_departamento.csv`
  - los HTML de Plotly en `python/html/`

### 2. R (mapa)
Requiere R ≥ 4.4 (probado con R 4.6.2) y RStudio. **No necesita RTools.**
```r
install.packages(c("sf", "ggplot2", "dplyr", "readr", "classInt", "ggspatial", "tmap", "rmarkdown", "knitr"))
```
- Abre `r/Equipo3_Proyecto3_Mapa.Rmd` y haz **Knit** (o ejecuta `rmarkdown::render("r/Equipo3_Proyecto3_Mapa.Rmd")`).
- Usa `datos/originales/cartografia/` y `datos/procesados/brecha_departamento.csv`. Genera:
  - `r/Equipo3_Proyecto3_Mapa.html`: el documento con código, salidas y lectura;
  - `r/salidas/Equipo3_Proyecto3_Mapa_Brecha_Departamento.png`: el mapa estático, 300 ppp;
  - `r/salidas/Equipo3_Proyecto3_Intervalos_Departamento.png`: el margen de error por departamento;
  - `r/salidas/Equipo3_Proyecto3_Mapa_Interactivo.html`: el mapa interactivo en `tmap`, que se abre con doble clic.

### 3. Presentación
Abre `presentacion/Equipo3_Proyecto3_Presentacion.html` en un navegador.

| Tecla | Acción |
|---|---|
| ← → | Cambiar de diapositiva |
| **N** | Notas del expositor |
| **F** | Pantalla completa |
| **G** | Vista general |

Los botones de las diapositivas abren los interactivos de Plotly, el mapa de `tmap` y el tablero de Power BI. Las imágenes están en `presentacion/img/`. Las capturas de Plotly se tomaron de los HTML con el navegador.

- **PDF:** abre el HTML en Edge o Chrome, elige Imprimir → Guardar como PDF, sin márgenes y con gráficos de fondo, y guárdalo como `presentacion/Equipo3_Proyecto3_Presentacion.pdf`. Cada diapositiva queda en una página.
- **Anexo de IA:** se genera igual, a partir de `docs/Equipo3_Proyecto3_Anexo_IA.html`, en tamaño carta.

### 4. Carpeta de entregables
```bash
python scripts/armar_entregables.py
```
Copia los productos finales a `entregables/` con nombres `Equipo3_Proyecto3_*`: presentación (PDF y HTML autocontenido), anexo de IA, fuentes y definiciones, LEEME, `.pbix`, notebook, Plotly y mapa. Vuelve a correrlo cada vez que cambie un producto.

### Power BI
- Archivo: `powerbi/Equipo3_Proyecto3_Dashboard.pbix`. Ábrelo con Power BI Desktop.
- Enlace en Power BI Service: https://app.powerbi.com/links/N7NaGvljjq?ctid=3b944d9a-1051-4685-b09d-9a95ee2dbd99&pbi_source=linkShare

## Fuentes
- **DANE, Gran Encuesta Integrada de Hogares (GEIH) 2026**, marco 2018, enero–julio. Microdatos: https://microdatos.dane.gov.co/index.php/catalog/900
- **DANE, Marco Geoestadístico Nacional (MGN)**, capa municipal `MGN_MPIO_POLITICO`, entregada como material del curso (sesión 02 de R). Los departamentos se obtienen uniendo los municipios por `DPTO_CCDGO`.

Las definiciones, los indicadores y las limitaciones están en [`docs/Definiciones_compartidas.md`](docs/Definiciones_compartidas.md). El uso de IA se declara en `docs/Equipo3_Proyecto3_Anexo_IA.pdf`.
