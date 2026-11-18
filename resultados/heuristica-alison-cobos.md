# Evaluación Heurística Individual — Alison Marcela Cobos Taco
## Método 1: Inspección de las 10 Heurísticas de Nielsen (1994, 1995) · Caso **CaféU**

- **Evaluadora:** Alison Marcela Cobos Taco ([@Itsuna18](https://github.com/Itsuna18))
- **Correo:** `tacomarcelab@gmail.com`
- **Rol en el equipo:** Desarrollador Back-End (API, modelos, persistencia, endpoints)
- **Fecha de inspección:** 18/11/2026
- **Prototipo inspeccionado:** `src/index.html` + `src/estilos.css` + `src/interaccion.js` + `src/api.js` (viewports 360 × 800 y 1366 × 768 px)

---

## 1. Escala de Severidad y Criterios de Ponderación (Nielsen, 1995)

Cada problema detectado se evalúa ponderando tres dimensiones en escala de 1 a 4:
- **Frecuencia (F):** ¿Con qué frecuencia ocurre? (`1 = Raro <10%`, `2 = Ocasional 10–30%`, `3 = Frecuente 30–70%`, `4 = Muy frecuente >70%`).
- **Impacto (I):** ¿Qué tan difícil es para el usuario superarlo? (`1 = Mínimo`, `2 = Moderado`, `3 = Severo`, `4 = Bloqueante`).
- **Persistencia (P):** ¿Se supera una vez aprendido o molesta siempre? (`1 = Se aprende a evitar`, `2 = Reaparece ocasionalmente`, `3 = Difícil de evitar`, `4 = Inevitable en cada uso`).

**Severidad resultante (1–4):**
- **1 = Cosmético:** No necesita corregirse a menos que haya tiempo extra.
- **2 = Menor:** Baja prioridad de corrección; genera duda leve.
- **3 = Mayor:** Alta prioridad de corrección; afecta notablemente la eficiencia o comprensión.
- **4 = Crítico:** Imperativo corregirlo antes de lanzar el producto; induce a error grave o bloquea la tarea.

---

## 2. Revisión Sistemática de las 10 Heurísticas de Nielsen (1994)

| Código | Heurística de Nielsen (1994) | Estado en CaféU | Observaciones de la inspección independiente |
| :---: | :--- | :---: | :--- |
| **H1** | Visibilidad del estado del sistema | ⚠️ Con hallazgos | El pago exitoso muestra bien el número `#A24` y el saldo `$5.75`, pero durante los 600 ms posteriores al pago el botón «Cancelar pedido» ignora clics sin indicación visual. Además, si la búsqueda no arroja resultados, el catálogo queda vacío en silencio. |
| **H2** | Relación entre el sistema y el mundo real | ✅ Cumple | Utiliza términos familiares para el estudiante de la UTA («Edificio central», «Tarjeta universitaria», «Sánduche», «12 oz»). |
| **H3** | Control y libertad del usuario | ⚠️ Con hallazgos | Permite cancelar el pedido y recibir el reembolso de inmediato, pero **cancela en un solo clic sin confirmación**, haciendo que el usuario pierda su turno `#A24` y pase a `#A25` si se equivocó al pulsar. |
| **H4** | Consistencia y estándares | ✅ Cumple | Mantiene la paleta visual CaféU del APE 4 y APE 5, botones primarios/secundarios diferenciados y estructura HTML5 semántica. |
| **H5** | Prevención de errores | ❌ Con fallos críticos | **Fallo crítico:** Cuando se agregan productos desde el catálogo y el total supera el saldo disponible (`$10.00`), el botón «Confirmar y pagar» sigue habilitado y recién falla cuando el estudiante intenta pagar. |
| **H6** | Reconocer antes que recordar | ⚠️ Con hallazgos | Los datos clave (`Total`, `Retiro`, `Pago`) están visibles antes del botón de pago, pero en la lista de productos agregados falta un botón individual claro `− Quitar` junto a cada ítem del resumen para reducir unidades directamente. |
| **H7** | Flexibilidad y eficiencia de uso | ✅ Cumple | La navegación por teclado (`Tab`, `Enter`, `Espacio`) y el reinicio rápido (`Alt+R`) funcionan fluidamente. |
| **H8** | Diseño estético y minimalista | ✅ Cumple | Interfaz limpia y enfocada en la tarea, sin publicidad ni elementos decorativos superfluos. |
| **H9** | Ayudar a reconocer, diagnosticar y recuperarse de errores | ⚠️ Con hallazgos | Cuando ocurre el rechazo por saldo insuficiente (`total > $10.00`), el mensaje de error no calcula ni muestra el monto exacto faltante (`$X.XX`) ni sugiere quitar un ítem específico. |
| **H10** | Ayuda y documentación | ✅ Cumple | La interfaz incluye indicaciones breves en la cabecera y el estado inicial. |

---

## 3. Hallazgos Individuales Registrados por Alison Cobos (`@Itsuna18`)

| ID Individual | ID Consolidado | Heurística violada | Componente / Ubicación | Descripción técnica del problema | F | I | P | Severidad (1–4) | Propuesta de solución |
| :---: | :---: | :--- | :--- | :--- | :-: | :-: | :-: | :---: | :--- |
| **AC-01** | **H-01** | **H5** Prevención de errores · **H9** Recuperación de errores | `src/interaccion.js` · `src/api.js` · `#btn-confirmar` | Al agregar productos en la Tarea 3 y superar los `$10.00` de saldo (ej. total `$11.25`), el botón «Confirmar y pagar» no se deshabilita preventivamente ni alerta cuánto dinero falta antes del clic. Al hacer clic, la API devuelve `saldo_insuficiente`, pero el usuario tuvo que equivocarse primero. | 4 | 4 | 4 | **4 (Crítico)** | Validar `total > saldo` en cada cambio del pedido, deshabilitar `#btn-confirmar` proactivamente y mostrar en `#estado` cuántos dólares faltan exactamente (`Te faltan $1.25`). |
| **AC-02** | **H-03** | **H3** Control y libertad · **H5** Prevención de errores | `src/interaccion.js` · `#btn-cancelar` | Pulsar «Cancelar pedido» ejecuta `PedidoAPI.cancelarPedido()` de inmediato en un solo clic (pasados los 600 ms). No existe confirmación de dos pasos ni advierte que el turno `#A24` se perderá (al volver a confirmar asigna `#A25`). | 3 | 3 | 3 | **3 (Mayor)** | Agregar confirmación en dos pasos (`¿Seguro que deseas cancelar #A24? Perderás tu turno actual`) antes de ejecutar la anulación en la API. |
| **AC-03** | **H-04** | **H6** Reconocer antes que recordar | `src/index.html` · `ul.productos` | Cuando el usuario agrega productos adicionales desde el catálogo, la lista `ul.productos` de la tarjeta «Revisa tu pedido» solo muestra el texto y el subtotal, obligando al usuario a regresar arriba al catálogo para buscar el botón `−` del producto que desea quitar. | 3 | 3 | 2 | **3 (Mayor)** | Incluir un botón compacto `− Quitar` directamente en cada fila `<li class="item-pedido">` dentro del resumen de «Mi pedido». |
| **AC-04** | **H-05** | **H1** Visibilidad del estado del sistema | `src/interaccion.js` · `MARGEN_DOBLE_PULSACION_MS` | Durante los 600 ms de protección anti-doble-Enter tras pagar, `#btn-cancelar` se muestra con apariencia 100 % activa aunque ignora cualquier clic. Si un usuario rápido pulsa en ese lapso, no recibe feedback visual. | 2 | 2 | 2 | **2 (Menor)** | Aplicar un estado visual `.boton--enfriamiento` o habilitar el botón con una transición visual clara tras los 600 ms. |

---

## 4. Síntesis de la Evaluadora

- **Total de hallazgos reportados:** 4 (`1 Crítico [Sev. 4]`, `2 Mayores [Sev. 3]`, `1 Menor [Sev. 2]`).
- **Conclusión desde Back-End:** Aunque `src/api.js` protege correctamente la integridad de datos (impide saldo negativo y bloquea cobros duplicados), **verificar la regla en la API no equivale a validarla en la experiencia del usuario**: el usuario necesita saber *antes de pulsar pagar* que su pedido de `$11.25` excede sus `$10.00` disponibles y poder quitar ítems directamente desde el resumen del pedido.
