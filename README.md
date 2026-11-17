# Proyecto 3: Narrativa visual integrada · Equipo 3

**Visualización I · Universidad Externado de Colombia** · Docentes: Adriana Pineda y Paola Moreno
**Integrantes:** Alejandro Pardo Costo y Juan Tomás Rincón Pinzón

> **¿Ganan lo mismo con el mismo título?** Diferencias de ingreso laboral entre mujeres y hombres con educación superior en Colombia (GEIH, enero–julio 2026), contadas para mujeres jóvenes que entran al mercado laboral.

| | |
|---|---|
| **Audiencia** | Mujeres de 18 a 28 años que terminan o acaban de terminar un programa técnico, tecnológico o universitario y van a buscar su primer empleo. |
| **Pregunta** | ¿Qué diferencias de ingreso laboral se observan entre mujeres y hombres con educación superior en Colombia (enero–julio 2026) y cómo varían según la edad y el departamento? |
| **La Gran Idea** | Ver [`docs/Definiciones_compartidas.md`](docs/Definiciones_compartidas.md) (versión final en la presentación). |

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
├── presentacion/                 ← presentación narrativa en HTML (máx. 10 diapositivas) e img/
├── docs/                         ← definiciones compartidas, fuentes y limitaciones, anexo IA, instrucciones
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
install.packages(c("sf", "ggplot2", "dplyr", "readr", "classInt", "tmap", "rmarkdown", "knitr"))
```
- Abre `r/Equipo3_Proyecto3_Mapa.Rmd` y haz **Knit** (o ejecuta `rmarkdown::render("r/Equipo3_Proyecto3_Mapa.Rmd")`).
- Usa `datos/originales/cartografia/` y `datos/procesados/brecha_departamento.csv`, y exporta el mapa a `r/salidas/`.

### 3. Presentación
Abre `presentacion/Equipo3_Proyecto3_Presentacion.html` en un navegador. Se avanza con las flechas del teclado. La versión PDF está en `entregables/`.

### Power BI
- Archivo: `powerbi/Equipo3_Proyecto3_Dashboard.pbix`. Ábrelo con Power BI Desktop.
- Enlace en Power BI Service: https://app.powerbi.com/links/N7NaGvljjq?ctid=3b944d9a-1051-4685-b09d-9a95ee2dbd99&pbi_source=linkShare

## Fuentes
- **DANE, Gran Encuesta Integrada de Hogares (GEIH) 2026**, marco 2018, enero–julio. Microdatos: https://microdatos.dane.gov.co/index.php/catalog/900
- **DANE, Marco Geoestadístico Nacional (MGN)**, capa municipal `MGN_MPIO_POLITICO`, entregada como material del curso (sesión 02 de R). Los departamentos se obtienen uniendo los municipios por `DPTO_CCDGO`.

Las definiciones, los indicadores y las limitaciones están en [`docs/Definiciones_compartidas.md`](docs/Definiciones_compartidas.md).
