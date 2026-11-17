# Guía de apoyo: Proyecto 3 (no se entrega)

> Para estudiar antes de la sustentación. La docente puede preguntarle **a cualquiera** por Power BI, Python o R y pedir que se abra o ejecute un componente. Aquí está qué se hizo, qué no y por qué, con las preguntas que probablemente harán.

---

## Parte 1. Python: `python/Equipo3_Proyecto3_Analisis.ipynb`

### 1.1 El recorrido en una frase por sección

| Sección | Qué hace | Cómo lo dices en la sustentación |
|---|---|---|
| Instalación | `%pip install` de las librerías | "Para que corra igual en Colab y en VS Code." |
| 1. Audiencia | Tabla audiencia → necesidad → pregunta y reparto entre herramientas | "Cada herramienta responde una parte distinta: Power BI el panorama, Python la distribución y la edad, Plotly los sectores, R el territorio." |
| 2. Rutas | Busca el zip en `.` o `..`; si no está (Colab), lo baja de GitHub | "Rutas relativas: corre desde el repo sin cambiar nada." |
| Ingredientes | Colores, categorías, `miles()` y `pct()` | "Todo lo que se repite está definido una vez: si cambia un color, cambia en todos los gráficos." |
| Carga | Lee los 14 CSV dentro del zip, solo las columnas necesarias | "No descomprimimos ni modificamos el original." |
| Unión | `merge(..., validate="1:1")` con la llave de 5 columnas | "Si hubiera duplicados, pandas se detiene. Incluir HOGAR evita el error que tuvimos en el P1." |
| Variables y filtros | Convierte tipos, calcula el ingreso por hora y filtra | "De 206.712 ocupados quedan 76.488 con educación superior, ingreso y horas." |
| Cómo se calculan | Funciones ponderadas, brecha y bootstrap | Ver 1.3 |
| Cifras de control | Tabla que debe coincidir con Power BI | "18,5 % mensual y 13,7 % por hora; Power BI da lo mismo." |
| Composición | Por qué la brecha general es casi 0 | Ver 1.4 |
| Gráfico 1 | Densidades por sexo y nivel | Ver 1.5 |
| Gráfico 2 | Barras de la brecha por edad con IC | Ver 1.5 |
| Plotly | Dispersión hombres vs. mujeres por sector, con menú de edad | Ver 1.6 |
| Tabla para R | Brecha por departamento + IC + CV, exportada a CSV | "El mapa usa exactamente estos números." |
| Hallazgos y limitaciones | Resumen para la presentación | Se lee tal cual en la diapositiva de cierre. |

### 1.2 Conceptos que tienes que poder explicar sin mirar

- **FEX_C18 (factor de expansión).** Cada persona encuestada representa a muchas personas del país. Si alguien tiene FEX = 250, "cuenta" por 250. Por eso todos los promedios son ponderados: `np.average(x, weights=FEX)`. Sin ponderar, las regiones sobremuestreadas pesarían de más.
- **Ingreso por hora.** `INGLABO / (P6800 × 4,3333)`. P6800 son las horas *semanales* y 4,3333 son las semanas promedio de un mes (52/12).
- **Por qué la brecha por hora es la principal.** La brecha mensual (18,5 %) mezcla dos cosas: lo que se paga por hora y cuántas horas se trabajan. Por hora (13,7 %) se compara a quienes trabajan jornadas distintas en igualdad de condiciones. La brecha baja, pero no desaparece.
- **Razón de sumas vs. promedio de razones.** Usamos Σ ingreso / Σ horas del grupo, igual que la medida DAX de Power BI. El promedio de los ingresos por hora individuales da 18,2 % porque es muy sensible a personas con muy pocas horas reportadas. La razón de sumas se lee como "por cada hora trabajada, el grupo recibe…".
- **Educación superior = P3042 de 8 a 13.** Técnica profesional (8), tecnológica (9), universitaria (10), especialización (11), maestría (12) y doctorado (13). No incluimos normalista (7): son 277 casos y su clasificación es ambigua.

