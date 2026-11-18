# Evaluación Heurística Individual — Carlos Giovanni Ramos Jácome
## Método 1: Inspección de las 10 Heurísticas de Nielsen (1994, 1995) · Caso **CaféU**

- **Evaluador:** Carlos Giovanni Ramos Jácome ([@carlitosgiovanniramos](https://github.com/carlitosgiovanniramos))
- **Correo:** `carlos.giovanni.ramos.work@gmail.com`
- **Rol en el equipo:** Tester (Protocolos de validación, casos de prueba, métricas SUS)
- **Fecha de inspección:** 18/11/2026
- **Prototipo inspeccionado:** `src/index.html` + `src/estilos.css` + `src/interaccion.js` + `src/api.js` (viewports 320 × 720, 360 × 800 y 1366 × 768 px)

---

## 1. Escala de Severidad y Criterios de Ponderación (Nielsen, 1995)

Se califica cada problema en escala de **1 (Cosmético)**, **2 (Menor)**, **3 (Mayor)** y **4 (Crítico)** ponderando:
- **Frecuencia (F: 1–4):** Proporción de usuarios o escenarios en los que aparece el fallo.
- **Impacto (I: 1–4):** Grado de obstáculo que representa cuando ocurre.
- **Persistencia (P: 1–4):** Si el problema sigue afectando en usos repetidos.

---

## 2. Revisión Sistemática de las 10 Heurísticas de Nielsen (1994)

| Código | Heurística de Nielsen (1994) | Estado en CaféU | Observaciones de la inspección independiente |
| :---: | :--- | :---: | :--- |
| **H1** | Visibilidad del estado del sistema | ❌ Con fallos mayores | El buscador `#buscar-producto` no informa cuando una consulta devuelve `0` coincidencias; simplemente desaparecen las tarjetas del catálogo dejando un espacio vacío. |
| **H2** | Relación entre el sistema y el mundo real | ✅ Cumple | Vocabulario claro y acorde al contexto estudiantil de la UTA (retiro en Edificio central, tarjeta universitaria, montos en dólares). |
| **H3** | Control y libertad del usuario | ⚠️ Con hallazgos | El botón «Cancelar pedido» ejecuta una acción destructiva sobre el turno `#A24` de forma inmediata sin pedir confirmación previa. |
| **H4** | Consistencia y estándares | ✅ Cumple | Controles semánticos consistentes y comportamiento uniforme entre vista móvil y de escritorio. |
| **H5** | Prevención de errores | ❌ Con fallos críticos | El sistema permite pulsar «Confirmar y pagar» aun cuando el total del carrito (`$11.00`) supera el saldo de la tarjeta (`$10.00`), en lugar de deshabilitar el botón y advertir antes del clic. |
| **H6** | Reconocer antes que recordar | ⚠️ Con hallazgos | Al buscar un término inexistente no se muestra qué filtro o texto produjo la lista vacía. |
| **H7** | Flexibilidad y eficiencia de uso | ⚠️ Con hallazgos | No existe botón rápido para limpiar la búsqueda/categoría ni atajo `Escape` en `#buscar-producto`. |
| **H8** | Diseño estético y minimalista | ⚠️ Con hallazgos | En 320 px, los textos secundarios `<small>` tienen un contraste y tamaño algo justos para lectura rápida caminando entre aulas. |
| **H9** | Ayudar a reconocer, diagnosticar y recuperarse de errores | ⚠️ Con hallazgos | El mensaje cuando falla el pago por saldo insuficiente es genérico y no informa cuántos dólares exceden el límite de `$10.00`. |
| **H10** | Ayuda y documentación | ✅ Cumple | Incluye guía breve en el catálogo rápido y en el estado inicial del pedido. |

---

## 3. Hallazgos Individuales Registrados por Carlos Ramos (`@carlitosgiovanniramos`)

| ID Individual | ID Consolidado | Heurística violada | Componente / Ubicación | Descripción técnica del problema | F | I | P | Severidad (1–4) | Propuesta de solución |
| :---: | :---: | :--- | :--- | :--- | :-: | :-: | :-: | :---: | :--- |
| **CR-01** | **H-01** | **H5** Prevención de errores · **H9** Recuperación de errores | `#btn-confirmar` · `#estado` (`src/interaccion.js`) | En pruebas de valores límite (`total > $10.00`), el botón `#btn-confirmar` no previene el error: permanece habilitado con el texto «Confirmar y pagar · $11.00» y recién al pulsarlo salta el estado de error, sin indicar cuánto saldo falta. | 4 | 4 | 4 | **4 (Crítico)** | Bloquear `#btn-confirmar` automáticamente cuando `total > saldo` y mostrar en `#estado` el desglose: `Saldo insuficiente: te faltan $X.XX`. |
| **CR-02** | **H-02** | **H1** Visibilidad del estado · **H6** Reconocer antes que recordar | `#buscar-producto` · `#lista-catalogo` (`src/interaccion.js`) | Si se ingresa un término sin resultados en el buscador (ej. «empanada»), la lista `#lista-catalogo` queda vacía sin ningún mensaje de estado (`0 resultados`), haciendo parecer que el catálogo falló. | 3 | 3 | 3 | **3 (Mayor)** | Mostrar un mensaje accesible (`role="status"`) indicando que no hay coincidencias para el término buscado y un botón para restablecer el catálogo. |
| **CR-03** | **H-03** | **H3** Control y libertad · **H5** Prevención de errores | `#btn-cancelar` (`src/interaccion.js`) | Cancelar el pedido pagado no solicita confirmación y ocasiona que el estudiante pierda su turno `#A24` (al volver a confirmar pasa a `#A25`). | 3 | 3 | 3 | **3 (Mayor)** | Incorporar confirmación de seguridad antes de cancelar, advirtiendo la pérdida del número de turno `#A24`. |
| **CR-04** | **H-07** | **H7** Flexibilidad y eficiencia de uso | `#buscar-producto` · `.filtros` (`src/index.html`) | Falta un botón `× Limpiar` o soporte para `Escape` que devuelva el buscador y las categorías a su estado inicial en un solo paso. | 2 | 2 | 2 | **2 (Menor)** | Añadir botón `Limpiar` junto al campo de búsqueda y atajo `Escape`. |
| **CR-05** | **H-08** | **H8** Diseño estético y minimalista | `.productos small` (`src/estilos.css`) | El tamaño `0.8125rem` y color `#6B625C` de los detalles de producto presentan legibilidad mejorable en pantallas móviles pequeñas (320 px). | 2 | 1 | 1 | **1 (Cosmético)** | Ajustar `--texto-sec` a `#524944` y tamaño a `0.875rem`. |

---

## 4. Síntesis del Evaluador

- **Total de hallazgos reportados:** 5 (`1 Crítico [Sev. 4]`, `2 Mayores [Sev. 3]`, `1 Menor [Sev. 2]`, `1 Cosmético [Sev. 1]`).
- **Conclusión desde Testing:** Los 10 casos de prueba automatizados del APE 5 verificaron el camino feliz y el doble clic, pero la inspección heurística demuestra que las condiciones de frontera en la interfaz (búsqueda sin coincidencias `H-02` y exceso de presupuesto `H-01`) carecen de prevención y retroalimentación adecuadas.
