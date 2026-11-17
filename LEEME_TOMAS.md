# LEEME TOMÁS: tu parte del Proyecto 3 (Power BI)

> **Entrega: hoy, martes 17-nov-2026, antes de las 11:59 p.m., por correo.** En el P1 nos quitaron 0,5 por entregar tarde.
> **Tu fecha interna: Power BI corregido, publicado y con capturas en el repo a las 7:00 p.m.** Alejandro arma la presentación con esas capturas.

**Si eres una IA ayudando a Tomás**, lee primero este archivo, `docs/Definiciones_compartidas.md` y `docs/instrucciones/Proyecto_3_Narrativa_Visual_Integrada.pdf` (sección 6, fila Power BI, y la rúbrica en 10.1). Respeta estas reglas:
- Todo en **español**.
- Los títulos de los visuales son **neutrales y descriptivos**, no conclusiones.
- No hay lenguaje causal.
- Solo se modifican archivos dentro de `powerbi/` y `presentacion/img/`.
- Las cifras tienen que coincidir con las de control de la sección 3.

---

## 1. Contexto en 30 segundos

- **Proyecto 3 = narrativa ciudadana** que integra Power BI (tú), Python y R (Alejandro). Vale 6 de 50 puntos para Power BI: *"correcciones justificadas; funcionalidad, modelado y DAX pertinentes; integración al mensaje"*.
- **Audiencia:** mujeres de 18 a 28 años que terminan o acaban de terminar un técnico, tecnológico o carrera y van a buscar su primer empleo.
- **Pregunta:** ¿Qué diferencias de ingreso laboral se observan entre mujeres y hombres con educación superior en Colombia (enero–julio 2026) y cómo varían según la edad y el departamento?
- **Gran Idea (borrador):** el título se asocia con más ingresos para las mujeres, pero no con ingresos iguales. Al empezar (18–28 años) reciben por hora cerca de un 7 % menos que los hombres con su mismo nivel, y entre los 29 y 40 años cerca de un 14 % menos.
- **Qué muestra cada herramienta (para no repetir gráficos):**

| Herramienta | Papel en la historia |
|---|---|
| **Power BI (tú)** | Panorama y exploración: KPI, ingreso por nivel educativo y sexo, evolución mensual, cotización a pensión, detalle por ciudad, con filtros. |
| Python (Seaborn) | Distribución de ingresos, no solo promedios, y la brecha por grupo de edad. |
| Python (Plotly) | Dos interactivos por sector económico: panorama (dispersión) y brecha por sector según la edad. |
| R | Mapa de la brecha por departamento. |

  → Por eso **quita el gráfico de barras "Ciudades donde la brecha es más urgente"**: lo territorial va en el mapa de R. La matriz ciudad × nivel educativo sí se queda como detalle.

## 2. Tareas (en orden de prioridad)

Archivo de trabajo: `powerbi/Equipo3_Proyecto3_Dashboard.pbix`, que es una copia del P1. El original queda intacto en la carpeta del P1.

### A. Correcciones que pidió la docente en el P1 (obligatorias)
- [ ] **Títulos neutrales y descriptivos** en todos los visuales. Cambios:
  - "A mayor educación, mayor brecha de ingresos" → "Ingreso laboral mensual promedio por nivel educativo y sexo".
  - "La brecha no cierra entre enero y julio" → "Brecha de ingreso mensual por mes, enero–julio 2026".
  - "La brecha cae con la educación, pero persiste en superior" → "Brecha de ingreso mensual por nivel educativo".
  - "Aun pagando por hora, la brecha casi no cambia" → "Brecha de ingreso mensual y por hora según nivel educativo".
  - "En superior, las mujeres cotizan igual que los hombres" → "Porcentaje de ocupados que cotiza a pensión, por sexo y nivel educativo".
  - Además, los títulos "A mayor educación, mayor brecha" y "La brecha cae con la educación" **se contradecían**. En porcentaje, la brecha baja con la educación (de ~35 % a ~18 %).