### 1.3 El bootstrap (la pregunta técnica más probable)

**Qué es.** Una forma de medir cuánto cambiaría la cifra si se hubiera tomado otra muestra. Se repite el cálculo 500 veces "remuestreando" las viviendas y se mira dónde cae el 95 % de los resultados. Ese rango es el intervalo de confianza (IC).

**Cómo está hecho (función `brecha_con_intervalo`).**
1. Se suman el ingreso×FEX y las horas×FEX **por vivienda y sexo**.
2. Cada vivienda recibe en cada repetición un peso aleatorio de una distribución Poisson con media 1 (0, 1, 2…). Esto equivale a sacar viviendas con reemplazo y es rápido porque se resuelve con una multiplicación de matrices (`pesos @ ingreso`).
3. Con esos pesos se recalcula el ingreso por hora de hombres y mujeres y la brecha. Se toman los percentiles 2,5 y 97,5.

**Por qué por vivienda y no por persona.** Las personas de un mismo hogar se parecen (mismo barrio, mismo estrato). Remuestrear personas sueltas daría intervalos demasiado estrechos.

**Limitación que debes decir tú antes de que te la pregunten.** El DANE usa el diseño completo (estratos y conglomerados), que no viene en las tablas públicas, así que nuestros intervalos son una aproximación y los reales pueden ser algo más amplios.

**CV (coeficiente de variación).** Es la desviación estándar del bootstrap dividida por la estimación, en %. Umbrales del DANE: hasta 7 % precisa, de 7 % a 15 % aceptable, de 15 % a 20 % regular y más de 20 % poco precisa. Todos los departamentos dan CV ≤ 15 % en el ingreso por hora. Lo incierto es la **diferencia**, por eso el mapa usa el IC de la brecha.

### 1.4 El efecto de composición

- Entre **todos** los ocupados, las mujeres ganan por hora un 3,8 % *más* que los hombres. ¿Contradice la historia? No.
- El 44,1 % de las mujeres ocupadas tiene educación superior, frente al 29,7 % de los hombres, y la educación superior se asocia con más ingreso. Al mezclar niveles, las mujeres "suben" el promedio por tener más títulos.
- Al comparar personas con el **mismo** nivel, aparece la brecha. Por eso la historia se cuenta siempre a igual nivel educativo.
- Esto también explica por qué la tarjeta general de Power BI (8,6 % mensual) es menor que la brecha de cada nivel.

### 1.5 Los gráficos de Seaborn

**Gráfico 1: densidades (`sns.kdeplot`).**
- **Qué muestra.** Dónde se concentra el ingreso por hora de cada sexo, en cada nivel. Las líneas punteadas son las medianas ponderadas.
- **Argumentos clave:**
  - `weights="FEX"`: la curva representa a la población, no a la muestra.
  - `common_norm=False`: cada curva suma 1 por separado. Si no, el grupo con más personas se vería más alto solo por tamaño.
  - `bw_adjust=1.2`: suaviza un poco el pico.
- **Por qué cortamos en $ 60 mil.** Hay valores extremos (el máximo supera los 12 millones por hora) que dejaban plana la curva de los hombres universitarios. Las curvas usan el 95,5 % de la población; las medianas y todas las cifras usan el 100 %.
- **Lectura:** en los tres niveles la curva ocre está a la izquierda. No es un efecto de unos pocos sueldos altos.

**Gráfico 2: barras con IC.**
- Seaborn no calcula un IC ponderado por vivienda, así que el IC se calcula con nuestro bootstrap y se dibuja con `ax.errorbar`.
- La barra 18–28 va en el color de acento (la audiencia) y el resto en gris: es una decisión de jerarquía visual.
- El eje y va de 0 a 30 %. Empieza en cero, como debe ser en barras, para no exagerar diferencias.
- **Diferencia 29–40 menos 18–28:** 6,7 puntos con un IC aproximado de 1,0 a 12,3. No incluye el 0, así que la distancia entre grupos no es solo ruido de la muestra.
- **Lo que NO dice:** que la brecha "crece" con la edad para una persona. Son grupos distintos medidos al mismo tiempo (datos transversales).

