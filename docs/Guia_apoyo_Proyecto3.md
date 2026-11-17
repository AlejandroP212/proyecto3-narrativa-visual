# Guía de apoyo: Proyecto 3 (no se entrega)

> Para estudiar antes de la sustentación. La docente puede preguntarle **a cualquiera** por Power BI, Python o R y pedir que se abra o ejecute un componente. Aquí está qué se hizo, qué no y por qué, con las preguntas que probablemente harán.

---

## Parte 1. Python: `python/Equipo3_Proyecto3_Analisis.ipynb`

### 1.1 El recorrido en una frase por sección

| Sección | Qué hace | Cómo lo dices en la sustentación |
|---|---|---|
| Instalación | `%pip install` de las librerías | "En VS Code hace falta la primera vez; en Colab no es obligatoria porque ya trae las librerías, pero no hace daño y así 'Ejecutar todas' funciona igual en los dos." |
| 1. Audiencia | Tabla audiencia → necesidad → pregunta y reparto entre herramientas | "Cada herramienta responde una parte distinta: Power BI el panorama, Python la distribución y la edad, Plotly los sectores, R el territorio." |
| 2. Rutas | Busca el zip en `.` o `..`; si no está (Colab), lo baja de GitHub | "Rutas relativas: corre desde el repo sin cambiar nada." |
| Configuración general | Colores, categorías, `miles()` y `pct()` | "Todo lo que se repite está definido una vez: si cambia un color, cambia en todos los gráficos." |
| Carga | Lee los 14 CSV dentro del zip, solo las columnas necesarias | "No descomprimimos ni modificamos el original." |
| Unión | `merge(..., validate="1:1")` con la llave de 5 columnas | "Si hubiera duplicados, pandas se detiene. Incluir HOGAR evita el error que tuvimos en el P1." |
| Variables y filtros | Convierte tipos, calcula el ingreso por hora y filtra | "De 206.712 ocupados quedan 76.488 con educación superior, ingreso y horas." |
| Quién queda fuera | Cuenta los excluidos por posición ocupacional | Ver 1.2b |
| Cómo se calculan | Tabla "qué mide / cómo se calcula / cómo se lee" + margen de error | Ver 1.2c y 1.3 |
| Cifras de control | Tabla que debe coincidir con Power BI + traducción a "por cada $ 100" + figura de las 500 repeticiones | "18,5 % al mes y 13,7 % por hora; Power BI da lo mismo." |
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

### 1.2b Quién queda fuera del análisis (dilo antes de que te lo pregunten)

1. **Trabajan pero no reportan ingreso mayor que 0:** 5.435 ocupados (3.983 no lo informaron y 1.452 reportaron 0); 1.535 de ellos tienen educación superior. La mayoría (3.250) son *trabajadores familiares sin remuneración*. **Ejemplo:** una contadora graduada que ayuda en el negocio de su familia sin sueldo.
2. **No trabajan:** la tabla *Ocupados* solo trae a quien trabajó. **Ejemplos:** una tecnóloga recién graduada que está buscando su primer empleo, o una profesional dedicada al cuidado de su hogar.

**Por qué importa:** la brecha compara a mujeres y hombres **que ya tienen trabajo remunerado**. No dice si a las mujeres les cuesta más conseguir empleo; esa sería otra brecha (de desempleo o de participación) que estos datos no incluyen.

### 1.2c Cómo traducir las cifras a palabras simples (para la presentación)

| Si la cifra es… | Se dice así |
|---|---|
| Brecha de 13,7 % por hora | "Por cada $ 100 que recibe por hora un hombre con educación superior, una mujer con el mismo nivel recibe $ 86,30." |
| Brecha de 18,5 % al mes | "Por cada $ 100 al mes de un hombre, una mujer recibe $ 81,50." |
| Diferencia entre 7,4 % y 14,1 % | "6,7 **puntos porcentuales** más" (no "6,7 % más"). |
| Brecha negativa (−3,4 %) | "En ese sector las mujeres reciben 3,4 % **más** por hora." |
| Intervalo de 11,2 % a 16,3 % | "Aunque la muestra fuera otra, la brecha estaría entre 11 % y 16 %; nunca cerca de 0." |
| Intervalo que incluye el 0 | "Con estos datos no se puede afirmar que haya brecha." |

