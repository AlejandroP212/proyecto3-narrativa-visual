# Guion de la sustentación · Proyecto 3 · Equipo 3

Documento de apoyo para los dos integrantes. **No se entrega.** La presentación es `presentacion/Equipo3_Proyecto3_Presentacion.html`. En pantalla: flechas para avanzar, **N** para ver las notas de cada diapositiva, **F** para pantalla completa y **G** para la vista general.

## Reglas de la sustentación (sección 8 de la guía)

- **Máximo 10 minutos** y luego preguntas de las docentes y de los compañeros.
- **Hablan los dos.** Una ausencia sin justificación afecta la nota individual.
- **No es una demostración de software.** No se explica código, DAX ni por qué se eligió un color. Se habla como comunicadores de datos ante la audiencia ciudadana.
- Aun así, **cada uno debe poder responder sobre Power BI, Python y R**, y abrir o ejecutar un componente si la docente lo pide.

## Reparto y tiempos

| # | Diapositiva | Quién | Tiempo | Bloque de la guía |
|---|---|---|---|---|
| 1 | Portada: ¿Mismo título, mismo ingreso? | Tomás | 0:30 | Problemática, audiencia y pregunta (1 min) |
| 2 | Para quién es esta historia | Tomás | 0:45 | |
| 3 | La Gran Idea | Tomás | 1:00 | Contexto, fuente y Gran Idea (2 min) |
| 4 | Panorama (Power BI) | Tomás | 1:00 | |
| 5 | Distribución (Seaborn) | Alejandro | 1:15 | Desarrollo e interacción (5 min) |
| 6 | Edad (Seaborn) | Alejandro | 1:15 | |
| 7 | Sector (Plotly) | Alejandro | 1:15 | |
| 8 | Territorio (mapa en R) | Alejandro | 1:15 | |
| 9 | Síntesis y mensaje final | Tomás | 1:00 | Síntesis, limitaciones y mensaje (2 min) |
| 10 | Fuentes y limitaciones | Alejandro | 0:45 | |
| | **Total** | | **10:00** | |

Si el tiempo aprieta, recorta de las diapositivas 5 y 8. **Nunca recortes la 6 ni la 9:** ahí están la respuesta para la audiencia y el mensaje final.

## Antes de empezar (5 minutos antes)

1. Abrir en el navegador, cada uno en una pestaña:
   - la presentación;
   - `python/html/Equipo3_Proyecto3_Plotly_Sectores_por_Edad.html`;
   - `python/html/Equipo3_Proyecto3_Plotly_Panorama_Sectores.html`;
   - `r/salidas/Equipo3_Proyecto3_Mapa_Interactivo.html`;
   - el tablero en Power BI Service.
2. Probar el enlace de Power BI en una ventana de incógnito. Si pide iniciar sesión con la cuenta de la universidad, tener abierto el `.pbix` en Power BI Desktop como respaldo.
3. Tener abiertos el notebook en VS Code y el `.Rmd` en RStudio, por si piden ejecutar algo.
4. Revisar que la diapositiva 4 muestre la captura del tablero y no el recuadro "Captura pendiente".

---

## Diapositiva por diapositiva

Las frases son una guía, no para leerlas. Lo importante son las **cifras en negrita** y las **transiciones**.

### 1. Portada (Tomás, 0:30)
- "Somos el Equipo 3. Esta presentación es para una persona concreta: una mujer de 18 a 28 años que está terminando una carrera y va a buscar su primer empleo."
- "Su pregunta es simple: si tengo el mismo título que un hombre, ¿voy a recibir lo mismo?"
- Señalar la barra: "Por cada **$ 100** que recibe por hora un hombre con educación superior, una mujer con educación superior recibe **$ 86,30**."
- **Transición:** "Veamos por qué elegimos esta pregunta y cómo la medimos."

### 2. Para quién es esta historia (Tomás, 0:45)
- Audiencia y por qué le importa: con esta información puede llegar mejor preparada a una entrevista o a una negociación salarial.
- Fuente: "Usamos la **GEIH del DANE, de enero a julio de 2026**: **76.488** personas ocupadas con educación superior."
- Por qué **por hora**: "Los hombres trabajan **43,7** horas a la semana y las mujeres **41,3**. Si solo comparamos el salario del mes, parte de la diferencia sería por horas. Por hora comparamos lo que se paga por el mismo tiempo de trabajo."
- **Transición:** "Con eso, esta es nuestra Gran Idea."

