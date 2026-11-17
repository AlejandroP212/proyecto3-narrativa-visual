# Definiciones compartidas (Power BI · Python · R)

> **Regla del equipo:** las tres herramientas usan **exactamente** estas definiciones. Si una cifra cambia entre Power BI, el notebook y el mapa, hay un error. Cualquier cambio se anota aquí primero.

## 1. Audiencia, pregunta y La Gran Idea (propuesta 1 elegida)

| Elemento | Definición |
|---|---|
| **Audiencia ciudadana** | Mujeres de 18 a 28 años que están terminando o acaban de terminar un programa técnico, tecnológico o universitario y van a buscar su primer empleo o a negociar su primer salario. |
| **Necesidad de comprensión** | Saber qué diferencias de ingreso existen, frente a los hombres con el mismo nivel educativo, en el mercado laboral al que entran, y cómo esas diferencias cambian con la edad y el territorio, para hacer preguntas informadas (por ejemplo, al negociar un salario). |
| **Pregunta analítica** | ¿Qué diferencias de ingreso laboral se observan entre mujeres y hombres con educación superior en Colombia (enero–julio de 2026) y cómo varían según la edad y el departamento? |
| **La Gran Idea (borrador, cifras por verificar en el notebook)** | Un título de educación superior se asocia con mayores ingresos para las mujeres, pero no con ingresos iguales: al comenzar su vida laboral (18–28 años), las mujeres con educación superior reciben por hora cerca de un 7 % menos que los hombres con su mismo nivel, y entre profesionales de 29 a 40 años esa diferencia es de cerca del 14 %. La brecha también cambia de un departamento a otro. |

Continuidad con el Proyecto 1: es la misma pregunta (ingresos por sexo y nivel educativo), **delimitada** a la educación superior y ampliada con edad y departamento para la nueva audiencia.

## 2. Datos

| Concepto | Definición |
|---|---|
| Fuente | DANE, Gran Encuesta Integrada de Hogares (GEIH) 2026, marco 2018. Tablas *Características generales…* y *Ocupados*, enero a julio de 2026 (`datos/originales/geih_2026/Tablas_Seleccionadas_GEIH_2026.zip`, las mismas del Proyecto 1). Catálogo: https://microdatos.dane.gov.co/index.php/catalog/900 |
| Periodo | Enero–julio de 2026 acumulado (7 meses). Se dice siempre "enero–julio de 2026". |
| Llave de unión | `DIRECTORIO + SECUENCIA_P + HOGAR + ORDEN + PERIODO` (unión 1:1 Ocupados → Características). |
| Factor de expansión | `FEX_C18` (decimal con **punto**). Toda cifra poblacional se pondera con él. |
| Población de análisis | Personas **ocupadas** con `INGLABO > 0`. Para el ingreso por hora, además `P6800 > 0`. |
| Sexo | `P3271`: 1 = Hombre, 2 = Mujer. |
| Educación superior | `P3042` ∈ {8, 9, 10, 11, 12, 13}: técnica profesional, tecnológica, universitaria, especialización, maestría y doctorado. **No** incluye normalista (7). |
| Niveles dentro de superior | Técnica/tecnológica (8–9) · Universitaria (10) · Posgrado (11–13). |
| Grupos de edad (`P6040`) | 18–28 (jóvenes, Ley 1622 de 2013) · 29–40 · 41–59 · 60 y más. |
| Departamento | `DPTO` (32 departamentos + Bogotá D. C.). |

## 3. Indicadores

| Indicador | Fórmula | Notas |
|---|---|---|
| Ingreso laboral mensual promedio | Σ(INGLABO·FEX) / Σ(FEX), con INGLABO > 0 | Igual a la medida `Ingreso_Promedio` de Power BI. |
| Ingreso por hora | Σ(INGLABO·FEX) / Σ(P6800·4,3333·FEX), con INGLABO > 0 **y** P6800 > 0 | Se lee: "por cada hora trabajada". En Power BI, a `Ingreso_Hora_Promedio` **le faltan estos dos filtros**. |
| Brecha (%) | (Hombres − Mujeres) / Hombres × 100 | Positiva = las mujeres reciben menos. Se presenta con **1 decimal y el signo %** (ej. 13,7 %). |
| % que cotiza a pensión | Σ FEX con P6920 = 1 / Σ FEX de ocupados con P6920 ∈ {1, 2, 3} | Es una **aproximación** a la protección social, **no** la medición oficial de informalidad del DANE. |
| Precisión territorial | Coeficiente de variación (CV) de la brecha por departamento, por bootstrap de viviendas (`DIRECTORIO`) | Umbrales DANE: ≤ 7 % precisa · 7–15 % aceptable · 15–20 % regular (usar con precaución) · > 20 % poco precisa (se marca en el mapa). |

Cifras de control (verificadas el 17-nov-2026 con esta definición; el notebook es la fuente oficial):

| Grupo (educación superior) | Brecha mensual | Brecha por hora |
|---|---|---|
| Todas las edades | 18,5 % | 13,7 % |
| 18–28 años | 10,2 % | 7,4 % |
| 29–40 años | 19,0 % | 14,1 % |
| 41–59 años | 17,3 % | 10,5 % |
| 60 y más | 24,5 % | 18,3 % |

Ojo para la narrativa: en el **total de ocupados** (todos los niveles) la brecha mensual es solo de 8,6 % y la de por hora es negativa (−3,8 %). Esto ocurre porque entre las mujeres ocupadas hay más personas con educación superior que entre los hombres (efecto de composición). Por eso se compara **a igual nivel educativo**.

## 4. Estilo común

| Elemento | Valor |
|---|---|
| Hombre | `#1F4E79` (azul, paleta del curso) |
| Mujer | `#B8862B` (ocre; contraste 3,2:1 sobre blanco y distinguible con daltonismo) |
| Brecha / acento | `#AD4A3C` |
| Neutro / texto secundario | `#6B7280` |
| Fondo | blanco `#FFFFFF` |

La pareja anterior del Proyecto 1 (`#1F5FA8` / `#7B3FA0`) tiene un contraste de 1,1:1 entre sí y es casi indistinguible con deuteranopía. Se cambia por accesibilidad.

- **Títulos de los gráficos: neutrales y descriptivos** (retroalimentación del P1), por ejemplo "Brecha de ingreso por hora según grupo de edad, educación superior, enero–julio 2026". El hallazgo va en el subtítulo, en una anotación o en el titular de la diapositiva, redactado como algo observado ("se observa…").
- Lenguaje: "se observa", "se asocia", "es mayor/menor". **Nunca** "causa", "debido a", "provoca" ni "por culpa de".
- Porcentajes con 1 decimal y coma decimal en el texto (13,7 %). Pesos con punto de miles ($ 2.459.340).
- Fuente en cada gráfico: "Fuente: DANE, GEIH enero–julio 2026. Cálculos del Equipo 3."

## 5. Limitaciones que deben aparecer

1. Son comparaciones **descriptivas**: no explican por qué existe la brecha ni miden discriminación (no se controla por profesión, cargo, experiencia ni empresa).
2. Son datos **transversales**: la diferencia entre grupos de edad no muestra cómo cambia la brecha a lo largo de la vida de una misma persona.
3. INGLABO es ingreso **declarado**; se excluyen las personas con ingreso 0 o sin dato.
4. La representatividad departamental de la GEIH es **anual**; con 7 meses, las cifras departamentales se marcan según su CV.
5. Cifras de enero–julio de 2026; no son el promedio anual.
