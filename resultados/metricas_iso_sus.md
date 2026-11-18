# Consolidación de Métricas de Usabilidad (ISO 9241-11:2018 y SUS) · APE 6
## Caso **CaféU** · Grupo 5 · Interacción Humano-Computador (IHC)

- **Responsable del cálculo y tabulación:** Carlos Giovanni Ramos Jácome ([@carlitosgiovanniramos](https://github.com/carlitosgiovanniramos)), Tester
- **Revisión cruzada:** Henry Daniel Lagua Flores ([@Hlagua](https://github.com/Hlagua)), QA / Arquitecto
- **Fuentes primarias:** [`resultados/P1.md`](P1.md), [`resultados/P2.md`](P2.md) y [`resultados/P3.md`](P3.md).

---

## 1. Métrica de Eficacia (ISO 9241-11:2018)

La **eficacia** mide la exactitud e integridad con la que los usuarios alcanzan los objetivos especificados:

| Tarea Evaluada | P1 (Éxito / Err. Crít. / No Crít.) | P2 (Éxito / Err. Crít. / No Crít.) | P3 (Éxito / Err. Crít. / No Crít.) | Tasa de Éxito Autónomo (%) | Total Errores Críticos | Total Errores No Críticos |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **T1:** Confirmar pedido `#A24` y verificar datos clave | Sí (`0` / `0`) | Sí (`0` / `0`) | Sí (`0` / `0`) | **100.0 % (3/3)** | **0** | **0** |
| **T2:** Cancelar pedido, verificar reembolso y re-confirmar | Sí (`0` / `1`) | Sí (`0` / `0`) | Sí (`0` / `1`) | **100.0 % (3/3)** | **0** | **2** |
| **T3 (Refuerzo):** Buscador, filtro y ajuste ante límite de saldo (`$10.00`) | Sí (`0` / `2`) | **No** (`1` / `2`) | Sí (`0` / `2`) | **66.7 % (2/3)** | **1** | **6** |
| **Consolidado Global** | **100.0 %** (`0` / `3`) | **66.7 %** (`1` / `2`) | **100.0 %** (`0` / `3`) | **88.9 % (8/9)** | **1** | **8** |

**Análisis de Eficacia:**
- En las tareas de flujo directo heredadas del pilotaje (`T1` y `T2`), la tasa de éxito autónomo es del **100.0 %** con **0 errores críticos**.
- Al introducir la **Tarea de Refuerzo Post-Pilotaje (`T3`)**, la tasa de éxito autónomo cae al **66.7 % (2/3)** y concentra **1 error crítico** (`P2`) y **6 errores no críticos**, provocados directamente por los hallazgos `H-01` (botón de pago activo con saldo insuficiente), `H-02` (buscador en blanco sin mensaje de «0 resultados») y `H-04` (ausencia de botón para quitar ítems dentro de la lista del pedido).

---

## 2. Métrica de Eficiencia (ISO 9241-11:2018)

La **eficiencia** relaciona los recursos temporales invertidos con los resultados logrados, evaluando la **mediana de tiempo (en segundos)** por tarea frente a la meta definida en el protocolo:

| Tarea Evaluada | Meta Definida (s) | P1 (s) | P2 (s) | P3 (s) | Media (s) | Mediana (s) | Diferencia (Mediana − Meta) | Evaluación frente a la Meta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **T1:** Confirmar pedido `#A24` | **20.0 s** | 16.0 | 14.0 | 18.0 | 16.0 s | **16.0 s** | **−4.0 s (−20.0 %)** | ✅ **Cumple con holgura** |
| **T2:** Cancelar y verificar reembolso | **15.0 s** | 17.0 | 13.0 | 19.0 | 16.3 s | **17.0 s** | **+2.0 s (+13.3 %)** | ⚠️ **Desviación leve** (duda por falta de confirmación `H-03` y cambio `#A24` → `#A25`) |
| **T3 (Refuerzo):** Buscador y límite `$10.00` | **35.0 s** | 52.0 | 64.0* | 48.0 | 54.7 s | **52.0 s** | **+17.0 s (+48.6 %)** | ❌ **No cumple la meta** (demora por lista vacía `H-02`, clic fallido `H-01` y retorno al catálogo `H-04`) |

> **\* Nota sobre `P2` en `T3` (`64.0* s`):** El participante `P2` no completó la tarea `T3` de forma autónoma; el tiempo de `64.0 s` incluye el bloqueo ante el buscador en blanco (`H-02`) y el error de saldo (`H-01`), tras lo cual requirió 1 pista de la moderadora para localizar cómo restar unidades en el catálogo.

---

## 3. Métrica de Satisfacción — Puntaje SUS (Brooke, 1996)

| Participante | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | Suma Base (0–40) | Puntaje SUS ($\times 2.5$) | Referencia Industria | Diferencia vs. 68.0 | Clasificación (Bangor et al., 2009) |
| :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :---: | :---: | :---: | :---: | :--- |
| **P1** | 4 | 2 | 4 | 1 | 4 | 2 | 4 | 2 | 5 | 2 | 32 | **80.0** | 68.0 | **+12.0** | Buena / Excelente (Grado B+) |
| **P2** | 3 | 3 | 3 | 2 | 3 | 2 | 4 | 3 | 4 | 2 | 25 | **62.5** | 68.0 | **−5.5** | **Marginal / Bajo el promedio (Grado D)** |
| **P3** | 4 | 2 | 4 | 2 | 4 | 2 | 4 | 2 | 4 | 2 | 30 | **75.0** | 68.0 | **+7.0** | Buena (Grado B) |
| **Promedio Grupal** | **3.67** | **2.33** | **3.67** | **1.67** | **3.67** | **2.00** | **4.00** | **2.33** | **4.33** | **2.00** | **29.0** | **72.5** | **68.0** | **+4.5** | **Aceptable / Buena (Grado C+/B−)** |
| **Mediana Grupal** | 4 | 2 | 4 | 2 | 4 | 2 | 4 | 2 | 4 | 2 | 30 | **75.0** | **68.0** | **+7.0** | **Buena (Grado B)** |

**Interpretación del Puntaje SUS:**
- El promedio global (**72.5**) y la mediana (**75.0**) superan la referencia de la industria (**68.0**), impulsados por la alta seguridad percibida en el cobro único (Ítem 9, media `4.33/5`) y la facilidad de aprendizaje inicial (Ítem 7, media `4.00/5`).
- Sin embargo, el análisis desagregado revela que **`P2` obtuvo 62.5 puntos (−5.5 por debajo del estándar de 68.0)** tras experimentar el estado vacío mudo del buscador (`H-02`) y el error tardío de saldo insuficiente (`H-01`) en `T3`. Esto demuestra empíricamente que **una interfaz técnicamente verificada puede ofrecer una experiencia deficiente cuando el usuario se enfrenta a búsquedas sin coincidencias o errores de presupuesto no prevenidos**.