### 3. La Gran Idea (Tomás, 1:00)
- Leer la Gran Idea despacio, solo la frase en negrita y la primera oración, y luego explicar las cuatro tarjetas:
  - **13,7 %** por hora, con margen de error de 11,2 % a 16,3 %: "aunque repitiéramos la encuesta, la brecha seguiría entre esos valores".
  - **18,5 %** al mes: $ 4,07 millones frente a $ 3,32 millones.
  - **7,4 % → 14,1 %**: las jóvenes y el grupo de 29 a 40 años.
  - **21 de 33** departamentos con brecha concluyente.
- Señalar las tres tarjetas de abajo: "Cada herramienta responde una parte de la pregunta, sin repetir gráficos."
- **Transición:** "Empecemos por el panorama general en Power BI."

### 4. Panorama, Power BI (Tomás, 1:00)
- "Si miramos a **todas** las personas ocupadas, la brecha mensual es de **8,6 %**. Si miramos solo a quienes tienen **educación superior**, sube a **18,5 %**."
- **El punto clave:** "¿Por qué el promedio general esconde la brecha? Entre las mujeres ocupadas, el **44,1 %** tiene educación superior; entre los hombres, el **29,7 %**. Al mezclar todos los niveles, ellas suben el promedio porque estudiaron más. Por eso toda la historia compara personas con el mismo nivel educativo."
- Si hay tiempo, mostrar en el tablero el **filtro de nivel educativo** y la evolución por mes.
- **Transición:** "Alejandro les va a mostrar si esa diferencia está en todos los ingresos o solo en unos pocos."

### 5. Distribución, Seaborn (Alejandro, 1:15)
- "Un promedio puede esconder que la diferencia está solo en unos pocos sueldos muy altos. Este gráfico muestra cómo se reparten los ingresos de todas las personas."
- Cómo se lee: "Cada curva es un sexo. Donde la curva es más alta hay más personas con ese ingreso. La línea punteada es la mediana: la mitad gana menos que ese valor."
- Lo que se ve: "En los tres niveles la curva ocre está corrida a la izquierda." Ejemplo: "Con posgrado, la mitad de las mujeres recibe menos de **$ 28.846** por hora; la mitad de los hombres, menos de **$ 34.154**."
- **Transición:** "Ahora, lo que más le importa a nuestra audiencia: ¿qué pasa al comenzar?"

### 6. Edad, Seaborn (Alejandro, 1:15)
- "Entre los **18 y 28** años la brecha es de **7,4 %**: por cada $ 100 de un joven, una joven recibe **$ 92,60**. En el grupo de **29 a 40** es de **14,1 %**: **$ 85,90**."
- Margen de error: "La diferencia entre los dos grupos, **6,7 puntos**, es mayor que su margen de error, que va de 1,0 a 12,3 puntos. No es un accidente de la muestra."
- **Cuidado (decirlo sí o sí):** "Esto compara personas distintas de cada edad en 2026. No sigue a las mismas mujeres en el tiempo, así que no podemos decir que a una joven le vaya a pasar esto. Lo que sí podemos decir es que hoy la brecha es mayor en el grupo de 29 a 40."
- **Transición:** "¿Y depende de dónde trabaje? Primero, el sector."

### 7. Sector, Plotly (Alejandro, 1:15) — **mostrar el interactivo**
- Abrir el HTML **Brecha por sector y edad** y elegir **18–28** en el menú.
- "Cada fila es un sector: azul hombres, ocre mujeres. Están ordenados de mayor a menor brecha y la línea punteada separa los sectores donde ellas reciben menos de aquellos donde reciben igual o más."
- "Entre los 18 y 28 años, en **12 de 17** sectores las jóvenes reciben menos. Las brechas más altas están en **comercio (20,0 %)**, **servicios administrativos (18,5 %)** y **educación (16,6 %)**."
- Cambiar a **Todas las edades**: "**Salud** pasa al primer lugar con **42,3 %**, y allí el **76 %** de las personas con educación superior son mujeres."
- Pasar el cursor por una fila para mostrar el detalle.
- **Transición:** "Y el último ángulo: el territorio."

### 8. Territorio, mapa en R (Alejandro, 1:15) — **mostrar el interactivo si hay tiempo**
- "Cada departamento tiene el color de su brecha por hora; más oscuro, brecha más grande. Usamos departamentos porque la GEIH no da cifras confiables por municipio."
- "En **21 de 33** departamentos la brecha es concluyente. La más alta y más firme está en el **Eje Cafetero**: **Caldas 24,9 %**, es decir **$ 75,10** por cada $ 100."
- "Guaviare y Casanare tienen cifras más altas, pero el círculo avisa que allí la encuesta solo cubre zonas urbanas y la muestra es pequeña."
- "**Bogotá: 13,4 %**, casi igual al país."
- **Los grises:** "No son lugares sin brecha. Son lugares donde la muestra no alcanza para afirmarla."
- **Transición:** "Tomás cierra con lo que esto significa para nuestra audiencia."

