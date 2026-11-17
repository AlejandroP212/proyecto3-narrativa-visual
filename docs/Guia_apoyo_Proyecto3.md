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