- [ ] **Página "Causas y Detalle" → renombrar a "Detalle"** (o "Detalle por nivel y ciudad"). "Causas" sugiere causalidad y la guía lo prohíbe.
- [ ] **Formato de porcentajes:** las medidas de brecha y `%_Cotiza` no tienen formato (FormatString vacío). Ponles **Porcentaje con 1 decimal** (Herramientas de medición → Formato → Porcentaje, 1 decimal). Deben mostrarse como "18,5 %".
- [ ] **Segmentadores con lista desplegable** para Ciudad y Nivel educativo (Formato del visual → Configuración del segmentador → Estilo: **Lista desplegable**), en ambas páginas. Revisa el segundo segmentador de la página 2: se llama "Nivel educativo" pero filtra **Ciudad**.
- [ ] **Documentar la fórmula de informalidad:** en la página de detalle, agrega un cuadro de texto que diga:
  > "% que cotiza a pensión = ocupados con P6920 = 1 (cotiza) / ocupados con P6920 ∈ {1, 2, 3}, ponderado por FEX_C18. Es una aproximación a la protección social, no la medición oficial de informalidad del DANE."

### B. Correcciones de las medidas DAX (para que coincidan con Python y R)
- [ ] **Corregir `Ingreso_Hora_Promedio`**: le faltan los filtros de ingreso y horas positivos.
  ```dax
  Ingreso_Hora_Promedio =
  CALCULATE(
      DIVIDE(
          SUMX(Fact_Ocupados, Fact_Ocupados[Ingreso_Laboral] * Fact_Ocupados[Factor_Expansion]),
          SUMX(Fact_Ocupados, Fact_Ocupados[Horas_Semanales] * 4.3333 * Fact_Ocupados[Factor_Expansion])
      ),
      Fact_Ocupados[Ingreso_Laboral] > 0,
      Fact_Ocupados[Horas_Semanales] > 0
  )
  ```
- [ ] **Nueva medida** para la tarjeta de brecha por hora en educación superior:
  ```dax
  Brecha_Hora_EducSuperior =
  CALCULATE([Brecha_Hora], Dim_Educacion[Categoria] = "Superior")
  ```
- [ ] **Verificar qué incluye la categoría "Superior".** Debe ser P3042 = 8 a 13 (técnica profesional → doctorado), **sin** normalista (7). Corre esto en la vista de consultas DAX:
  ```dax
  EVALUATE
  SUMMARIZECOLUMNS(
      Dim_Educacion[Nivel], Dim_Educacion[Categoria],
      "Registros", COUNTROWS(Fact_Ocupados)
  )
  ```
- [ ] **Nueva columna Grupo de edad** + segmentador desplegable "Grupo de edad". Es clave para la audiencia. En la tabla donde esté la edad (P6040):
  ```dax
  Grupo_Edad =
  SWITCH(TRUE(),
      [Edad] < 18, "Menor de 18",
      [Edad] <= 28, "18–28",
      [Edad] <= 40, "29–40",
      [Edad] <= 59, "41–59",
      "60 y más")
  ```
  Si la edad no está en `Fact_Ocupados`, tráela en Power Query con la misma llave (DIRECTORIO + SECUENCIA_P + HOGAR + ORDEN + PERIODO).

### C. Diseño y accesibilidad
- [ ] **Colores** (Ver → Temas → Personalizar el tema actual, o edita el JSON del tema):

  | Uso | Color |
  |---|---|
  | Hombre | `#1F4E79` |
  | Mujer | `#B8862B` |
  | Brecha / acento | `#AD4A3C` |
  | Neutro | `#6B7280` |

  El azul `#1F5FA8` y el morado `#7B3FA0` actuales tienen un contraste de 1,1:1 entre sí: **no se distinguen con daltonismo**. Es una mejora justificada que debes mencionar en la sustentación. Asigna los colores **por categoría** (Hombre siempre azul, Mujer siempre ocre) en todos los visuales.
- [ ] **Etiquetas de datos** en las barras principales, para no depender solo del color.
- [ ] En cada página, un **cuadro de texto pequeño "Cómo leer esta página"** en lenguaje ciudadano y el pie: "Fuente: DANE, GEIH enero–julio 2026. Cálculos del Equipo 3. Promedios ponderados con el factor de expansión. Comparaciones descriptivas, no causales."
- [ ] Tooltips con lenguaje simple ("Ingreso mensual promedio", no "Ingreso_Promedio").