### 9. Síntesis y mensaje final (Tomás, 1:00)
- Respuesta a la pregunta, en una frase: "Con el mismo nivel educativo, las mujeres reciben menos por hora en casi todos los grupos que miramos. La diferencia es menor al empezar, es mayor de los 29 a los 40 y cambia mucho de un sector y de un departamento a otro."
- **Mensaje para la audiencia:**
  1. compara por hora, no solo el salario mensual;
  2. averigua cuánto paga el cargo en tu sector y tu región antes de aceptar una oferta;
  3. usa los interactivos para ver tu caso.
- **Lo que no decimos:** "Estos datos no prueban discriminación ni explican las causas: no tienen en cuenta el cargo, la carrera ni la experiencia."

### 10. Fuentes y limitaciones (Alejandro, 0:45)
- "Las fuentes son la GEIH y el Marco Geoestadístico del DANE. Todo está en el repositorio, con los pasos para reproducirlo."
- Las tres limitaciones que más importan:
  1. "Solo comparamos a personas con trabajo remunerado: una recién graduada que busca empleo no aparece."
  2. "La edad compara personas distintas, no la trayectoria de una persona."
  3. "En nueve departamentos la muestra es solo urbana."
- "Gracias. Quedamos atentos a sus preguntas."

---

## Preguntas probables y respuestas cortas

| Pregunta | Quién responde | Respuesta corta |
|---|---|---|
| ¿Por qué solo educación superior? | Cualquiera | Porque es la audiencia. Además, al mezclar niveles el promedio esconde la brecha: ellas tienen más educación superior (44,1 % frente a 29,7 %). |
| ¿Por qué por hora y no por mes? | Cualquiera | Ellas trabajan 2,4 horas menos a la semana. Por hora comparamos lo que se paga por el mismo tiempo. Al mes la brecha es mayor (18,5 %). |
| ¿Qué es el margen de error? | Alejandro | Repetimos el cálculo 500 veces sacando viviendas al azar (bootstrap). El 95 % de los resultados cae en ese rango. Si incluye el 0, no podemos afirmar que haya brecha. |
| ¿Por qué por vivienda? | Alejandro | La GEIH encuesta viviendas completas y las personas de una misma vivienda se parecen entre sí. Remuestrear personas sueltas daría márgenes demasiado estrechos. |
| ¿Esto prueba discriminación? | Cualquiera | No. Es descriptivo: no controla cargo, carrera, experiencia ni empresa. |
| ¿Por qué el total por hora da −3,8 %? | Alejandro | Efecto de composición (paradoja de Simpson). Dentro de cada nivel ellas reciben menos, pero como hay más mujeres con educación superior, al mezclar todo el promedio de ellas sube. |
| ¿Por qué no mapa por municipio? | Alejandro | La GEIH no es representativa por municipio. Por departamento, juntando 7 meses, sí hay muestra (y aun así 12 no son concluyentes). |
| ¿Por qué el mapa empieza en 10 %? | Alejandro | Ningún departamento concluyente tiene menos de 11,4 %. Empezar en 0 dejaba dos colores sin uso. |
| ¿Qué cambió en Power BI desde el P1? | Tomás | Títulos neutrales, porcentajes con formato, segmentadores desplegables, página "Detalle" (antes "Causas"), fórmula de cotización documentada, ingreso por hora corregido con filtros de valores positivos y medida de brecha por hora en educación superior. |
| ¿Cómo se calcula la brecha en DAX? | Tomás | (Ingreso hombres − ingreso mujeres) / ingreso hombres, ponderado con el factor de expansión. Por hora: suma de ingresos / suma de horas × 4,33. |
| ¿Las cifras de Power BI y Python coinciden? | Cualquiera | Sí: 18,5 % mensual y 13,7 % por hora en educación superior, con las mismas definiciones (`docs/Definiciones_compartidas.md`). |
| ¿Por qué dos gráficos de Plotly? | Alejandro | Responden preguntas distintas: el panorama muestra nivel de pago, tamaño y brecha de cada sector a la vez; el ranking compara brechas y cómo cambia el orden con la edad. |
| ¿Usaron IA? | Cualquiera | Sí, está declarado en el anexo: herramientas, propósito, prompts y qué corregimos. |

Para más detalle técnico, ver `docs/Guia_apoyo_Proyecto3.md`.
