# LEEME · Proyecto 3 · Narrativa visual integrada · Equipo 3

**Visualización I · Universidad Externado de Colombia** · Docentes: Adriana Pineda y Paola Moreno
**Integrantes:** Alejandro Pardo Costo y Juan Tomás Rincón Pinzón · Modalidad A (presentación narrativa)

> **¿Mismo título, mismo ingreso?** Diferencias de ingreso laboral entre mujeres y hombres con educación superior en Colombia (GEIH, enero–julio 2026), contadas para mujeres de 18 a 28 años que van a buscar su primer empleo.

## Cómo recorrer la entrega

1. **Presentación:** `Equipo3_Proyecto3_Presentacion.pdf` (10 diapositivas). La versión `Equipo3_Proyecto3_Presentacion.html` es la misma, interactiva: se abre en el navegador, se avanza con las flechas y sus botones abren los productos interactivos de esta carpeta.
2. **Power BI:** `PowerBI/Equipo3_Proyecto3_Dashboard.pbix` y el enlace publicado en `PowerBI/Equipo3_Proyecto3_Enlace_PowerBI.txt`.
3. **Python:**
   - `Python/Equipo3_Proyecto3_Analisis.ipynb`, ejecutado, con código comentado y la lectura de cada resultado.
   - Los dos interactivos de Plotly en HTML, que se abren con doble clic, sin internet:
     - `Python/Equipo3_Proyecto3_Plotly_Panorama_Sectores.html`;
     - `Python/Equipo3_Proyecto3_Plotly_Sectores_por_Edad.html`.
4. **R:**
   - `R/Equipo3_Proyecto3_Mapa.Rmd` y su versión ejecutada, `R/Equipo3_Proyecto3_Mapa.html`;
   - el mapa en PNG;
   - la figura de márgenes de error;
   - el mapa interactivo en `tmap`.
5. **Fuentes, definiciones y limitaciones:** `Equipo3_Proyecto3_Fuentes_Definiciones_Limitaciones.md`. Un resumen está también en la diapositiva 10.
6. **Uso de IA:** `Equipo3_Proyecto3_Anexo_IA.pdf` (una página).

## Cómo reproducir los resultados

Esta carpeta es una copia de los productos finales. **El proyecto completo y reproducible está en el repositorio público:**
https://github.com/AlejandroP212/proyecto3-narrativa-visual

El repositorio incluye:
- los datos originales sin modificar: los microdatos de la GEIH 2026 de enero a julio (zip) y la cartografía municipal del DANE (shapefile);
- los datos procesados;
- el código, con rutas relativas;
- las dependencias (`requirements.txt` y la lista de paquetes de R);
- un `README.md` con los pasos.

Para reproducir:

1. Descargar o clonar el repositorio.
2. **Python 3.10 o superior:**
   ```bash
   pip install -r requirements.txt
   jupyter nbconvert --to notebook --execute --inplace python/Equipo3_Proyecto3_Analisis.ipynb
   ```
   También se puede abrir en VS Code o en Google Colab y usar "Ejecutar todas". Si el notebook no encuentra los datos (por ejemplo en Colab), descarga el zip de la GEIH desde el repositorio.
3. **R 4.4 o superior** (probado con 4.6.2); no necesita RTools:
   ```r
   install.packages(c("sf", "dplyr", "readr", "ggplot2", "ggspatial", "classInt", "tmap", "rmarkdown", "knitr"))
   ```
   Luego, abrir `r/Equipo3_Proyecto3_Mapa.Rmd` en RStudio y hacer **Knit**. El mapa usa la tabla que genera el notebook (`datos/procesados/brecha_departamento.csv`), que ya está en el repositorio.
4. **Power BI Desktop:** abrir `powerbi/Equipo3_Proyecto3_Dashboard.pbix`.

## Fuentes

- DANE, Gran Encuesta Integrada de Hogares (GEIH) 2026, marco 2018, enero–julio. https://microdatos.dane.gov.co/index.php/catalog/900
- DANE, Marco Geoestadístico Nacional, capa municipal `MGN_MPIO_POLITICO` (material del curso, sesión 02 de R).
