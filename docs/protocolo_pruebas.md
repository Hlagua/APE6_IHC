# Protocolo de Pruebas de Usabilidad (Think-Aloud) y Cuestionario SUS · APE 6
## Caso **CaféU** · Grupo 5 · Interacción Humano-Computador (IHC)

- **Autor:** Carlos Giovanni Ramos Jácome ([@carlitosgiovanniramos](https://github.com/carlitosgiovanniramos)), Tester
- **Revisión cruzada:** Henry Daniel Lagua Flores ([@Hlagua](https://github.com/Hlagua)), QA / Arquitecto
- **Estándares aplicados:** ISO 9241-11:2018 (Eficacia, Eficiencia y Satisfacción), Protocolo *Think-Aloud* (Ericsson & Simon, 1993; Nielsen, 1993) y *System Usability Scale* (Brooke, 1996).

---

## 1. Asignación de los 4 Roles del Laboratorio

En cada sesión individual con los participantes externos (`P1`, `P2`, `P3`), el equipo mantiene una estructura fija de 4 roles para evitar sesgos de conducción:

| Rol en el Laboratorio | Integrante Responsable | Funciones durante la sesión |
| :--- | :--- | :--- |
| **1. Moderador(a)** | **Melany Saleth Cevallos Goyes** (`@SalyC15`) | Recibe al participante, explica el consentimiento informado, lee textualmente cada escenario (`T1`, `T2`, `T3`) sin mencionar los nombres de los botones y recuerda pensar en voz alta (*«¿Qué estás buscando ahora?»*). |
| **2. Usuario (Participante)** | **Participante externo (`P1`, `P2`, `P3`)** | Estudiante externo al Grupo 5 que no participó en el diseño de CaféU. Ejecuta las 3 tareas verbalizando su razonamiento y responde el cuestionario SUS al finalizar. |
| **3. Cronometrista** | **Carlos Giovanni Ramos Jácome** (`@carlitosgiovanniramos`) | Mide en segundos el tiempo exacto de cada tarea (desde el fin de la lectura de la consigna hasta la confirmación verbal del usuario) y aplica el cuestionario SUS. |
| **4. Observador(a) (y Soporte F5)** | **Alison Marcela Cobos Taco** (`@Itsuna18`) y **Henry Daniel Lagua Flores** (`@Hlagua`) | Alison registra las citas textuales *Think-Aloud*, vacilaciones y conteo de errores críticos / no críticos; Henry ejecuta el protocolo de reinicio `F5` (`PedidoAPI.reiniciar()`) antes de cada participante y antes de `T3`. |

---

## 2. Definición Operativa de Errores y Éxito (ISO 9241-11:2018)

- **Éxito autónomo (1 / Sí):** El participante logra el objetivo de la tarea por sí mismo, sin intervención ni pistas del moderador.
- **Fallo / Éxito con ayuda (0 / No):** El participante abandona la tarea, da por terminada una acción incompleta creyendo que ya acabó, o requiere una pista explícita del moderador para destrabarse.
- **Error crítico:** Acción o bloqueo que impide completar la tarea de forma autónoma o lleva a un estado erróneo no recuperado por el propio participante.
- **Error no crítico:** Desvío navegacional, clic sobre un botón que produce rechazo (ej. intentar pagar con saldo insuficiente porque el botón seguía activo), confusión ante lista vacía o vacilación mayor a 3 segundos que el participante logra superar por sí mismo.

---

## 3. Tareas Evaluadas y Metas de Eficiencia

| Tarea | Nombre | Consigna textual (sin revelar etiquetas de la UI) | Meta (s) | Estado inicial requerido |
| :---: | :--- | :--- | :---: | :--- |
| **T1** | Confirmación y verificación de cobro único | *«Tienes 10 minutos entre clases. Ya tienes en tu bandeja 1 Café Americano ($1.50) y 1 Sánduche ($2.75). Confirma tu compra y dime en voz alta tu número de pedido, cuánto te quedó de saldo y en dónde debes retirarlo.»* | **20.0 s** | Reinicio `F5` limpio: Saldo `$10.00`, total `$4.25`, estado `pendiente`, correlativo `#A24`. |
| **T2** | Cancelación, reembolso y re-confirmación | *«Te acabas de dar cuenta de que tu siguiente clase cambió de aula y quieres cancelar el pedido que acabas de pagar. Anula el pedido, verifica si te devolvieron tu dinero completo y vuelve a dejar el pedido confirmado.»* | **15.0 s** | Continuación inmediata de `T1`: Pedido `#A24` `confirmado`, saldo `$5.75`. |
| **T3** | **Tarea de Refuerzo Post-Pilotaje:** Buscador, filtro y límite de saldo (`$10.00`) | *«Con la sesión reiniciada (saldo $10.00, pedido base $4.25), un compañero te pide usar el buscador o los filtros del menú para buscar un postre o bebida sin lactosa, agregar productos hasta pasar de los $10.00 de tu tarjeta, comprobar qué ocurre al intentar pagar y luego ajustar el pedido quitando lo necesario para que el pago sí se procese.»* | **35.0 s** | Reinicio `F5` limpio (`Alt+R`): Saldo `$10.00`, total `$4.25`, buscador vacío, filtro `Todos`. |

---

## 4. Cuestionario SUS (*System Usability Scale* — Brooke, 1996)

Al finalizar las 3 tareas, el participante califica los 10 ítems en escala Likert de **1 (Totalmente en desacuerdo)** a **5 (Totalmente de acuerdo)**:

1. Creo que me gustaría usar este sistema de pedidos con frecuencia.
2. Encontré el sistema innecesariamente complejo.
3. Pensé que el sistema era fácil de usar.
4. Creo que necesitaría el apoyo de un técnico para poder utilizar este sistema.
5. Encontré que las diversas funciones de este sistema estaban bien integradas.
6. Pensé que había demasiada inconsistencia en este sistema.
7. Me imagino que la mayoría de las personas aprenderían a usar este sistema muy rápidamente.
8. Encontré el sistema muy engorroso de usar.
9. Me sentí muy seguro(a) usando el sistema.
10. Necesité aprender muchas cosas antes de poder manejarme con este sistema.

### Fórmula de cálculo SUS (0 a 100):
$$\text{SUS} = 2.5 \times \left( \sum_{i \in \{1,3,5,7,9\}} (R_i - 1) + \sum_{j \in \{2,4,6,8,10\}} (5 - R_j) \right)$$

- **Referencia de la industria (Brooke, 1996; Sauro & Lewis, 2016):** Puntaje promedio estándar = **68.0 puntos** (`< 68.0` = bajo el promedio / requiere mejoras prioritarias; `≥ 68.0` = aceptable/bueno; `≥ 80.3` = excelente).