### D. Publicación y capturas (antes de las 7:00 p.m.)
- [ ] **Publicar** en Power BI Service, reemplazando el informe del enlace actual o creando uno nuevo.
- [ ] Comprobar que **la docente puede abrir el enlace**: Compartir → "Personas de su organización" si ella está en el mismo dominio de la universidad, o "Personas específicas" con su correo. Pruébalo en una ventana de incógnito. Pega el enlace final en la sección 5 de este archivo.
- [ ] **Exportar capturas PNG** de cada página (sin filtros aplicados) a:
  - `presentacion/img/powerbi_pagina1.png`
  - `presentacion/img/powerbi_pagina2.png`
- [ ] Guardar el `.pbix` y subirlo al repo (sección 4).

## 3. Cifras de control (deben coincidir con Power BI)

Corre esta consulta en la vista de consultas DAX **después** de las correcciones:
```dax
EVALUATE
ROW(
    "Brecha_mensual_superior", [Brecha_EducSuperior],
    "Brecha_hora_superior",    [Brecha_Hora_EducSuperior],
    "Ingreso_H_superior",      [Ingreso_Hombres_Superior],
    "Ingreso_M_superior",      [Ingreso_Mujeres_Superior]
)
```

| Medida | Valor esperado (Python) |
|---|---|
| Brecha_mensual_superior | ≈ 18,5 % |
| Brecha_hora_superior | ≈ 13,7 % |
| Ingreso_H_superior | ≈ $ 4.068.584 |
| Ingreso_M_superior | ≈ $ 3.317.843 |

Si no coinciden, lo más probable es que la categoría "Superior" incluya otro rango de P3042 o que falte el filtro `Ingreso_Laboral > 0`. Avísale a Alejandro con el resultado.

## 4. Cómo trabajar con el repo

1. Acepta la invitación de colaborador que te llega a GitHub o al correo.
2. Clona el repo y trabaja siempre sobre lo último:
   ```bash
   git clone https://github.com/AlejandroP212/proyecto3-narrativa-visual.git
   cd proyecto3-narrativa-visual
   git pull                       # siempre antes de empezar
   ```
3. Sube tus cambios:
   ```bash
   git add powerbi/ presentacion/img/ LEEME_TOMAS.md
   git commit -m "Power BI: títulos neutrales, formato %, medidas por hora y grupo de edad"
   git push
   ```

- **Solo tú modificas `powerbi/`.** El `.pbix` es binario y no se puede fusionar, así que Alejandro no lo toca.
- Si `git push` falla porque hay cambios nuevos, primero haz `git pull` y luego vuelve a hacer `git push`.

## 5. Para completar (Tomás)

- Enlace final de Power BI Service: `https://app.powerbi.com/links/N7NaGvljjq?ctid=3b944d9a-1051-4685-b09d-9a95ee2dbd99&pbi_source=linkShare` ← actualizar si cambia
- ¿Permisos probados en incógnito o por la docente? ☐
- Resultado de la consulta de control (sección 3): …
- Herramientas de IA que usaste y para qué (para el anexo de IA, máximo 1 página): …

## 6. Para la sustentación (todos responden de todo)

La docente puede preguntarle **a cualquiera** por Power BI, Python o R. Antes de la sustentación lee:
- `docs/Guia_apoyo_Proyecto3.md`: qué se hizo, qué no y por qué.
- Las celdas de interpretación del notebook `python/Equipo3_Proyecto3_Analisis.ipynb`.
- El mapa en R, `r/Equipo3_Proyecto3_Mapa.Rmd`: unidad territorial, cortes de la leyenda y advertencia de precisión.

Y prepárate para explicar tus propias decisiones: por qué cambiaste los colores, qué mide cada medida DAX, qué es FEX_C18 y por qué la brecha total (8,6 %) es menor que la de cada nivel educativo (efecto de composición).