Siempre en tres pasos: **qué mide** (ingreso mensual o por hora), **cómo se mide** (comparando el promedio de hombres y mujeres con el mismo nivel) y **qué significa** (la frase de los $ 100).

**Horas:** los hombres con educación superior trabajan en promedio 43,7 horas a la semana y las mujeres 41,3. Por eso la brecha mensual (18,5 %) es mayor que la brecha por hora (13,7 %): 4,8 puntos de diferencia coinciden con tener menos horas pagadas, pero la mayor parte se mantiene por hora.

### 1.3 El bootstrap (la pregunta técnica más probable)

**En una frase:** "Simulamos repetir la encuesta 500 veces con las mismas viviendas, recalculamos la brecha cada vez y nos quedamos con el rango donde cae el 95 % de los resultados."

**Figura de apoyo en el notebook:** el histograma de las 500 brechas simuladas. Casi todas caen entre 11 % y 16 % y ninguna se acerca a 0. Si te piden explicarlo, abre esa figura.

**Qué es.** Una forma de medir cuánto cambiaría la cifra si se hubiera tomado otra muestra. Se repite el cálculo 500 veces "remuestreando" las viviendas y se mira dónde cae el 95 % de los resultados. Ese rango es el intervalo de confianza (IC).

**Cómo está hecho (función `brecha_con_intervalo`).**
1. Se suman el ingreso×FEX y las horas×FEX **por vivienda y sexo**.
2. Cada vivienda recibe en cada repetición un peso aleatorio de una distribución Poisson con media 1 (0, 1, 2…). Esto equivale a sacar viviendas con reemplazo y es rápido porque se resuelve con una multiplicación de matrices (`pesos @ ingreso`).
3. Con esos pesos se recalcula el ingreso por hora de hombres y mujeres y la brecha. Se toman los percentiles 2,5 y 97,5.

**Por qué por vivienda y no por persona.** Las personas de un mismo hogar se parecen (mismo barrio, mismo estrato). Remuestrear personas sueltas daría intervalos demasiado estrechos.

**Limitación que debes decir tú antes de que te la pregunten.** El DANE usa el diseño completo (estratos y conglomerados), que no viene en las tablas públicas, así que nuestros intervalos son una aproximación y los reales pueden ser algo más amplios.

**CV (coeficiente de variación).** Es la desviación estándar del bootstrap dividida por la estimación, en %. Umbrales del DANE: hasta 7 % precisa, de 7 % a 15 % aceptable, de 15 % a 20 % regular y más de 20 % poco precisa. Todos los departamentos dan CV ≤ 15 % en el ingreso por hora. Lo incierto es la **diferencia**, por eso el mapa usa el IC de la brecha.

### 1.4 El efecto de composición

- **Sin** educación superior las mujeres reciben 11,3 % menos por hora y **con** educación superior 13,7 % menos. Pero **todos juntos**, las mujeres reciben 3,8 % *más*. ¿Contradice la historia? No.
- El 44,1 % de las mujeres ocupadas tiene educación superior, frente al 29,7 % de los hombres, y ese grupo gana mucho más por hora ($ 18.553 las mujeres y $ 21.491 los hombres, frente a $ 7.142 y $ 8.049 sin educación superior). Al mezclar niveles, las mujeres "suben" el promedio por tener más títulos.
- **Ejemplo para decirlo:** "Si en un salón casi todas las mujeres son profesionales y casi todos los hombres no, el promedio de las mujeres sale más alto aunque cada profesional gane menos que su colega hombre."
- Nombre técnico, por si lo preguntan: **paradoja de Simpson**.
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