**Por qué títulos neutrales.** Es la retroalimentación de la docente en el P1: el título describe ("Brecha de ingreso por hora… por grupo de edad") y lo que se observa va en el subtítulo.

### 1.6 Plotly

- **Construcción.** Un `go.Scatter` por grupo de edad (5 trazas) más la línea de igualdad. El menú (`updatemenus`) cambia qué traza es visible y actualiza el subtítulo.
- **Por qué los ejes son fijos y la escala 1:1** (`scaleanchor`). Para comparar grupos sin que el gráfico "mienta" al cambiar de opción, y para que la diagonal sea realmente de 45°.
- **Colores.** Rojo si las mujeres reciben menos y gris si reciben igual o más. No se usa el azul de "Hombre" para no confundir.
- **Muestra mínima.** Solo sectores con al menos 50 hombres y 50 mujeres en la muestra para ese grupo. Con menos, la cifra cambia demasiado de una muestra a otra.
- **Aporte de la interactividad.** Con 18 sectores × 5 grupos, la versión estática necesitaría 90 etiquetas. El hover da el detalle de cada sector y el menú permite ubicar el caso propio.
- **Pregunta probable: "¿por qué en salud la brecha es tan grande (42,3 %)?"** Respuesta: el dato no separa profesiones. En salud trabajan médicos y enfermeras, y la composición puede explicar parte de la diferencia, pero los datos no permiten afirmarlo.

### 1.7 Qué NO hicimos y por qué

| No hicimos | Por qué |
|---|---|
| Regresión o "brecha ajustada" | La guía pide comunicación ciudadana descriptiva; un modelo invitaría a lecturas causales que los datos no sostienen. |
| Excluir valores extremos de las cifras | Para que coincidan con Power BI; solo se acota el dibujo de las curvas. |
| Mapa o análisis por departamento solo con jóvenes | Varios departamentos quedan con menos de 30 hombres jóvenes en la muestra. |
| Usar la mediana como cifra principal | Muchos ingresos se repiten (el mismo valor exacto), y por departamento la mediana daba brechas de 0 % sin sentido. |
| Dash | No se pide; un HTML de Plotly se abre en cualquier navegador sin servidor. |

### 1.8 Preguntas probables y respuestas cortas

1. **¿Por qué 18–28?** Es el rango de juventud de la Ley 1622 de 2013 (Estatuto de Ciudadanía Juvenil) y coincide con quienes terminan estudios superiores.
2. **¿Las cifras son anuales?** No. Son enero–julio de 2026 acumulados.
3. **¿Esto prueba discriminación?** No. Es una diferencia descriptiva: no controla carrera, cargo, experiencia ni empresa.
4. **¿Qué pasa si corro el notebook en Colab?** Si no encuentra el zip local, lo descarga del repo público.
5. **¿Cómo sabes que la unión no duplicó personas?** Por `validate="1:1"` y porque hay 0 ocupados sin pareja.
6. **¿Por qué ese color para mujeres?** El azul/morado del P1 tenía un contraste de 1,1:1 entre sí y no se distinguía con daltonismo. El ocre `#B8862B` tiene 3,2:1 contra el blanco y se separa del azul en luminosidad.

---

## Parte 2. Preparación para R (lo que sigue)

### 2.1 Qué vamos a construir

`r/Equipo3_Proyecto3_Mapa.Rmd`: un mapa coroplético de Colombia por **departamento** con la brecha de ingreso por hora en educación superior (todas las edades, enero–julio 2026). Los departamentos donde la brecha **no es concluyente** (el IC 95 % incluye el 0) van en gris con su propia entrada en la leyenda.

### 2.2 Los pasos y lo que significa cada uno

