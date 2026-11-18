# APE 6 · Fase 3.1: Ajuste Post-Pilotaje y Protocolo de Reinicio (F5)
## Proyecto **CaféU** · Grupo 5 · Interacción Humano-Computador (IHC)

- **Responsable:** Alison Marcela Cobos Taco ([@Itsuna18](https://github.com/Itsuna18)) · Rol: Desarrollador Back-End
- **Revisión cruzada:** Carlos Giovanni Ramos Jácome ([@carlitosgiovanniramos](https://github.com/carlitosgiovanniramos))
- **Fecha:** 18/11/2026

---

## 1. Continuidad desde las Fases 1 (Planificación) y 2 (Pilotaje)

En el **APE 5**, el Grupo 5 implementó y verificó técnicamente la pantalla **«Mi pedido → Confirmar y pagar»** de **CaféU**, logrando **0 px de desborde horizontal** en 4 viewports (320, 360, 768 y 1366 px) y **10/10 pruebas automatizadas aprobadas**.

Durante las **Fases 1 (Planificación)** y **2 (Pilotaje)** del **APE 6**, pusimos a prueba nuestros instrumentos de evaluación para responder a la pregunta central del laboratorio:

> **«¿Una interfaz que funciona técnicamente puede ser una mala interfaz?»** *(Verificación vs. Validación — Boehm, 1984).*

### Brechas detectadas en el Pilotaje (Fase 2)

| ID Brecha | Problema observado en el pilotaje (Fase 2) | Impacto metodológico | Ajuste aplicado para la Fase 3 |
| :---: | :--- | :--- | :--- |
| **BP-01** | Solo se evaluaron el pago directo (`T1`) y la cancelación (`T2`) sobre una bandeja estática de $4.25. No se evaluaron **buscadores, filtros de productos ni la prevención de errores cuando el pedido supera el saldo de $10.00**. | El pilotaje daba una falsa impresión de ausencia de errores porque no exigía buscar ítems ni enfrentar condiciones de borde (saldo insuficiente o búsqueda vacía). | Se incorporó el módulo de **Catálogo Rápido con Buscador y Filtros por Categoría** en `src/index.html` y `src/api.js`, y se diseñó la **Tarea de Refuerzo T3**. |
| **BP-02** | Al presionar `F5` en el navegador entre el participante piloto y el siguiente, `sessionStorage` conservaba el estado `confirmado` y el correlativo `#A25`, alterando las condiciones iniciales. | Contaminación del estado experimental entre sesiones (el participante 2 veía el pedido ya pagado o con saldo distinto de $10.00). | Se definió el **Protocolo de Reinicio de Estado (`F5` + `Alt+R` / botón `#btn-reiniciar-lab`)** que invoca `PedidoAPI.reiniciar()`, limpia los filtros y recarga el DOM limpio. |
| **BP-03** | La hoja de observación no diferenciaba entre **errores críticos** (impiden completar la tarea o requieren intervención) y **errores no críticos** (desvíos, clics en botones sin efecto o vacilaciones superadas por el propio usuario). | Dificultad para calcular con precisión la métrica de **Eficacia** bajo **ISO 9241-11:2018**. | Se actualizaron las plantillas `resultados/P1.md` a `P3.md` separando explícitamente errores críticos y no críticos por tarea. |

---

## 2. Escenarios y Tareas Definitivas (incluyendo Tarea de Refuerzo T3)

| ID | Tipo de Tarea | Función crítica evaluada | Consigna leída al participante (Think-Aloud) | Meta de tiempo | Criterio de éxito autónomo |
| :---: | :--- | :--- | :--- | :---: | :--- |
| **T1** | Flujo principal (del pilotaje) | Revisión de datos clave (`<dl>`), confirmación de pago único y lectura de estado (`role="status"`). | *«Tienes 10 minutos entre clases. Ya tienes en tu bandeja 1 Café Americano ($1.50) y 1 Sánduche ($2.75). Confirma tu compra y dime en voz alta tu número de pedido, cuánto te quedó de saldo y en dónde debes retirarlo.»* | **≤ 20 s** | Confirma el pago una sola vez y verbaliza `#A24`, saldo `$5.75` y `Edificio central (10 min)` sin ayuda. |
| **T2** | Recuperación de errores (del pilotaje) | Reversibilidad de la acción (`Cancelar pedido`), verificación de reembolso y re-confirmación. | *«Te acabas de dar cuenta de que tu siguiente clase cambió de aula y quieres cancelar el pedido que acabas de pagar. Anula el pedido, verifica si te devolvieron tu dinero completo y vuelve a dejar el pedido confirmado.»* | **≤ 15 s** | Cancela el pedido, comprueba que el saldo regresó a `$10.00` y vuelve a confirmar (`#A25`) sin ayuda. |
| **T3** | **Tarea de Refuerzo (Ajuste Post-Pilotaje)** | **Buscador en vivo, filtros por categoría, edición de pedido y prevención de error por saldo insuficiente (`> $10.00`).** | *«Con la sesión reiniciada (saldo $10.00, pedido base $4.25), un compañero te pide usar el buscador o los filtros del menú para buscar un postre o bebida sin lactosa, agregar productos hasta pasar de los $10.00 de tu tarjeta, comprobar qué ocurre al intentar pagar y luego ajustar el pedido quitando lo necesario para que el pago sí se procese.»* | **≤ 35 s** | Utiliza el buscador/filtros, detecta el bloqueo por saldo insuficiente al superar `$10.00`, reduce ítems hasta `≤ $10.00` y confirma el pago sin asistencia del moderador. |

---

## 3. Protocolo de Reinicio de Estado (`F5`) entre Sesiones

Dado que `src/api.js` persiste el estado del pedido en `sessionStorage` (`ape6_cafeu_pedido_v1`) para simular una sesión real de navegador, una recarga estándar (`F5`) por sí sola **mantiene el estado previo** (requisito de persistencia del APE 5). Por ello, entre cada participante (`P1`, `P2`, `P3`) y antes de iniciar la **Tarea de Refuerzo T3**, el **Soporte Técnico / Cronometrista** ejecuta el siguiente procedimiento obligatorio de 3 pasos:

1. **Limpieza de estado y almacenamiento:** Presionar el botón **`Reiniciar sesión (F5)`** ubicado en la barra superior del prototipo (o el atajo de teclado `Alt + R`), el cual ejecuta `PedidoAPI.reiniciar()` eliminando la clave `ape6_cafeu_pedido_v1` de `sessionStorage`, limpia el campo `#buscar-producto`, restablece el filtro de categoría a `Todos` y ejecuta la recarga limpia (`F5` / `location.reload()`).
2. **Verificación visual de línea base (Checklist de 5 puntos):**
   - [x] Saldo de tarjeta universitaria en **`$10.00`**.
   - [x] Bandeja con los 2 productos base (`1 × Café Americano $1.50` + `1 × Sánduche $2.75` = **`$4.25`**).
   - [x] Estado del pedido en `pendiente`: *«Aún no confirmas tu pedido. No se ha cobrado nada.»*
   - [x] Correlativo interno reiniciado para asignar **`#A24`** al primer cobro.
   - [x] Buscador vacío y filtro activo en **«Todos»** (6 productos visibles en catálogo).
3. **Reinicio del cronómetro:** El Cronometrista pone el temporizador en `00:00.0` antes de que el Moderador lea la consigna de la tarea.
