# PRÁCTICA EXPERIMENTAL DE APRENDIZAJE – APE 6 · Grupo 5
## Evaluación y Validación de Prototipos · Caso **CaféU** · Interacción Humano-Computador (IHC) · Quinto "A"
### Universidad Técnica de Ambato (UTA) · FISEI · Carrera de Ingeniería de Software

**Docente:** Ing. Mg. José Caiza · **Repositorio APE 6:** [https://github.com/Hlagua/APE6_IHC](https://github.com/Hlagua/APE6_IHC) · **Base previa (APE 5):** [https://github.com/Hlagua/APE5_IHC](https://github.com/Hlagua/APE5_IHC)

> **Pregunta central del laboratorio:** *«¿Una interfaz que funciona técnicamente puede ser una mala interfaz?»* (**Verificación vs. Validación** — Boehm, 1984).
>
> **Respuesta con evidencia del APE 6:** **Sí.** El prototipo web adaptable de **CaféU** aprobó el 100 % de la verificación técnica (0 px de desborde en 320–1366 px y 12/12 pruebas automatizadas), pero la validación formativa combinando **Evaluación Heurística (Nielsen, 1994/1995)** y **Pruebas de Usabilidad Think-Aloud + SUS (ISO 9241-11:2018; Brooke, 1996)** destapó **8 hallazgos de usabilidad** (`1 Crítico [Sev. 4]`, `3 Mayores [Sev. 3]`, `3 Menores [Sev. 2]` y `1 Cosmético [Sev. 1]`) que redujeron la eficacia autónoma al **66.7 %** en la tarea de refuerzo post-pilotaje (`T3`) y llevaron el puntaje SUS del participante `P2` a **62.5** (bajo el estándar industrial de **68.0**).

---

## 1. Integrantes del Grupo 5 y Trabajo Colaborativo en GitHub

| N.º | Integrante | Usuario GitHub | Correo | Rol | Rama | Issue Sprint | Pull Request | Evidencia Heurística Individual |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| 1 | **Alison Marcela Cobos Taco** | [@Itsuna18](https://github.com/Itsuna18) | `tacomarcelab@gmail.com` | Desarrollador Back-End | `feat/ajuste-post-pilotaje-backend` | [#5](https://github.com/Hlagua/APE6_IHC/issues/5) | [PR #9](https://github.com/Hlagua/APE6_IHC/pull/9) | [`resultados/heuristica-alison-cobos.md`](resultados/heuristica-alison-cobos.md) |
| 2 | **Melany Saleth Cevallos Goyes** | [@SalyC15](https://github.com/SalyC15) | `mcevallos8901@uta.edu.ec` | Desarrollador Front-End | `feat/interfaz-refuerzo-frontend` | [#6](https://github.com/Hlagua/APE6_IHC/issues/6) | [PR #10](https://github.com/Hlagua/APE6_IHC/pull/10) | [`resultados/heuristica-melany-cevallos.md`](resultados/heuristica-melany-cevallos.md) |
| 3 | **Carlos Giovanni Ramos Jácome** | [@carlitosgiovanniramos](https://github.com/carlitosgiovanniramos) | `carlos.giovanni.ramos.work@gmail.com` | Tester | `test/usabilidad-usuarios-sus` | [#7](https://github.com/Hlagua/APE6_IHC/issues/7) | [PR #11](https://github.com/Hlagua/APE6_IHC/pull/11) | [`resultados/heuristica-carlos-ramos.md`](resultados/heuristica-carlos-ramos.md) |
| 4 | **Henry Daniel Lagua Flores** | [@Hlagua](https://github.com/Hlagua) | `hlagua6116@uta.edu.ec` | QA / Arquitecto | `docs/triangulacion-cierre-qa` | [#8](https://github.com/Hlagua/APE6_IHC/issues/8) | [PR #12](https://github.com/Hlagua/APE6_IHC/pull/12) | [`resultados/heuristica-henry-lagua.md`](resultados/heuristica-henry-lagua.md) |

---

## 2. Fase 3.1: Ajuste Post-Pilotaje y Protocolo de Reinicio (`F5`)

Detalle completo en [`docs/ajuste_post_pilotaje.md`](docs/ajuste_post_pilotaje.md):
- **Brechas corregidas de la Fase 2 (Pilotaje):** En el pilotaje solo se probaron `T1` (confirmar pago del pedido `#A24`) y `T2` (cancelar pedido y verificar reembolso), dejando sin evaluar las funciones críticas de **búsqueda, filtrado por categoría y prevención de errores por exceso de saldo (`> $10.00`)**, además de la persistencia de `sessionStorage` entre sesiones.
- **Tarea de Refuerzo incorporada (`T3` · Meta ≤ 35.0 s):** Buscar/filtrar productos en el catálogo rápido (`#buscar-producto`, chips `Todos`, `Bebidas`, `Snacks`, `Postres`), agregar ítems hasta superar los `$10.00` de la tarjeta universitaria, observar la respuesta del sistema al intentar pagar y ajustar el pedido para concretar el cobro.
- **Reinicio de estado entre sesiones (`F5` / `Alt+R` / `#btn-reiniciar-lab`):** Ejecuta `PedidoAPI.reiniciar()`, elimina `ape6_cafeu_pedido_v1` de `sessionStorage`, limpia el buscador/filtros y garantiza que cada sesión (`P1`, `P2`, `P3`) inicie con saldo **`$10.00`**, pedido base **`$4.25`**, estado **`pendiente`** y correlativo **`#A24`**.

---

## 3. Fase 3.2 y 3.3: Evidencias Individuales (Heurística y Usuarios P1–P3)

### Evaluaciones Heurísticas Independientes (Nielsen, 1994; Severidad 1–4 de Nielsen, 1995)
- [`resultados/heuristica-alison-cobos.md`](resultados/heuristica-alison-cobos.md) — Alison Cobos (`@Itsuna18`): 4 hallazgos (`H-01` Sev. 4, `H-03` Sev. 3, `H-04` Sev. 3, `H-05` Sev. 2).
- [`resultados/heuristica-melany-cevallos.md`](resultados/heuristica-melany-cevallos.md) — Melany Cevallos (`@SalyC15`): 5 hallazgos (`H-01` Sev. 4, `H-02` Sev. 3, `H-04` Sev. 3, `H-07` Sev. 2, `H-08` Sev. 1).
- [`resultados/heuristica-carlos-ramos.md`](resultados/heuristica-carlos-ramos.md) — Carlos Ramos (`@carlitosgiovanniramos`): 5 hallazgos (`H-01` Sev. 4, `H-02` Sev. 3, `H-03` Sev. 3, `H-07` Sev. 2, `H-08` Sev. 1).
- [`resultados/heuristica-henry-lagua.md`](resultados/heuristica-henry-lagua.md) — Henry Lagua (`@Hlagua`): 5 hallazgos (`H-01` Sev. 4, `H-02` Sev. 3, `H-03` Sev. 3, `H-05` Sev. 2, `H-08` Sev. 1).

### Registros de Sesiones Think-Aloud con Participantes Externos (`P1` a `P3`)
- Consentimiento informado anonimizado: [`docs/consentimiento_informado.md`](docs/consentimiento_informado.md) y protocolo con los 4 roles del laboratorio (Moderadora: Melany Cevallos; Cronometrista: Carlos Ramos; Observadora: Alison Cobos; Soporte F5/QA: Henry Lagua): [`docs/protocolo_pruebas.md`](docs/protocolo_pruebas.md).
- [`resultados/P1.md`](resultados/P1.md) — Participante externo `P1` (T1: `16.0 s`, T2: `17.0 s`, T3: `52.0 s` · Éxito: `3/3` · SUS: **`80.0`**).
- [`resultados/P2.md`](resultados/P2.md) — Participante externo `P2` (T1: `14.0 s`, T2: `13.0 s`, T3: `64.0 s` con ayuda · Éxito autónomo: `2/3` · SUS: **`62.5`**).
- [`resultados/P3.md`](resultados/P3.md) — Participante externo `P3` (T1: `18.0 s`, T2: `19.0 s`, T3: `48.0 s` · Éxito: `3/3` · SUS: **`75.0`**).

---

## 4. Fase 3.4: Consolidación de Métricas (ISO 9241-11:2018 y SUS)

Detalle completo en [`resultados/metricas_iso_sus.md`](resultados/metricas_iso_sus.md).

### 4.1 Tabla de Eficacia y Eficiencia (ISO 9241-11:2018)

| Tarea Evaluada | Meta (s) | P1 (s) | P2 (s) | P3 (s) | Mediana (s) | Diferencia vs. Meta | Tasa de Éxito Autónomo (%) | Errores Críticos | Errores No Críticos |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **T1:** Confirmar pedido `#A24` y verificar datos | **20.0 s** | 16.0 | 14.0 | 18.0 | **16.0 s** | **−4.0 s** (✅ Cumple) | **100.0 % (3/3)** | **0** | **0** |
| **T2:** Cancelar pedido, verificar reembolso y re-confirmar | **15.0 s** | 17.0 | 13.0 | 19.0 | **17.0 s** | **+2.0 s** (⚠️ Leve exceso) | **100.0 % (3/3)** | **0** | **2** |
| **T3 (Refuerzo):** Buscador, filtro y límite de saldo (`$10.00`) | **35.0 s** | 52.0 | 64.0* | 48.0 | **52.0 s** | **+17.0 s** (❌ No cumple) | **66.7 % (2/3)** | **1** | **6** |
| **Global / Consolidado** | — | 85.0 | 91.0 | 85.0 | — | — | **88.9 % (8/9)** | **1** | **8** |

### 4.2 Tabla de Satisfacción — Cuestionario SUS (Brooke, 1996)

| Participante | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | Suma Base | Puntaje SUS (0–100) | Referencia Industria | Diferencia vs. 68.0 | Valoración |
| :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :---: | :---: | :---: | :---: | :--- |
| **P1** | 4 | 2 | 4 | 1 | 4 | 2 | 4 | 2 | 5 | 2 | 32 | **80.0** | 68.0 | **+12.0** | Buena / Excelente (B+) |
| **P2** | 3 | 3 | 3 | 2 | 3 | 2 | 4 | 3 | 4 | 2 | 25 | **62.5** | 68.0 | **−5.5** | **Bajo el promedio (D)** |
| **P3** | 4 | 2 | 4 | 2 | 4 | 2 | 4 | 2 | 4 | 2 | 30 | **75.0** | 68.0 | **+7.0** | Buena (B) |
| **Promedio** | **3.67** | **2.33** | **3.67** | **1.67** | **3.67** | **2.00** | **4.00** | **2.33** | **4.33** | **2.00** | **29.0** | **72.5** | **68.0** | **+4.5** | **Aceptable / Buena (C+/B−)** |
| **Mediana** | 4 | 2 | 4 | 2 | 4 | 2 | 4 | 2 | 4 | 2 | 30 | **75.0** | **68.0** | **+7.0** | **Buena (B)** |

---

## 5. Fase 4.5: Matriz Consolidada de Hallazgos (`H-01` a `H-08`)

Detalle completo en [`resultados/matriz_hallazgos_triangulacion.md`](resultados/matriz_hallazgos_triangulacion.md).

| ID | Problema Unificado | Heurística (Nielsen, 1994) | F | I | P | Severidad Consensuada | Evidencia (Heurística y Usuarios) | Propuesta de Mejora |
| :---: | :--- | :--- | :-: | :-: | :-: | :---: | :--- | :--- |
| **H-01** | El botón «Confirmar y pagar» permanece habilitado cuando el total supera el saldo (`$10.00`) y el error no indica cuánto dinero falta. | **H5** Prevención de errores · **H9** Recuperación | 4 | 4 | 4 | **4 (Crítico)** | 4/4 evaluadores (`AC-01`, `MC-01`, `CR-01`, `HL-01`) + `P1`, `P2` (error crítico) y `P3` en `T3`. | Deshabilitar `#btn-confirmar` cuando `total > saldo` y mostrar en `#estado` el monto exacto faltante (`Te faltan $X.XX`). |
| **H-02** | El buscador (`#buscar-producto`) deja la lista en blanco sin mensaje de «0 resultados» cuando no hay coincidencias. | **H1** Visibilidad del estado · **H6** Reconocer | 3 | 3 | 3 | **3 (Mayor)** | 3/4 evaluadores (`MC-02`, `CR-02`, `HL-02`) + `P2` («empanada», 9 s detenido) y `P3` («mocachino») en `T3`. | Mostrar estado vacío con `role="status"` (`No se encontraron productos para «...»`) y botón `Ver todo el menú`. |
| **H-03** | «Cancelar pedido» anula el pedido en un solo clic sin confirmación ni advertencia de perder el turno `#A24` (`#A24` → `#A25`). | **H3** Control y libertad · **H5** Prevención | 3 | 3 | 3 | **3 (Mayor)** | 3/4 evaluadores (`AC-02`, `CR-03`, `HL-03`) + sorpresa y duda de `P1` y `P3` en `T2`. | Solicitar confirmación en dos pasos advirtiendo la pérdida del turno `#A24` antes de anular. |
| **H-04** | Los ítems agregados en «Revisa tu pedido» (`#lista-pedido`) carecen de botón individual `− Quitar` en cada línea. | **H6** Reconocer · **H3** Control y libertad | 3 | 3 | 3 | **3 (Mayor)** | 2/4 evaluadoras (`AC-03`, `MC-03`) + `P1` y `P2` intentando borrar desde el resumen en `T3`. | Agregar botón `− Quitar` (`≥ 44 × 44 px`) en cada fila de `#lista-pedido`. |
| **H-05** | El bloqueo de 600 ms en «Cancelar pedido» no muestra retroalimentación visual de enfriamiento. | **H1** Visibilidad del estado | 2 | 2 | 2 | **2 (Menor)** | Detectado en inspección heurística (`AC-04`, `HL-04`). | Aplicar clase `.boton--enfriamiento` durante los 600 ms posteriores al pago. |
| **H-06** | No se indica en qué ventanilla del Edificio central presentar el código `#A24` ni si requiere carné universitario. | **H10** Ayuda · **H2** Mundo real | 2 | 2 | 2 | **2 (Menor)** | Verbalizado por `P1` y `P3` al finalizar `T1`. | Especificar `Ventanilla Rápida (PB, Edificio central) con código #A24 y carné UTA`. |
| **H-07** | Falta botón rápido `× Limpiar` o soporte de tecla `Escape` en el buscador y filtros. | **H7** Flexibilidad y eficiencia | 2 | 2 | 2 | **2 (Menor)** | Detectado en inspección heurística (`MC-04`, `CR-04`). | Añadir botón `× Limpiar` y manejador de tecla `Escape` en `#buscar-producto`. |
| **H-08** | Tamaño compacto (`0.8125rem`) y contraste ajustado de subtítulos `<small>` en viewport de 320 px. | **H8** Diseño estético y minimalista | 2 | 1 | 1 | **1 (Cosmético)** | Detectado en inspección heurística (`MC-05`, `CR-05`, `HL-05`). | Subir `<small>` a `0.875rem` y oscurecer `--texto-sec` a `#524944` (contraste `7.1:1`). |

---

## 6. Fase 4.6: Triangulación Metodológica

| Categoría de Cruce | Hallazgos | Total (%) | Síntesis Analítico-Empírica |
| :--- | :--- | :---: | :--- |
| **Confirmado por ambos métodos**<br>*(Heurística + Usuarios)* | `H-01` (Sev. 4), `H-02` (Sev. 3), `H-03` (Sev. 3), `H-04` (Sev. 3) | **4 (50.0 %)** | Los 4 defectos más graves predichos por las heurísticas de Nielsen causaron bloqueos, clics fallidos y exceso de tiempo en las sesiones reales con `P1–P3`. |
| **Solo heurística**<br>*(Método Analítico)* | `H-05` (Sev. 2), `H-07` (Sev. 2), `H-08` (Sev. 1) | **3 (37.5 %)** | Captura condiciones de borde temporales (`600 ms`), atajos para expertos (`Escape`) y detalles en 320 px que 3 usuarios novatos no verbalizan. |
| **Solo usuarios**<br>*(Método Empírico)* | `H-06` (Sev. 2) | **1 (12.5 %)** | Supera el «sesgo de familiaridad» de los diseñadores al evidenciar dudas sobre el retiro físico en el mostrador de la cafetería. |

---

## 7. Fase 4.7: Criterios Técnicos de Mejora (`C-01` a `C-08`)

| ID | Hallazgo | Componente Afectado | Cambio Técnico Específico y Verificable | Estándar de Respaldo |
| :---: | :---: | :--- | :--- | :--- |
| **C-01** | `H-01` | `src/interaccion.js` · `#btn-confirmar` · `#estado` | Si `total > saldo`, aplicar `btnConfirmar.disabled = true` preventivamente y mostrar en `#estado` (`role="status"`): `Saldo insuficiente: te faltan $X.XX (Saldo: $10.00).` | **Nielsen:** H5, H9 · **WCAG 2.1:** SC 3.3.1, 4.1.3 · **ISO 9241-11:** Eficacia |
| **C-02** | `H-02` | `src/interaccion.js` · `#lista-catalogo` | Cuando `filtrados.length === 0`, insertar `<li class="catalogo-vacio" role="status">` con `No se encontraron productos para «[término]»` y botón `Ver todo el menú`. | **Nielsen:** H1, H6 · **WCAG 2.1:** SC 4.1.3 |
| **C-03** | `H-03` | `src/interaccion.js` · `#btn-cancelar` | Incorporar confirmación de dos pasos antes de anular el pedido pagado, advirtiendo que se perderá el turno `#A24`. | **Nielsen:** H3, H5 · **WCAG 2.1:** SC 3.3.4 · **ISO 9241-11:** Eficacia |
| **C-04** | `H-04` | `src/index.html` · `#lista-pedido` | Incluir botón `<button type="button" class="btn-quitar-linea">− Quitar</button>` (`≥ 44 × 44 px`) en cada ítem dentro de «Revisa tu pedido». | **Nielsen:** H6, H3 · **WCAG 2.1:** SC 2.5.5 · **ISO 9241-11:** Eficiencia |
| **C-05** | `H-05` | `src/interaccion.js` · `src/estilos.css` | Aplicar clase `.boton--enfriamiento` (`opacity: 0.7`) a `#btn-cancelar` durante los `600 ms` posteriores al cobro. | **Nielsen:** H1 · **WCAG 2.1:** SC 1.3.3 |
| **C-06** | `H-06` | `src/index.html` · `#estado` | Indicar explícitamente `Ventanilla Rápida (PB, Edificio central) presentando el código #A24 y tu carné UTA`. | **Nielsen:** H10, H2 · **ISO 9241-11:** Satisfacción |
| **C-07** | `H-07` | `src/index.html` · `.campo-busqueda` | Agregar botón `× Limpiar` junto a `#buscar-producto` y soporte para la tecla `Escape`. | **Nielsen:** H7 · **WCAG 2.1:** SC 2.1.1 |
| **C-08** | `H-08` | `src/estilos.css` · `--texto-sec` | Cambiar `--texto-sec` a `#524944` (contraste `7.12:1` AAA) y subir `<small>` a `0.875rem` (14 px). | **Nielsen:** H8 · **WCAG 2.1:** SC 1.4.3, 1.4.6 |

---

## 8. Fase 4.8: Backlog Priorizado en GitHub Issues y Conclusiones

| Prioridad | GitHub Issue Vinculado | Hallazgos | Criterios Técnicos | Severidad | Resumen de la Mejora Trazable | Responsables |
| :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **P1 (Crítica)** | [**Issue #1**](https://github.com/Hlagua/APE6_IHC/issues/1) | `H-01` | `C-01` | **4 (Crítico)** | Validación proactiva de saldo insuficiente (`> $10.00`), bloqueo preventivo de `#btn-confirmar` y cálculo del monto faltante. | `@Itsuna18` · `@SalyC15` |
| **P2 (Alta)** | [**Issue #2**](https://github.com/Hlagua/APE6_IHC/issues/2) | `H-02`, `H-07` | `C-02`, `C-07` | **3 (Mayor)** | Estado vacío informativo en `#lista-catalogo` cuando hay 0 resultados y botón/atajo `Escape` para limpiar filtros. | `@SalyC15` |
| **P3 (Media-Alta)** | [**Issue #3**](https://github.com/Hlagua/APE6_IHC/issues/3) | `H-03`, `H-04` | `C-03`, `C-04` | **3 (Mayor)** | Confirmación de seguridad antes de cancelar el turno `#A24` y botón individual `− Quitar` en cada línea de `#lista-pedido`. | `@Itsuna18` · `@carlitosgiovanniramos` |
| **P4 (Refinamiento)** | [**Issue #4**](https://github.com/Hlagua/APE6_IHC/issues/4) | `H-05`, `H-06`, `H-08` | `C-05`, `C-06`, `C-08` | **2–1 (Menor / Cosmético)** | Estado visual durante el margen de 600 ms, indicación de Ventanilla Rápida para retiro y mejora de contraste AAA en `<small>`. | `@Hlagua` |

- **Documento completo de Conclusiones:** [`docs/conclusiones.md`](docs/conclusiones.md)
- **Informe Oficial UTA (DOCX y PDF):** [`06_documento/APE6_Informe_Final.pdf`](06_documento/APE6_Informe_Final.pdf)

---

## 9. Estructura del Repositorio y Ejecución Local

| Ruta | Contenido |
| :--- | :--- |
| [`src/`](src/) | Prototipo evaluado (`index.html`, `estilos.css`, `interaccion.js`, `api.js`) con buscador, filtros y reinicio `F5` |
| [`resultados/heuristica-*.md`](resultados/) | 4 evaluaciones heurísticas individuales (`alison-cobos`, `melany-cevallos`, `carlos-ramos`, `henry-lagua`) |
| [`resultados/P1.md`](resultados/P1.md) a [`P3.md`](resultados/P3.md) | Registros individuales de las 3 sesiones de usabilidad *Think-Aloud* + respuestas SUS |
| [`resultados/metricas_iso_sus.md`](resultados/metricas_iso_sus.md) | Tabulación de Eficacia, Eficiencia y Satisfacción (ISO 9241-11:2018 y SUS) |
| [`resultados/matriz_hallazgos_triangulacion.md`](resultados/matriz_hallazgos_triangulacion.md) | Matriz Consolidada (`H-01` a `H-08`), Triangulación y Criterios Técnicos (`C-01` a `C-08`) |
| [`docs/conclusiones.md`](docs/conclusiones.md) | Respuesta argumentada a la pregunta central del laboratorio (Boehm, 1984) |
| [`docs/ajuste_post_pilotaje.md`](docs/ajuste_post_pilotaje.md) | Brechas de la Fase 2, Tarea de Refuerzo `T3` y protocolo de reinicio `F5` |
| [`docs/consentimiento_informado.md`](docs/consentimiento_informado.md) · [`docs/protocolo_pruebas.md`](docs/protocolo_pruebas.md) | Consentimiento informado anonimizado, 4 roles del laboratorio y cuestionario SUS |
| [`presentacion/index.html`](presentacion/index.html) | Presentación interactiva de 10 diapositivas sobre los métodos aplicados y sus resultados |
| [`tests/test_runner.html`](tests/test_runner.html) | Suite automatizada de 12 pruebas |
| [`evidencias/`](evidencias/) | Capturas del prototipo bajo evaluación y de los hallazgos `H-01` a `H-04` |
| [`06_documento/`](06_documento/) | Informe Final del APE 6 en formato oficial de la Universidad Técnica de Ambato (`.docx` y `.pdf`) |

```bash
python -m http.server 8769
# Abrir http://localhost:8769/src/index.html o http://localhost:8769/presentacion/
```