- **Tipo de gráfico: "pesas" (dumbbell) + barras.** Cada fila es un sector. A la izquierda, un punto azul (hombres) y uno ocre (mujeres) con su ingreso por hora, unidos por una línea: mientras más larga, mayor la diferencia. A la derecha de cada fila, el texto "42,3 % menos" (rojo) o "3,4 % más" (gris). El panel derecho tiene barras apiladas con cuántos ocupados con educación superior hay en el sector, por sexo (tamaño y composición).
- **Por qué cambiamos del gráfico de dispersión a este.** En la dispersión los 18 puntos quedaban amontonados y había que adivinar qué sector era cada uno. Aquí cada sector tiene su nombre escrito, el orden (de mayor a menor brecha) ya cuenta la historia y se ve de inmediato quién gana más.
- **Construcción.** `make_subplots` con dos paneles que comparten el eje de sectores. Por cada grupo de edad hay 6 trazas (línea, hombres, mujeres, texto de brecha, barra de hombres, barra de mujeres). El menú (`updatemenus`) muestra las 6 del grupo elegido, cambia el subtítulo y reordena los sectores (`categoryarray`).
- **Cursor:** ingreso por hora, ingreso mensual promedio, brecha frente a los hombres del sector, % de mujeres en el sector y tamaño de la muestra.
- **Ejes fijos.** No cambian al cambiar de grupo de edad, para que la comparación sea justa.
- **Fuente:** Inter / Segoe UI (tipografía de pantalla) en tamaño 14, para que se lea bien proyectado.
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

## Parte 2. El mapa en R

### 2.1 Qué construimos

`r/Equipo3_Proyecto3_Mapa.Rmd` (se abre en RStudio y se le da **Knit**; tarda cerca de 1 minuto). Produce:

| Archivo | Qué es | Para qué sirve |
|---|---|---|
| `r/Equipo3_Proyecto3_Mapa.html` | El documento completo, con código, salidas y textos | Entregable de R (código comentado y ejecutado) |
| `r/salidas/Equipo3_Proyecto3_Mapa_Brecha_Departamento.png` | Mapa coroplético estático (300 ppp) | Diapositiva del mapa |
| `r/salidas/Equipo3_Proyecto3_Intervalos_Departamento.png` | Brecha de cada departamento con su margen de error | Respaldo; explica por qué hay grises |
| `r/salidas/Equipo3_Proyecto3_Mapa_Interactivo.html` | Mismo mapa en `tmap` (modo `view`) | Consulta: clic en un departamento y aparecen sus cifras |

**Qué se pinta:** la brecha de ingreso por hora en educación superior (todas las edades, enero–julio 2026), por departamento. La cifra **no se calcula en R**: viene del notebook (sección 5) en `datos/procesados/brecha_departamento.csv`. R solo la lleva al mapa.

### 2.2 Los pasos del código y qué debes saber explicar

