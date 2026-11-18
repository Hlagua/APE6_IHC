# Evaluación Heurística Individual — Henry Daniel Lagua Flores
## Método 1: Inspección de las 10 Heurísticas de Nielsen (1994, 1995) · Caso **CaféU**

- **Evaluador:** Henry Daniel Lagua Flores ([@Hlagua](https://github.com/Hlagua))
- **Correo:** `hlagua6116@uta.edu.ec`
- **Rol en el equipo:** QA / Arquitecto (Auditorías, motor IA, resiliencia, suite de tests)
- **Fecha de inspección:** 18/11/2026
- **Prototipo inspeccionado:** `src/index.html` + `src/estilos.css` + `src/interaccion.js` + `src/api.js` (viewports 320 × 720, 360 × 800, 768 × 1024 y 1366 × 768 px)

---

## 1. Escala de Severidad y Criterios de Ponderación (Nielsen, 1995)

La severidad de cada hallazgo se determina en escala entera de **1 a 4** (`1 = Cosmético`, `2 = Menor`, `3 = Mayor`, `4 = Crítico`) ponderando tres factores:
- **Frecuencia (F: 1–4):** Probabilidad de aparición durante el uso normal o en las tareas evaluadas.
- **Impacto (I: 1–4):** Consecuencia sobre el logro de la tarea cuando el usuario encuentra el defecto.
- **Persistencia (P: 1–4):** Recurrencia del defecto incluso cuando el usuario ya conoce la interfaz.

---

## 2. Revisión Sistemática de las 10 Heurísticas de Nielsen (1994)

| Código | Heurística de Nielsen (1994) | Estado en CaféU | Observaciones de la auditoría QA / Arquitectura |
| :---: | :--- | :---: | :--- |
| **H1** | Visibilidad del estado del sistema | ❌ Con fallos mayores | Dos brechas de estado: (1) el buscador `#buscar-producto` deja el contenedor `#lista-catalogo` vacío sin mensaje cuando `filtrados.length === 0`; (2) durante los 600 ms del margen anti-doble-Enter, `#btn-cancelar` ignora eventos sin reflejar estado de enfriamiento. |
| **H2** | Relación entre el sistema y el mundo real | ✅ Cumple | Terminología alineada con el campus FISEI-UTA y formato monetario estándar (`$X.XX`). |
| **H3** | Control y libertad del usuario | ⚠️ Con hallazgos | «Cancelar pedido» revierte el cobro de inmediato, pero carece de confirmación ante una acción que destruye el turno `#A24` asignado en cocina. |
| **H4** | Consistencia y estándares | ✅ Cumple | La arquitectura CSS Mobile-First (`48rem`), los roles ARIA (`role="status"`) y el orden de tabulación del DOM cumplen estándares W3C. |
| **H5** | Prevención de errores | ❌ Con fallos críticos | Aunque la capa `PedidoAPI` impide cobrar más de `$10.00`, la capa de presentación mantiene habilitado `#btn-confirmar` cuando `total > $10.00`, induciendo al usuario a pulsar un botón destinado a fallar. |
| **H6** | Reconocer antes que recordar | ⚠️ Con hallazgos | Cuando el catálogo queda vacío por una búsqueda sin coincidencias, el usuario no tiene una indicación visual en el área de resultados que le recuerde el filtro aplicado. |
| **H7** | Flexibilidad y eficiencia de uso | ✅ Cumple | Incluye atajo `Alt+R` para reinicio de laboratorio y navegación completa por teclado. |
| **H8** | Diseño estético y minimalista | ⚠️ Con hallazgos | En 320 px, los metadatos `<small>` con color `#6B625C` sobre `#FAF7F3` tienen un ratio de contraste de `5.1:1`, aceptable en AA pero mejorable en tipografía de `13 px`. |
| **H9** | Ayudar a reconocer, diagnosticar y recuperarse de errores | ❌ Con fallos mayores | El mensaje `No se pudo procesar el pago: el total del pedido supera el saldo disponible` no cuantifica el excedente (`$X.XX`) ni guía al usuario hacia el ítem que puede restar. |
| **H10** | Ayuda y documentación | ✅ Cumple | Los textos de ayuda contextuales son concisos. |

---

## 3. Hallazgos Individuales Registrados por Henry Lagua (`@Hlagua`)

| ID Individual | ID Consolidado | Heurística violada | Componente / Ubicación | Descripción técnica del problema | F | I | P | Severidad (1–4) | Propuesta de solución |
| :---: | :---: | :--- | :--- | :--- | :-: | :-: | :-: | :---: | :--- |
| **HL-01** | **H-01** | **H5** Prevención de errores · **H9** Recuperación de errores | `src/interaccion.js` · `#btn-confirmar` · `#estado` | Desfase entre validación de negocio (`PedidoAPI`) y prevención en UI: cuando `s.total > s.saldo` (`$10.00`), `#btn-confirmar` sigue activo (`disabled = false`), provocando un clic fallido. Además, el mensaje de error omite el valor `faltante` que `PedidoAPI.confirmarPedido()` ya calcula. | 4 | 4 | 4 | **4 (Crítico)** | Deshabilitar `#btn-confirmar` de forma reactiva apenas `s.total > s.saldo` y mostrar en `#estado`: `Saldo insuficiente: te faltan $X.XX (Saldo disponible: $10.00).` |
| **HL-02** | **H-02** | **H1** Visibilidad del estado · **H6** Reconocer antes que recordar | `src/interaccion.js` · `renderizarCatalogo()` | En `renderizarCatalogo()`, cuando `filtrados.length === 0`, no se inserta ningún nodo en `#lista-catalogo`. El usuario percibe una falla de carga en lugar de un resultado vacío legítimo. | 3 | 3 | 3 | **3 (Mayor)** | Renderizar un `<li class="estado-vacio" role="status">` con el término buscado y un botón de acción rápida `Restablecer menú`. |
| **HL-03** | **H-03** | **H3** Control y libertad · **H5** Prevención de errores | `src/interaccion.js` · `#btn-cancelar` | La cancelación del pedido confirmado `#A24` se ejecuta en un único clic sin confirmación, provocando la pérdida irreversible del turno `#A24` (la siguiente confirmación asigna `#A25`). | 3 | 3 | 3 | **3 (Mayor)** | Implementar confirmación en dos pasos o diálogo modal accesible (`role="alertdialog"`) advirtiendo la pérdida del turno `#A24`. |
| **HL-04** | **H-05** | **H1** Visibilidad del estado del sistema | `src/interaccion.js` · `MARGEN_DOBLE_PULSACION_MS` | Durante la ventana de 600 ms posterior a confirmar, `#btn-cancelar` recibe el foco (`btnCancelar.focus()`) pero descarta silenciosamente cualquier evento `click` sin indicador visual de bloqueo temporal. | 2 | 2 | 2 | **2 (Menor)** | Añadir indicador visual temporal (`.boton--enfriamiento`) durante los 600 ms posteriores al pago. |
| **HL-05** | **H-08** | **H8** Diseño estético y minimalista | `src/estilos.css` · `--texto-sec` (`#6B625C`) | El tamaño `0.8125rem` (13 px) en `.productos small` y `.item-catalogo__info small` reduce la legibilidad en pantallas de 320 px. | 2 | 1 | 1 | **1 (Cosmético)** | Subir tamaño a `0.875rem` (14 px) y oscurecer `--texto-sec` a `#524944` (contraste > 7:1 AAA). |

---

## 4. Síntesis del Evaluador (QA / Arquitecto)

- **Total de hallazgos reportados:** 5 (`1 Crítico [Sev. 4]`, `2 Mayores [Sev. 3]`, `1 Menor [Sev. 2]`, `1 Cosmético [Sev. 1]`).
- **Conclusión de Auditoría QA:** La suite automatizada del APE 5 comprobó que el software cumple su especificación técnica (*Verificación*), pero la auditoría heurística demuestra que una arquitectura técnicamente limpia puede inducir errores humanos si no previene estados inválidos antes del clic (*Validación* — Boehm, 1984).
