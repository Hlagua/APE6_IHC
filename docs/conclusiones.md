# Conclusiones de la Evaluación Formativa · APE 6 · Caso **CaféU**
## Respuesta Basada en Evidencia a la Pregunta Central del Laboratorio (Boehm, 1984)

- **Grupo:** 5 · **Autores:** Henry Daniel Lagua Flores (`@Hlagua`), Carlos Giovanni Ramos Jácome (`@carlitosgiovanniramos`), Melany Saleth Cevallos Goyes (`@SalyC15`) y Alison Marcela Cobos Taco (`@Itsuna18`)
- **Asignatura:** Interacción Humano-Computador (IHC) · Quinto "A" · FISEI - UTA

---

## 1. Respuesta Directa a la Pregunta Central del Laboratorio

> **Pregunta del laboratorio:** *«¿Una interfaz que funciona técnicamente puede ser una mala interfaz?» (Verificación vs. Validación — Boehm, 1984).*

**Respuesta categórica respaldada por los datos del APE 6:** **Sí.** Una interfaz puede cumplir al **100 % la verificación técnica** (*«building the product right»*: código libre de errores de ejecución, `0 px` de desborde horizontal en 4 viewports de 320 a 1366 px, etiquetas HTML5 semánticas y API idempotente que aprueba 12/12 pruebas automatizadas) y, al mismo tiempo, **fallar en la validación centrada en el ser humano** (*«building the right product»*) cuando no previene errores antes del clic, no comunica estados vacíos o destruye el turno del usuario sin confirmación previa.

---

## 2. Evidencia Empírica y Analítica que Sustenta la Conclusión

### 2.1 Contraste entre la Verificación Técnica (APE 5) y la Validación de Usabilidad (APE 6)

| Dimensión Evaluada | Resultado en Verificación Técnica (Código y Suite) | Resultado en Validación Formativa (Heurística + Usuarios P1–P3) |
| :--- | :--- | :--- |
| **Control de presupuesto (`$10.00`)** | ✅ `PedidoAPI.confirmarPedido()` rechaza correctamente cobros cuando `total > $10.00` (el saldo nunca se vuelve negativo). | ❌ **Hallazgo Crítico H-01 (Sev. 4):** Como el botón `#btn-confirmar` permanece visualmente habilitado al superar `$10.00`, **3 de 3 participantes (`P1`, `P2`, `P3`) hicieron clic esperando pagar** y no supieron por cuántos dólares se habían excedido. |
| **Buscador en tiempo real (`#buscar-producto`)** | ✅ `PedidoAPI.buscarProductos()` filtra el arreglo sin lanzar excepciones JavaScript cuando el resultado es `[]`. | ❌ **Hallazgo Mayor H-02 (Sev. 3):** Al devolver `0` coincidencias («empanada» en `P2`, «mocachino» en `P3`), la lista queda en blanco sin mensaje de estado; **`P2` esperó 9 segundos creyendo que la aplicación se había colgado**. |
| **Cancelación con reembolso (`#btn-cancelar`)** | ✅ `PedidoAPI.cancelarPedido()` restituye exactamente los `$4.25` al saldo (`$10.00`) tras el margen de 600 ms. | ⚠️ **Hallazgo Mayor H-03 (Sev. 3):** Se ejecuta en un solo clic sin diálogo de confirmación, haciendo que el estudiante **pierda su turno `#A24` y pase a `#A25`**, generando ansiedad en `P1` y `P3` y elevando la mediana de `T2` a **17.0 s** (sobre la meta de 15.0 s). |
| **Edición de ítems en bandeja (`#lista-pedido`)** | ✅ Los botones `+` y `−` funcionan en las tarjetas del catálogo superior. | ⚠️ **Hallazgo Mayor H-04 (Sev. 3):** Dentro del resumen «Revisa tu pedido» no existe un botón individual `− Quitar` por línea; `P1` y `P2` intentaron borrar el producto excedente ahí mismo y perdieron tiempo regresando al catálogo. |

### 2.2 Impacto en las Métricas ISO 9241-11:2018 y SUS (Brooke, 1996)

1. **Eficacia:** Mientras en el flujo básico (`T1` y `T2`) la tasa de éxito autónomo fue del **100.0 % (3/3)** con **0 errores críticos**, al evaluar la **Tarea de Refuerzo Post-Pilotaje (`T3`)** la eficacia cayó al **66.7 % (2/3)**, registrando **1 error crítico (`P2`) y 6 errores no críticos**. Esto demuestra que un pilotaje limitado al «camino feliz» oculta los fallos más severos de una interfaz.
2. **Eficiencia:** En `T1`, la mediana de tiempo (**16.0 s**) estuvo **4.0 s por debajo de la meta (20.0 s)**. En cambio, en `T3` la mediana se disparó a **52.0 s frente a una meta de 35.0 s (+48.6 % de sobre-tiempo)** debido al recorrido visual adicional causado por `H-01`, `H-02` y `H-04`.
3. **Satisfacción (SUS):** El puntaje SUS promedio del grupo fue **72.5 / 100** (mediana **75.0**), superando por **+4.5 puntos** el estándar de la industria (**68.0** — Brooke, 1996). No obstante, el participante **`P2` calificó con 62.5 puntos (−5.5 bajo la referencia de 68.0)** a raíz de su bloqueo en `T3`, probando cómo dos defectos de visibilidad y prevención (`H-01` y `H-02`) bastan para derrumbar la satisfacción de un usuario real aunque la interfaz sea técnicamente impecable.

---

## 3. Valor de la Triangulación Metodológica

El cruce entre el **Método 1 (Evaluación Heurística de Nielsen)** y el **Método 2 (Prueba Think-Aloud con Usuarios)** demostró que ningún método por sí solo es suficiente:
- **Lo que ambos métodos confirmaron (`H-01`, `H-02`, `H-03`, `H-04`):** El 100 % de los problemas de severidad 4 y 3 fueron anticipados por las heurísticas (`H1`, `H3`, `H5`, `H6`, `H9`) y verificados en la práctica con `P1–P3`.
- **Lo que solo la heurística detectó (`H-05`, `H-07`, `H-08`):** La inspección sistemática identificó el vacío visual durante la ventana de 600 ms (`H-05`), la falta del acelerador `Escape`/`× Limpiar` (`H-07`) y el ajuste de contraste en 320 px (`H-08`).
- **Lo que solo los usuarios descubrieron (`H-06`):** Únicamente los participantes externos (`P1` y `P3`) evidenciaron la duda contextual del mundo físico (*«¿En qué ventanilla del Edificio central presento el código #A24?»*), un punto ciego para los desarrolladores por su familiaridad previa con el proyecto desde el APE 4.

---

## 4. Cierre e Iteración Trazable en GitHub Issues

Los 8 hallazgos se tradujeron en **8 criterios técnicos verificables (`C-01` a `C-08`)** respaldados por **WCAG 2.1**, **ISO 9241-11:2018** y las **10 Heurísticas de Nielsen**, y quedaron registrados en el backlog activo del repositorio ([Issues #1 a #4](https://github.com/Hlagua/APE6_IHC/issues)) priorizados de **P1 (Crítico)** a **P4 (Menor/Cosmético)** para su implementación en el cierre del ciclo de diseño centrado en el usuario.