| Paso | Código | Qué decir |
|---|---|---|
| 1. Rutas | `BASE <- if (dir.exists("../datos")) ".." else "."` | Funciona igual con Knit (que corre desde `r/`) y desde la raíz del repo. No usamos `setwd()`. |
| 2. Leer la cartografía | `st_read(...MGN_MPIO_POLITICO.shp)` | Marco Geoestadístico Nacional del DANE, capa municipal, 1.121 municipios, en WGS84 (EPSG:4326, grados). |
| 3. Reproyectar | `st_transform(crs = 9377)` + `st_make_valid()` | EPSG:9377 = MAGNA-SIRGAS Origen Nacional, la proyección plana oficial de Colombia (metros). `st_make_valid` arregla polígonos mal cerrados antes de unirlos. |
| 4. Municipios → departamentos | `group_by(DPTO_CCDGO) %>% summarise(n_municipios = n())` | `summarise` sobre un objeto `sf` **une las geometrías** y borra los límites internos. Quedan 33 departamentos y verificamos que sumen 1.121 municipios. |
| 5. Simplificar | `st_simplify(dTolerance = 500, preserveTopology = TRUE)` | Quita vértices a menos de 500 m para que el archivo pese poco. `preserveTopology` evita que las islas (San Andrés, Providencia) desaparezcan. |
| 6. Nombres | `tribble(...)` con 33 filas | Los nombres de la capa vienen en mayúsculas y algunos sin tilde ("QUINDIO"). También marca los 9 departamentos con muestra **solo urbana**. |
| 7. Leer la tabla de Python | `read_csv(..., col_types = cols(DPTO = col_character()))` | El código va como **texto** para no perder el 0 de "05" (Antioquia). Como número, la unión fallaría. |
| 8. Unir y verificar | `left_join` + dos `anti_join` + `stopifnot` | Se revisa en los dos sentidos: ningún departamento sin dato y ningún dato sin departamento. Si falla, el documento se detiene. (Criterio de integridad de uniones.) |
| 9. Clasificar | `classIntervals(style = "fixed", fixedBreaks = c(10, 15, 20, 25, 35))` + `cut()` | 4 clases de 5 en 5 puntos; los no concluyentes van aparte en gris. Resultado: 8 / 6 / 5 / 2 departamentos y 12 grises. |
| 10. Colores | `PALETA` | Secuencial de un solo tono (rojo teja de la brecha, `#AD4A3C`), más oscuro = brecha mayor. Gris claro sin tono para "no concluyente". |
| 11. Etiquetas | `st_point_on_surface()` + tabla `posiciones` | Solo 6 etiquetas: las 5 brechas concluyentes más altas y Bogotá como referencia. Las de departamentos pequeños (Caldas, Quindío, Bogotá) van sobre el Pacífico con una línea. `st_point_on_surface` garantiza que el punto caiga **dentro** del departamento (un centroide puede caer fuera en formas irregulares). |
| 12. San Andrés | `ggplotGrob(recuadro)` dentro de `annotation_custom()` | El archipiélago está a unos 700 km de la costa; en su posición real encogería el mapa. Va en un recuadro aparte, a otra escala. |
| 13. Elementos cartográficos | `annotation_scale()`, `annotation_north_arrow()`, `labs(caption = ...)` | Escala (300 km), norte, leyenda, fuente, proyección y método del margen de error. |
| 14. Interactivo | `tmap_mode("view")` + `tm_polygons(popup.vars = ...)` + `tm_basemap(NULL)` | Al hacer clic se ve: brecha, margen de error, "por cada $ 100…", ingreso por hora de cada sexo, muestra y si es solo urbana. Sin mapa de fondo: CARTO ahora pide clave de API y llenaba el mapa de marcas de agua; así además funciona sin internet. |
| 15. Exportar | `ggsave(..., dpi = 300)` y `tmap_save(..., selfcontained = TRUE)` | PNG para la presentación y HTML que se abre con doble clic. |

### 2.3 Decisiones que te van a preguntar