| Paso | Código (sf + dplyr + ggplot2) | Qué debes saber explicar |
|---|---|---|
| 1. Leer la cartografía | `st_read("datos/originales/cartografia/MGN_MPIO_POLITICO.shp")` | Es el Marco Geoestadístico Nacional del DANE, capa municipal (1.121 municipios). Viene en WGS84 (EPSG:4326). |
| 2. Reproyectar | `st_transform(crs = 9377)` | EPSG:9377 = MAGNA-SIRGAS / Origen Nacional, la proyección plana oficial de Colombia. Las áreas y distancias quedan en metros y el país no sale deformado. |
| 3. Pasar de municipios a departamentos | `group_by(DPTO_CCDGO) %>% summarise()` | `summarise` sobre un objeto sf **une las geometrías** (disuelve los límites internos). La GEIH no permite cifras municipales. |
| 4. Simplificar | `st_simplify(dTolerance = 1000)` | Quita vértices (tolerancia de 1 km) para que el mapa pese poco. No cambia lo que se lee a escala nacional. |
| 5. Leer la tabla de Python | `read_csv(..., col_types = cols(DPTO = col_character()))` | El código se lee como **texto** para no perder el 0 inicial ("05" Antioquia). Si se lee como número, la unión falla. |
| 6. Unión espacial (por atributo) | `left_join(dptos, brecha, by = c("DPTO_CCDGO" = "DPTO"))` | Se verifica que los 33 departamentos encuentren pareja (`anti_join` vacío). Es el criterio "integridad de uniones" de la rúbrica. |
| 7. Clasificar la brecha | `classInt::classIntervals(style = "fixed")` con cortes 0–5–10–15–20–25+ | Se usan cortes fijos y redondos porque la audiencia los lee fácil y se pueden comparar con la cifra nacional (13,7 %). Los cuantiles o k-means darían límites raros (12,73 %). |
| 8. Dibujar | `geom_sf(aes(fill = clase))` + `scale_fill_manual` | Escala secuencial de un solo tono (más oscuro = brecha mayor). Gris = no concluyente. |
| 9. Elementos cartográficos | Título, subtítulo, leyenda, fuente, **escala** y **norte** | En ggplot se agregan con `ggspatial` (`annotation_scale`, `annotation_north_arrow`), o se hace en `tmap` con `tm_scalebar` y `tm_compass`. |
| 10. San Andrés | Recuadro aparte (inset) o nota | Queda lejos del continente; si no se pone aparte, el mapa se encoge. |
| 11. Exportar | `ggsave("r/salidas/Equipo3_Proyecto3_Mapa.png", dpi = 300)` | PNG para la presentación y HTML del Rmd para entregar. |

### 2.3 Decisiones que te van a preguntar

- **¿Por qué departamentos y no municipios o ciudades?** La GEIH es representativa por departamento (en el agregado anual), no por municipio. Las 23 ciudades son puntos, no áreas, y el Power BI ya las muestra.
- **¿Por qué gris y no el color de la brecha estimada?** Si el IC incluye el 0, no podemos afirmar que haya brecha. Pintarlo con un color de brecha sería inventar una diferencia. Es honestidad de escala (criterio de ética de la rúbrica).
- **¿Por qué una escala secuencial y no divergente?** Casi todos los valores concluyentes son positivos (las mujeres reciben menos). Una divergente centrada en 0 desperdiciaría la mitad de la paleta.
- **¿El mapa dice que vivir en X *causa* más brecha?** No. Describe dónde se observa una brecha mayor.
- **Lectura del mapa:**
  - Brechas altas y concluyentes: Guaviare (28,1 %), Casanare (27,3 %), Caldas (24,9 %), Quindío (24,1 %) y Meta (20,8 %).
  - 12 departamentos sin brecha concluyente.
  - Bogotá: alrededor de 13,5 % (IC 8,7 % – 18,6 %), cerca del promedio nacional.

### 2.4 Antes de abrir RStudio

1. R 4.6.2 ya está instalado y `sf` carga bien.
2. Falta instalar `ggspatial` (escala y norte en ggplot) y `readr`:
   ```r
   install.packages(c("ggspatial", "readr"))
   ```
3. El Rmd se abre desde `r/` y usa rutas relativas (`../datos/...`). En RStudio, el **Knit** se ejecuta desde la carpeta del Rmd, así que funciona sin `setwd()`.
