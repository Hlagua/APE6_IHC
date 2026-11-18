# Evaluación Heurística Individual — Melany Saleth Cevallos Goyes
## Método 1: Inspección de las 10 Heurísticas de Nielsen (1994, 1995) · Caso **CaféU**

- **Evaluadora:** Melany Saleth Cevallos Goyes ([@SalyC15](https://github.com/SalyC15))
- **Correo:** `mcevallos8901@uta.edu.ec`
- **Rol en el equipo:** Desarrollador Front-End (Vistas, componentes UI, diseño, wizard)
- **Fecha de inspección:** 18/11/2026
- **Prototipo inspeccionado:** `src/index.html` + `src/estilos.css` + `src/interaccion.js` + `src/api.js` (viewports 320 × 720, 360 × 800 y 1366 × 768 px)

---

## 1. Escala de Severidad y Criterios de Ponderación (Nielsen, 1995)

- **1 = Cosmético:** Problema visual o tipográfico leve que no afecta el cumplimiento de la tarea.
- **2 = Menor:** Genera fricción leve o pasos adicionales, pero el usuario se recupera rápido.
- **3 = Mayor:** Dificulta la comprensión del estado o provoca errores de interacción importantes.
- **4 = Crítico:** Induce a fallo en la tarea principal o impide diagnosticar el problema sin ayuda.

*Ponderación:* **Frecuencia (F: 1–4)**, **Impacto (I: 1–4)** y **Persistencia (P: 1–4)**.

---

## 2. Revisión Sistemática de las 10 Heurísticas de Nielsen (1994)

| Código | Heurística de Nielsen (1994) | Estado en CaféU | Observaciones de la inspección independiente |
| :---: | :--- | :---: | :--- |
| **H1** | Visibilidad del estado del sistema | ❌ Con fallos mayores | Cuando el estudiante escribe en `#buscar-producto` un término que no existe (ej. «empanada» o «té»), la cuadrícula `#lista-catalogo` queda completamente vacía sin mostrar un mensaje de «No se encontraron productos». |
| **H2** | Relación entre el sistema y el mundo real | ✅ Cumple | La metáfora de «Mi pedido», «En bandeja» y «Tarjeta universitaria» corresponde al flujo real de la cafetería en FISEI-UTA. |
| **H3** | Control y libertad del usuario | ⚠️ Con hallazgos | Para quitar un producto agregado por error, el usuario no tiene un botón directo en la tarjeta «Revisa tu pedido», sino que debe buscarlo de nuevo en el catálogo superior. |
| **H4** | Consistencia y estándares | ✅ Cumple | Uso consistente de etiquetas `<button type="button">`, colores semánticos (`--exito`, `--aviso`, `--error`) y foco visible `:focus-visible`. |
| **H5** | Prevención de errores | ❌ Con fallos críticos | El botón `#btn-confirmar` sigue viéndose habilitado (`background: var(--primario)`) incluso cuando el usuario agrega productos por `$11.00` o `$12.00` superando su saldo de `$10.00`. |
| **H6** | Reconocer antes que recordar | ⚠️ Con hallazgos | Si el usuario filtró el catálogo y luego revisa «Mi pedido», no puede quitar unidades desde la lista `ul#lista-pedido` ni reconoce qué filtro dejó activo si la lista quedó vacía. |
| **H7** | Flexibilidad y eficiencia de uso | ⚠️ Con hallazgos | El campo `#buscar-producto` no incluye un botón visible `× Limpiar` ni responde a la tecla `Escape` para restablecer la vista completa con un toque. |
| **H8** | Diseño estético y minimalista | ⚠️ Con hallazgos | En resoluciones pequeñas (320 × 720 px), los textos `<small>` (`0.8125rem`, color `#6B625C`) quedan demasiado juntos al nombre del producto y pierden jerarquía visual. |
| **H9** | Ayudar a reconocer, diagnosticar y recuperarse de errores | ⚠️ Con hallazgos | El mensaje de error al superar `$10.00` dice que el total supera el saldo, pero no indica el monto exacto que excede (`Te pasaste por $X.XX`). |
| **H10** | Ayuda y documentación | ✅ Cumple | La frase guía bajo «Agregar del menú rápido» orienta el uso del filtro. |

---

## 3. Hallazgos Individuales Registrados por Melany Cevallos (`@SalyC15`)

| ID Individual | ID Consolidado | Heurística violada | Componente / Ubicación | Descripción técnica del problema | F | I | P | Severidad (1–4) | Propuesta de solución |
| :---: | :---: | :--- | :--- | :--- | :-: | :-: | :-: | :---: | :--- |
| **MC-01** | **H-01** | **H5** Prevención de errores · **H9** Recuperación de errores | `#btn-confirmar` · `#estado` (`src/interaccion.js`) | Cuando el total acumulado en `#total` supera el saldo disponible (`$10.00`), el botón «Confirmar y pagar» conserva su estilo primario activo, invitando al usuario a hacer clic en una acción que fallará. Además, el aviso de error no muestra cuánto dinero falta. | 4 | 4 | 3 | **4 (Crítico)** | Deshabilitar `#btn-confirmar` en cuanto `total > saldo` y mostrar en vivo un aviso preventivo con la diferencia exacta (`Excedes tu saldo por $X.XX`). |
| **MC-02** | **H-02** | **H1** Visibilidad del estado · **H6** Reconocer antes que recordar | `#lista-catalogo` · `#buscar-producto` (`src/interaccion.js`) | Al escribir una búsqueda sin coincidencias en `#buscar-producto`, `listaCatalogo.innerHTML` queda vacío (`""`). El contenedor colapsa sin informar «0 resultados» ni ofrecer un botón para volver a ver todo el menú. | 3 | 3 | 3 | **3 (Mayor)** | Insertar un estado vacío explícito con texto `No hay productos que coincidan con «...»` y un botón `Mostrar todo el menú`. |
| **MC-03** | **H-04** | **H6** Reconocer antes que recordar · **H3** Control y libertad | `#lista-pedido` (`src/index.html`, `src/interaccion.js`) | En la tarjeta «Revisa tu pedido», cada `<li>` muestra el nombre y subtotal pero carece de un botón `− Quitar` propio. Si el usuario filtró el catálogo por otra categoría, no ve cómo restar el producto excedente. | 3 | 3 | 3 | **3 (Mayor)** | Renderizar un botón `−` o `Quitar` dentro de cada fila de `#lista-pedido` para modificar el pedido sin depender del catálogo superior. |
| **MC-04** | **H-07** | **H7** Flexibilidad y eficiencia de uso | `.campo-busqueda` (`src/index.html`, `src/interaccion.js`) | No hay un control rápido para limpiar simultáneamente el texto de búsqueda y el filtro de categoría (ni soporte para tecla `Escape`), obligando a borrar letra por letra en móvil. | 2 | 2 | 2 | **2 (Menor)** | Añadir botón `Limpiar filtro` junto al buscador y manejador de tecla `Escape`. |
| **MC-05** | **H-08** | **H8** Diseño estético y minimalista | `.productos small` · `.item-catalogo__info small` (`src/estilos.css`) | En el viewport de 320 px, los subtítulos `<small>` en `#6B625C` a `0.8125rem` tienen bajo contraste visual frente al fondo `#FAF7F3` de las tarjetas del catálogo y poco espacio vertical. | 2 | 1 | 1 | **1 (Cosmético)** | Oscurecer `--texto-sec` a `#524944`, subir tamaño a `0.875rem` y agregar `margin-top: 0.15rem`. |

---

## 4. Síntesis de la Evaluadora

- **Total de hallazgos reportados:** 5 (`1 Crítico [Sev. 4]`, `2 Mayores [Sev. 3]`, `1 Menor [Sev. 2]`, `1 Cosmético [Sev. 1]`).
- **Conclusión desde Front-End:** Pasar todas las pruebas de diseño adaptable (`scrollWidth === innerWidth` en 320–1366 px) garantiza que la interfaz **no se desborde**, pero no garantiza que el usuario comprenda los estados vacíos del buscador (`H-02`) ni que prevenga excesos de saldo antes de pulsar pagar (`H-01`).