- **¿Por qué departamentos y no municipios?** La GEIH da cifras confiables por departamento si se juntan varios meses; por municipio no. Las 23 ciudades son puntos, no áreas, y ya están en el Power BI.
- **¿Por qué los cortes empiezan en 10 y no en 0?** Ningún departamento con brecha concluyente tiene menos de 11,4 %. Empezar en 0 gastaría dos colores en clases vacías. Los cortes de 5 en 5 son redondos y fáciles de leer, y la clase 10–15 % agrupa a los que están cerca del promedio nacional (13,7 %). Con cuantiles o Jenks saldrían límites como "13,84 % a 16,45 %".
- **¿Por qué gris y no el color de la brecha?** Si el margen de error incluye el 0, no podemos afirmar que haya diferencia. Pintarlo con color de brecha sería mostrar algo que los datos no sostienen (ética, escala no engañosa). **Gris no significa "ganan lo mismo"**: significa "no alcanza la muestra para afirmarlo".
- **¿Por qué secuencial y no divergente?** Todos los concluyentes son positivos (las mujeres reciben menos). Una escala centrada en 0 desperdiciaría la mitad de los colores.
- **¿Qué es el círculo?** En Arauca, Casanare, Putumayo, San Andrés, Amazonas, Guainía, Guaviare, Vaupés y Vichada, **todas** las viviendas encuestadas están en cabeceras municipales (variable `CLASE = 1` en la tabla de Características generales; lo revisamos en los microdatos). La cifra no representa a la población rural, aunque el color cubra todo el departamento.
- **¿Por qué todas las edades y no solo 18–28?** Al cruzar edad y departamento, varias celdas quedan con menos de 30 hombres jóvenes. La diferencia por edad se cuenta con el gráfico de Python.
- **¿El mapa dice que vivir en X causa más brecha?** No. Describe dónde se observa una brecha mayor, no por qué.
- **¿Por qué EPSG:9377?** Es el sistema plano oficial de Colombia, adoptado por el IGAC en 2020. En grados (4326) el país sale levemente estirado y la barra de escala no mediría bien.

### 2.4 Lectura del mapa (cifras verificadas en el HTML)

| Qué | Cifra | En palabras simples |
|---|---|---|
| Guaviare | 28,1 % (IC 15,5 % a 38,7 %) | Por cada $ 100 por hora de un hombre, una mujer recibe cerca de $ 71,90. **Ojo:** muestra pequeña (217 hombres y 319 mujeres) y solo urbana. |
| Casanare | 27,3 % (IC 15,6 % a 38,5 %) | Cerca de $ 72,70 por cada $ 100. Mismo cuidado: solo urbana. |
| Caldas | 24,9 % (IC 19,2 % a 29,9 %) | La brecha alta **más firme**: muestra grande (más de 4.500 personas) e intervalo estrecho. |
| Quindío | 24,1 % (IC 17,0 % a 32,1 %) | Eje Cafetero, también alta. |
| Meta | 20,8 % | Quinta más alta. |
| Bogotá | 13,4 % (IC 8,7 % a 18,6 %) | Casi igual a la nacional (13,7 %): cerca de $ 86,60 por cada $ 100. |
| No concluyentes | 12 departamentos | Varios en el Caribe (Córdoba, Sucre, Magdalena, La Guajira) y el Pacífico (Chocó, Cauca, Nariño), más Cundinamarca, Putumayo, Amazonas, Guainía y Vaupés. |
| Intervalos más anchos | Amazonas, Cundinamarca, Vichada | Más de 34 puntos de punta a punta: la cifra puede cambiar mucho con otra muestra. |
| Intervalos más estrechos | Bogotá, Caldas, Antioquia | Unos 10 a 11 puntos. |

**Frase para la sustentación:** "En 21 de los 33 departamentos podemos afirmar que las mujeres con educación superior reciben menos por hora que los hombres con educación superior. En ninguno se observa lo contrario de forma concluyente. La brecha más alta y firme está en el Eje Cafetero; las de Guaviare y Casanare son altas pero vienen de muestras pequeñas y solo urbanas."

### 2.5 Cómo correrlo

1. R 4.6.2 y RStudio. Paquetes (una sola vez):
   ```r
   install.packages(c("sf", "dplyr", "readr", "ggplot2", "ggspatial", "classInt", "tmap", "rmarkdown", "knitr"))
   ```
2. Abrir `r/Equipo3_Proyecto3_Mapa.Rmd` → **Knit**. No necesita RTools ni `setwd()`.
3. Antes, el notebook de Python debe haber generado `datos/procesados/brecha_departamento.csv` (ya está en el repo).
