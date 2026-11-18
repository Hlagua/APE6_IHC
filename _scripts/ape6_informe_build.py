"""Generador del Informe Final del APE 6 en formato oficial de la Universidad Técnica de Ambato (UTA).

Usa la plantilla oficial de guía práctica UTA y docx_lib.py para generar:
- 06_documento/APE6_Informe_Final.docx
- 06_documento/APE6_Informe_Final.pdf (exportado automáticamente con Microsoft Word)
"""
import os, sys, subprocess
sys.path.insert(0, 'C:/Users/henry/Documents/UTA/IHC/APE4/_scripts')
from docx_lib import Doc, TNR, run
from PIL import Image, ImageDraw

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/') + '/'
EV = REPO + 'evidencias/'
DOC = REPO + '06_documento/'
W = os.environ.get('TEMP', '/tmp').replace('\\', '/') + '/ape6/informe/'
os.makedirs(W, exist_ok=True)
os.makedirs(DOC, exist_ok=True)
REPO_URL = 'https://github.com/Hlagua/APE6_IHC'


def fila(archivos, dest, alto=760, gap=24, pad=18):
    ims = []
    for a in archivos:
        im = Image.open(EV + a).convert('RGB')
        ims.append(im.resize((int(im.width * alto / im.height), alto)))
    lienzo = Image.new('RGB', (sum(i.width for i in ims) + gap * (len(ims) - 1) + 2 * pad, alto + 2 * pad), 'white')
    x = pad
    for im in ims:
        lienzo.paste(im, (x, pad))
        ImageDraw.Draw(lienzo).rectangle([x - 1, pad - 1, x + im.width, pad + im.height], outline='#9aa3a7', width=2)
        x += im.width + gap
    lienzo.save(dest)
    return dest


F_FLUJO = fila(['T1-inicial-360.png', 'T1-confirmado-360.png'], W + 'fig_flujo.png', alto=740)
F_HALLAZGOS = fila(['T3-hallazgo-H01-saldo.png', 'T3-hallazgo-H02-buscador.png'], W + 'fig_hallazgos.png', alto=740)

d = Doc(W)
E = d.E
out = E[0:3]
out.append(d.replace_t(
    E[3],
    'Refactorización con SOLID, Clean Architecture y Patrones Creacionales – Tipo B: Venta de motocicletas',
    'APE 6. Evaluación y validación · caso CaféU: Heurísticas de Nielsen, Think-Aloud, ISO 9241-11, SUS y Triangulación · Grupo 5'
))
out.append(E[4])
out.append(d.replace_t(E[5], 'Sexto - A', 'Quinto - A'))
out.append(E[6])
for n in ['Cevallos Goyes Melany Saleth', 'Cobos Taco Alison Marcela', 'Ramos Jacome Carlos Giovanni']:
    out.append('<w:p><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/><w:ind w:left="3540"/><w:rPr>%s</w:rPr></w:pPr>%s</w:p>' % (TNR, run(n)))
out.append(d.replace_t(E[7], 'Patrones de Software', 'Interacción Humano / Computador'))
out.append(d.replace_t(E[8], 'Ing. Alex Maigua, Mg.', 'Ing. Mg. José Rubén Caiza Caizabuano'))
# Omitir E[11] ('PP') y E[12] ('YY'), que son textos ocultos de la plantilla base
out += E[9:11] + E[13:16]
out.append(d.listpara('Elección de métodos apropiados de evaluación y validación para un contexto de la aplicación de prototipos (evaluación formativa completa del prototipo web adaptable CaféU para contrastar Verificación vs. Validación según Boehm, 1984).'))
out += E[17:19]
for s in [
    'Ejecutar el ajuste post-pilotaje incorporando la Tarea de Refuerzo T3 (buscador, filtros por categoría y límite de saldo de $10.00) y el protocolo de reinicio de estado (F5 / PedidoAPI.reiniciar()) entre sesiones.',
    'Aplicar de forma independiente el Método 1 (Evaluación Heurística de Nielsen, 1994 con severidad 1–4 de Nielsen, 1995) por los cuatro integrantes y el Método 2 (Prueba de Usabilidad Think-Aloud + Cuestionario SUS con 3 participantes externos P1–P3).',
    'Calcular las métricas de Eficacia, Eficiencia y Satisfacción (ISO 9241-11:2018 y SUS frente al estándar de 68.0), construir la Matriz Consolidada de Hallazgos, la Triangulación Metodológica, los Criterios Técnicos de Mejora (WCAG 2.1 / ISO / Nielsen) y el Backlog trazable en GitHub Issues.'
]:
    out.append(d.bullet(s))
out += E[21:26]
# En 2.2 Modalidad queda 'Presencial' (E[23]) y en 2.3 Tiempo de duración 'Presenciales: 8' (guía oficial APE 6)
out.append(E[26].replace('<w:t>4</w:t>', '<w:t>8</w:t>'))
out += E[27:30]
for s in [
    '**Acciones previas:** ingresar al aula virtual de la asignatura; generar una base de conocimiento debidamente documentada sobre los métodos de evaluación y validación de prototipos; aplicar los métodos seleccionados en casos prácticos y desarrollar un documento sobre sus aplicaciones y resultados.',
    '**Paso 1.** Revisar el material entregado por el docente sobre la aplicación de métodos de evaluación y validación.',
    '**Paso 2.** Aplicar los métodos seleccionados en casos prácticos (Evaluación Heurística individual y Prueba de Usabilidad Think-Aloud con usuarios sobre CaféU).',
    '**Paso 3.** Desarrollar una presentación sobre el desarrollo de los métodos aplicados (presentacion/index.html).',
    '**Paso 4.** Elaborar las conclusiones y emitir criterios técnicos con el fin de mejorar los métodos y la interfaz evaluada.',
    '**Paso 5.** Subir el archivo a la plataforma dentro de la fecha indicada.'
]:
    out.append(d.listpara(s))
out += E[33:37]
for s in [
    'Inteligencia artificial, TAC',
    'Computadora y navegador Chromium con emulación móvil (360 × 800 px) y escritorio (1366 × 768 px)',
    'Herramientas Ofimáticas y generador documental UTA',
    'Aula virtual e Internet',
    'GitHub: Repositorio Hlagua/APE6_IHC con ramas, commits individuales por autor, Pull Requests e Issues del Backlog'
]:
    out.append(d.bullet(s, num=7))
out.append(E[41])
for k, v in {42: True, 43: False, 44: True, 45: False, 46: False, 47: True}.items():
    out.append(d.check(E[k], v))
out += E[48:51]
for s in [
    'Fase 3 (Aplicación y Análisis): 1. Ajuste post-pilotaje (Tarea de refuerzo T3 y reinicio F5) · 2. Evaluación Heurística Independiente (Severidad 1–4) · 3. Prueba de Usabilidad Think-Aloud (P1–P3, 4 roles y SUS) · 4. Consolidación de Métricas ISO 9241-11:2018.',
    'Fase 4 (Priorización y Cierre): 5. Matriz Consolidada de Hallazgos (H-01 a H-08) · 6. Triangulación Metodológica · 7. Criterios Técnicos de Mejora (C-01 a C-08) · 8. Backlog en GitHub Issues (P1–P4) y Conclusiones (Boehm, 1984).'
]:
    out.append(d.actividad(s))
out += E[58:60]

R = []
R.append(d.para(
    'El presente informe documenta el desarrollo completo de la Guía **APE 6 (Evaluación y validación)** por el **Grupo 5** sobre el prototipo web adaptable **CaféU** («Mi pedido → Confirmar y pagar»), continuando el trabajo realizado en el APE 5 y en las Fases 1 (Planificación) y 2 (Pilotaje). El objetivo central es responder con evidencia empírica y analítica a la pregunta del laboratorio: **«¿Una interfaz que funciona técnicamente puede ser una mala interfaz?»** (Verificación vs. Validación — Boehm, 1984).'
))
R.append(d.table([2100, 1500, 1750, 1650, 1144], [
    ['Integrante', 'Rol en el Grupo', 'Usuario GitHub', 'Rama de Trabajo', 'PR · Issue'],
    ['Alison Marcela Cobos Taco', 'Desarrollador Back-End', '@Itsuna18', 'feat/ajuste-post-pilotaje-backend', 'PR #9 · #5'],
    ['Melany Saleth Cevallos Goyes', 'Desarrollador Front-End', '@SalyC15', 'feat/interfaz-refuerzo-frontend', 'PR #10 · #6'],
    ['Carlos Giovanni Ramos Jácome', 'Tester', '@carlitosgiovanniramos', 'test/usabilidad-usuarios-sus', 'PR #11 · #7'],
    ['Henry Daniel Lagua Flores', 'QA / Arquitecto', '@Hlagua', 'docs/triangulacion-cierre-qa', 'PR #12 · #8'],
]))
R.append(d.link_para('Repositorio oficial del APE 6 en GitHub: ', REPO_URL))

# Sección 1
R.append(d.sub('1. Fase 3.1: Ajuste Post-Pilotaje y Protocolo de Reinicio de Estado (F5)'))
R.append(d.para(
    'Al revisar los instrumentos aplicados en la Fase 2 (Pilotaje), el equipo identificó tres brechas metodológicas: (1) solo se habían probado el pago directo (T1) y la cancelación (T2) sobre un pedido estático de $4.25, dejando sin evaluar funciones críticas como el **buscador en tiempo real, los filtros por categoría y la prevención de errores cuando el total supera el saldo disponible de $10.00**; (2) al recargar la página con F5 entre participantes, sessionStorage mantenía el pedido pagado o el correlativo #A25; y (3) faltaba separar errores críticos y no críticos en las hojas de registro.'
))
R.append(d.table([900, 1900, 3244, 950, 1150], [
    ['Tarea', 'Función Evaluada', 'Consigna Leída al Participante (Think-Aloud)', 'Meta (s)', 'Estado Inicial'],
    ['T1', 'Confirmación de pedido y cobro único (#A24)', 'Confirmar la compra de 1 Café Americano ($1.50) y 1 Sánduche ($2.75) e indicar en voz alta el número de pedido, saldo restante y lugar de retiro.', '≤ 20.0 s', 'Reinicio F5: Saldo $10.00, base $4.25'],
    ['T2', 'Cancelación, reembolso y re-confirmación', 'Anular el pedido recién pagado por cambio de aula, comprobar que se devolvieron los $4.25 a la tarjeta y volver a dejar el pedido confirmado.', '≤ 15.0 s', 'Pedido #A24 confirmado, saldo $5.75'],
    ['T3 (Refuerzo)', 'Buscador, filtro por categoría y límite de saldo ($10.00)', 'Con sesión reiniciada, buscar un postre o bebida sin lactosa, agregar ítems hasta superar los $10.00, observar qué ocurre al intentar pagar y ajustar el pedido para lograr pagar.', '≤ 35.0 s', 'Reinicio F5: Saldo $10.00, filtros limpios'],
]))
R.append(d.para(
    '**Protocolo de Reinicio entre Sesiones (F5 / Alt+R):** Se implementó el control #btn-reiniciar-lab («Reiniciar sesión (F5)») conectado a PedidoAPI.reiniciar(), que borra la clave ape6_cafeu_pedido_v1 de sessionStorage, limpia el campo #buscar-producto, restablece el filtro «Todos» y garantiza que cada participante (P1, P2 y P3) inicie con saldo de **$10.00**, pedido base de **$4.25** y turno **#A24**.'
))
R.append(d.figure(F_FLUJO, 5.2, 'Figura 1. Prototipo CaféU tras el ajuste post-pilotaje a 360 px: (izquierda) estado inicial reiniciado con F5 y catálogo filtrable; (derecha) pedido #A24 confirmado y pagado en T1.'))

# Sección 2
R.append(d.sub('2. Fase 3.2: Método 1 — Evaluación Heurística Independiente (Severidad 1–4)'))
R.append(d.para(
    'Cada integrante inspeccionó el prototipo por separado aplicando las **10 heurísticas de Nielsen (1994)** y calificó la severidad de **1 a 4** (1 = Cosmético, 2 = Menor, 3 = Mayor, 4 = Crítico) ponderando **Frecuencia, Impacto y Persistencia** (Nielsen, 1995). Las evidencias completas se encuentran en resultados/heuristica-*.md.'
))
R.append(d.table([1950, 1350, 2300, 2544], [
    ['Evaluador(a)', 'Rol', 'Archivo en el Repositorio', 'Hallazgos Detectados Individualmente (Severidad)'],
    ['Alison Cobos (@Itsuna18)', 'Back-End', 'resultados/heuristica-alison-cobos.md', 'AC-01 → H-01 (Sev. 4), AC-02 → H-03 (Sev. 3), AC-03 → H-04 (Sev. 3), AC-04 → H-05 (Sev. 2)'],
    ['Melany Cevallos (@SalyC15)', 'Front-End', 'resultados/heuristica-melany-cevallos.md', 'MC-01 → H-01 (Sev. 4), MC-02 → H-02 (Sev. 3), MC-03 → H-04 (Sev. 3), MC-04 → H-07 (Sev. 2), MC-05 → H-08 (Sev. 1)'],
    ['Carlos Ramos (@carlitosgiovanniramos)', 'Tester', 'resultados/heuristica-carlos-ramos.md', 'CR-01 → H-01 (Sev. 4), CR-02 → H-02 (Sev. 3), CR-03 → H-03 (Sev. 3), CR-04 → H-07 (Sev. 2), CR-05 → H-08 (Sev. 1)'],
    ['Henry Lagua (@Hlagua)', 'QA / Arquitecto', 'resultados/heuristica-henry-lagua.md', 'HL-01 → H-01 (Sev. 4), HL-02 → H-02 (Sev. 3), HL-03 → H-03 (Sev. 3), HL-04 → H-05 (Sev. 2), HL-05 → H-08 (Sev. 1)'],
]))

# Sección 3
R.append(d.sub('3. Fase 3.3: Método 2 — Prueba de Usabilidad con Usuarios (Think-Aloud y SUS)'))
R.append(d.para(
    'Se ejecutaron tres sesiones individuales con participantes externos (P1, P2 y P3) que no diseñaron el prototipo, bajo consentimiento informado anonimizado (docs/consentimiento_informado.md) y con los **4 roles del laboratorio**: Moderadora (Melany Cevallos), Cronometrista (Carlos Ramos), Observadora Think-Aloud (Alison Cobos) y Soporte Técnico/F5 (Henry Lagua). Los registros detallados constan en resultados/P1.md, resultados/P2.md y resultados/P3.md.'
))
R.append(d.table([750, 1200, 1200, 1200, 950, 2844], [
    ['Part.', 'T1 (Meta 20s)', 'T2 (Meta 15s)', 'T3 (Meta 35s)', 'Puntaje SUS', 'Citas Textuales Think-Aloud y Comportamiento Observado'],
    ['P1', '16.0 s (Sí · 0/0)', '17.0 s (Sí · 0/1)', '52.0 s (Sí · 0/2)', '80.0 / 100', 'En T1 preguntó en qué ventanilla presentar #A24 (H-06). En T2 se sorprendió de que Cancelar anulara de golpe y cambiara #A24 a #A25 (H-03). En T3 pulsó pagar con $11.50 porque el botón seguía activo (H-01) y buscó quitar ítems abajo en la lista (H-04).'],
    ['P2', '14.0 s (Sí · 0/0)', '13.0 s (Sí · 0/0)', '64.0* s (No · 1/2)', '62.5 / 100', 'En T3 buscó «empanada» y esperó 9 s frente a la lista en blanco creyendo que se colgó (H-02). Al subir a $11.00 hizo clic en pagar (H-01) y necesitó pista para identificar cómo restar unidades desde el catálogo (H-04).'],
    ['P3', '18.0 s (Sí · 0/0)', '19.0 s (Sí · 0/1)', '48.0 s (Sí · 0/2)', '75.0 / 100', 'En T1 dudó si había fila rápida para #A24 (H-06). En T2 esperaba confirmación antes de cancelar #A24 (H-03). En T3 escribió «mocachino» sin mensaje de 0 resultados (H-02) y pulsó pagar con $11.75 (H-01).'],
]))
R.append(d.figure(F_HALLAZGOS, 5.2, 'Figura 2. Evidencia visual de los hallazgos principales durante la Tarea de Refuerzo T3: (izquierda) H-01 pedido con 3 postres ($11.75 > $10.00), botón Confirmar activo y mensaje de rechazo por saldo insuficiente sin monto faltante; (derecha) H-02 estado vacío sin mensaje al buscar «empanada».'))

# Sección 4
R.append(d.sub('4. Fase 3.4: Consolidación de Métricas (ISO 9241-11:2018 y SUS)'))
R.append(d.table([1800, 950, 850, 850, 850, 950, 1000, 894], [
    ['Tarea Evaluada', 'Meta (s)', 'P1 (s)', 'P2 (s)', 'P3 (s)', 'Mediana (s)', 'Éxito Autónomo', 'Err. Crít / No Crít'],
    ['T1 Confirmar pedido #A24', '20.0 s', '16.0', '14.0', '18.0', '16.0 s (-4.0s)', '100.0 % (3/3)', '0 / 0'],
    ['T2 Cancelar y reembolso', '15.0 s', '17.0', '13.0', '19.0', '17.0 s (+2.0s)', '100.0 % (3/3)', '0 / 2'],
    ['T3 Buscador y límite $10', '35.0 s', '52.0', '64.0*', '48.0', '52.0 s (+17.0s)', '66.7 % (2/3)', '1 / 6'],
    ['Consolidado Global', '—', '85.0', '91.0', '85.0', '—', '88.9 % (8/9)', '1 / 8'],
]))
R.append(d.para(
    '**Nota sobre el valor 64.0* s de P2 en T3:** El asterisco (*) indica que el participante P2 no logró completar la tarea T3 de forma autónoma (requirió 1 pista de la moderadora tras quedar detenido ante el buscador en blanco H-02 y el rechazo por saldo insuficiente H-01).'
))
R.append(d.para(
    '**Satisfacción (Cuestionario SUS — Brooke, 1996; Bangor et al., 2009):** P1 = 80.0, P2 = 62.5, P3 = 75.0 → **Promedio grupal = 72.5 puntos** (Mediana = **75.0**), situándose **+4.5 puntos sobre la referencia de la industria (68.0)**. No obstante, el puntaje de P2 (**62.5 < 68.0**, categoría marginal según Bangor et al., 2009) refleja directamente el impacto negativo de los hallazgos H-01 y H-02 durante la Tarea de Refuerzo T3.'
))

# Sección 5
R.append(d.sub('5. Fase 4.5: Matriz Consolidada de Hallazgos (H-01 a H-08)'))
R.append(d.table([700, 2350, 1100, 850, 1550, 1594], [
    ['ID', 'Problema Unificado', 'Heurística', 'Sev. (F/I/P)', 'Evidencia', 'Propuesta de Mejora'],
    ['H-01', 'Botón «Confirmar y pagar» sigue activo cuando total > $10.00 y el error no indica cuánto dinero falta.', 'H5 · H9', '4 Crítico (4/4/4)', '4/4 heurística + P1, P2, P3 en T3', 'Deshabilitar #btn-confirmar si total > saldo y mostrar monto faltante exacto ($X.XX).'],
    ['H-02', 'Buscador deja la lista vacía en blanco sin mensaje de «0 resultados» cuando no hay coincidencias.', 'H1 · H6', '3 Mayor (3/3/3)', '3/4 heurística + P2 y P3 en T3', 'Renderizar estado vacío con role="status" y botón «Ver todo el menú».'],
    ['H-03', '«Cancelar pedido» anula en un solo clic sin confirmar ni advertir pérdida del turno #A24 → #A25.', 'H3 · H5', '3 Mayor (3/3/3)', '3/4 heurística + P1 y P3 en T2', 'Solicitar confirmación de dos pasos advirtiendo la pérdida del turno #A24.'],
    ['H-04', 'Ítems en «Revisa tu pedido» (#lista-pedido) no tienen botón individual «− Quitar» por fila.', 'H6 · H3', '3 Mayor (3/3/3)', '2/4 heurística + P1 y P2 en T3', 'Añadir botón «− Quitar» (≥ 44×44 px) en cada línea de #lista-pedido.'],
    ['H-05', 'Margen de 600 ms en «Cancelar pedido» ignora clics sin indicador visual de enfriamiento.', 'H1', '2 Menor (2/2/2)', '2/4 heurística (AC-04, HL-04)', 'Añadir clase .boton--enfriamiento durante los 600 ms posteriores al pago.'],
    ['H-06', 'No se indica en qué ventanilla del Edificio central retirar el #A24 ni si requiere carné.', 'H10 · H2', '2 Menor (2/2/2)', 'Usuarios P1 y P3 tras T1', 'Especificar «Ventanilla Rápida (PB, Edificio central) con código #A24 y carné».'],
    ['H-07', 'Falta botón «× Limpiar» o atajo Escape en el buscador y filtros de categoría.', 'H7', '2 Menor (2/2/2)', '2/4 heurística (MC-04, CR-04)', 'Añadir botón «× Limpiar» y listener de tecla Escape.'],
    ['H-08', 'Subtítulos <small> (0.8125rem, #6B625C) con tamaño y contraste ajustados en 320 px.', 'H8', '1 Cosm. (2/1/1)', '3/4 heurística en 320 px', 'Subir a 0.875rem y oscurecer --texto-sec a #524944 (8.77:1 sobre #FFFFFF y 8.21:1 sobre #FAF7F3).'],
]))

# Sección 6
R.append(d.sub('6. Fase 4.6: Triangulación Metodológica'))
R.append(d.table([2100, 1800, 4244], [
    ['Clasificación del Cruce', 'Hallazgos', 'Análisis de Complementariedad Metodológica'],
    ['Confirmado por ambos métodos (50.0 %)', 'H-01 (Sev. 4 · P1), H-02 (Sev. 3 · P2), H-03 (Sev. 3 · P3), H-04 (Sev. 3 · P2)', 'El 100 % de los problemas críticos y mayores detectados analíticamente por las heurísticas de Nielsen provocaron fallos y demoras reales en los participantes P1–P3.'],
    ['Solo heurística (37.5 %)', 'H-05 (Sev. 2 · P4), H-07 (Sev. 2 · P4), H-08 (Sev. 1 · P4)', 'La inspección experta capturó condiciones de borde de 600 ms, aceleradores de teclado (Escape) y detalles en 320 px que no emergieron en 3 usuarios novatos a 360 px.'],
    ['Solo usuarios (12.5 %)', 'H-06 (Sev. 2 · P4)', 'Los participantes externos superaron el «sesgo de familiaridad» del equipo al cuestionar en qué ventanilla física presentar el código #A24.'],
]))

# Sección 7
R.append(d.sub('7. Fase 4.7 y 4.8: Criterios Técnicos de Mejora (C-01 a C-08) y Backlog en GitHub Issues'))
R.append(d.para(
    'La priorización del Backlog en GitHub Issues guarda correspondencia estricta con la severidad consensuada: **P1** para Severidad 4 (H-01), **P2 y P3** para Severidad 3 (H-02, H-04 y H-03), y **P4** para Severidades 2 y 1 (H-05, H-06, H-07 y H-08).'
))
R.append(d.table([750, 750, 1750, 2550, 1450, 894], [
    ['Crit.', 'Hall.', 'Componente Afectado', 'Cambio Técnico Específico y Verificable', 'Estándar de Respaldo', 'Prior. / Issue'],
    ['C-01', 'H-01', 'src/interaccion.js · #btn-confirmar', 'Deshabilitar #btn-confirmar si total > saldo y anunciar en #estado el monto exacto faltante ($X.XX).', 'Nielsen H5, H9 · WCAG 2.1 3.3.1, 4.1.3 · ISO 9241-11', 'P1 · Issue #1'],
    ['C-02', 'H-02', 'src/interaccion.js · #lista-catalogo', 'Insertar estado vacío con role="status" («0 resultados para...») y botón «Ver todo el menú».', 'Nielsen H1, H6 · WCAG 2.1 4.1.3', 'P2 · Issue #2'],
    ['C-03', 'H-03', 'src/interaccion.js · #btn-cancelar', 'Confirmación en dos pasos antes de cancelar #A24, advirtiendo pérdida del turno actual.', 'Nielsen H3, H5 · WCAG 2.1 3.3.4 · ISO 9241-11', 'P3 · Issue #3'],
    ['C-04', 'H-04', 'src/index.html · #lista-pedido', 'Añadir botón «− Quitar» (≥ 44×44 px) en cada línea de producto dentro de «Revisa tu pedido».', 'Nielsen H6, H3 · WCAG 2.1 2.5.5 · ISO 9241-11', 'P2 · Issue #2'],
    ['C-05', 'H-05', 'src/estilos.css · #btn-cancelar', 'Aplicar clase .boton--enfriamiento (opacidad 0.7) durante los 600 ms posteriores al pago.', 'Nielsen H1 · WCAG 2.1 1.3.3', 'P4 · Issue #4'],
    ['C-06', 'H-06', 'src/index.html · #estado', 'Incluir microcopia: «Retira en Ventanilla Rápida (PB, Edificio central) con código #A24 y carné».', 'Nielsen H10, H2 · ISO 9241-11', 'P4 · Issue #4'],
    ['C-07', 'H-07', 'src/index.html · .campo-busqueda', 'Agregar botón «× Limpiar» junto a #buscar-producto y soporte para tecla Escape.', 'Nielsen H7 · WCAG 2.1 2.1.1', 'P4 · Issue #4'],
    ['C-08', 'H-08', 'src/estilos.css · --texto-sec', 'Cambiar --texto-sec a #524944 (contraste 8.77:1 sobre #FFFFFF y 8.21:1 sobre #FAF7F3, nivel AAA) y subir <small> a 0.875rem (14 px).', 'Nielsen H8 · WCAG 2.1 1.4.3, 1.4.6', 'P4 · Issue #4'],
]))
R.append(d.EMPTY)
out += R

out += E[110:113]
for k, v in {113: True, 114: True, 115: True, 116: False, 117: True, 118: False, 119: False, 120: False, 121: True}.items():
    out.append(d.check(E[k], v))
out += E[122:124]
for s in [
    '**Respuesta a la pregunta central del laboratorio (Verificación vs. Validación — Boehm, 1984).** Sí: una interfaz que funciona técnicamente al 100 % (0 px de desborde en 320–1366 px y 12/12 pruebas automatizadas aprobadas) puede ser una mala interfaz cuando no previene errores antes del clic (H-01: botón de pago habilitado con saldo insuficiente) ni comunica estados vacíos en el buscador (H-02).',
    '**Impacto medido en ISO 9241-11:2018 y SUS (Brooke, 1996).** Mientras en el flujo básico (T1) la eficacia fue del 100.0 % con mediana de 16.0 s (meta ≤ 20.0 s), en la tarea de refuerzo post-pilotaje (T3) la eficacia cayó al 66.7 %, la mediana subió a 52.0 s (+17.0 s sobre la meta de 35.0 s) y el puntaje SUS del participante P2 descendió a 62.5 (bajo la referencia industrial de 68.0, pese a un promedio grupal de 72.5).',
    '**Valor de la Triangulación y Cierre en GitHub.** La combinación de evaluación heurística (4 inspectores) y pruebas Think-Aloud (P1–P3) permitió confirmar los 4 hallazgos más severos (H-01 a H-04), detectar detalles técnicos analíticos (H-05, H-07, H-08) y descubrir dudas del contexto físico (H-06), traduciéndolos en 8 criterios técnicos verificables (C-01 a C-08) vinculados a los GitHub Issues #1 a #4 (prioridades P1 a P4).'
]:
    out.append(d.concl(s))
out += E[127:129]
for s in [
    'Complementar siempre las pruebas de flujo principal del pilotaje con tareas de refuerzo que evalúen buscadores, filtros vacíos y condiciones de borde financiero.',
    'Aplicar un protocolo estricto de reinicio de estado (F5 / PedidoAPI.reiniciar()) entre sesiones para evitar que el almacenamiento del navegador contamine las métricas de los participantes siguientes.',
    'Triangular la inspección heurística con pruebas empíricas Think-Aloud antes de priorizar el backlog de ingeniería en GitHub Issues.'
]:
    out.append(d.concl(s, 426))
out.append(d.EMPTY)
out.append(E[128].replace('Recomendaciones', 'Bibliografía'))
for s in [
    '[1] J. J. Cañas Delgado, T. Granollers i Saltiveri, y J. Lorés Vidal, *Diseño de sistemas interactivos centrados en el usuario*. Barcelona, España: Editorial UOC, 2012.',
    '[2] J. Ferrer Martínez, *Desarrollo de interfaces*. Madrid, España: RA-MA Editorial, 2015.',
    '[3] B. Shneiderman, *Diseño de interfaces de usuario*, 4.ª ed. Madrid, España: Pearson Educación, 2006.',
    '[4] R. S. Pressman, *Ingeniería del software: un enfoque práctico*, 7.ª ed. México D.F., México: McGraw-Hill, 2010.',
    '[5] H. Beati, *HTML5 y CSS3 para diseñadores*, 1.ª ed. Buenos Aires, Argentina: Alfaomega, 2015.',
    '[6] J. E. Córcoles Tendero y F. Montero Simarro, *Diseño de interfaces WEB*. Madrid, España: RA-MA Editorial, 2015.',
    '[7] J. Pintos Fernández, *Aplicación de técnicas de usabilidad y accesibilidad en el entorno cliente. UF1843*. La Rioja, España: Tutor Formación, 2024.',
    '[8] B. W. Boehm, "Verifying and Validating Software Requirements and Design Specifications," *IEEE Software*, vol. 1, no. 1, pp. 75–88, Jan. 1984.',
    '[9] J. Nielsen, *Usability Engineering*. San Francisco, CA, USA: Morgan Kaufmann, 1994.',
    '[10] J. Nielsen, "Severity Ratings for Usability Problems," *Nielsen Norman Group*, 1995. [En línea]. Disponible: https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/',
    '[11] J. Brooke, "SUS: A \'Quick and Dirty\' Usability Scale," in *Usability Evaluation in Industry*, London, UK: Taylor & Francis, 1996, pp. 189–194.',
    '[12] A. Bangor, P. Kortum, y J. Miller, "Determining What Individual SUS Scores Mean: Adding an Adjective Rating Scale," *Journal of Usability Studies*, vol. 4, no. 3, pp. 114–123, May 2009.',
    '[13] World Wide Web Consortium (W3C), "Web Content Accessibility Guidelines (WCAG) 2.1," *W3C Recommendation*, Jun. 2018. [En línea]. Disponible: https://www.w3.org/TR/WCAG21/',
    '[14] International Organization for Standardization, *Ergonomics of human-system interaction — Part 11: Usability: Definitions and concepts*, ISO 9241-11:2018, 2018.'
]:
    out.append(d.ref(s))
out.append(d.EMPTY)
out.append(d.sub('Firmas de los integrantes'))
out.append(d.table([3600, 2200, 2344], [
    ['Integrante', 'Cédula / Correo UTA', 'Firma'],
    ['Henry Daniel Lagua Flores', 'hlagua6116@uta.edu.ec', ''],
    ['Melany Saleth Cevallos Goyes', 'mcevallos8901@uta.edu.ec', ''],
    ['Alison Marcela Cobos Taco', 'tacomarcelab@gmail.com', ''],
    ['Carlos Giovanni Ramos Jácome', 'carlos.giovanni.ramos.work@gmail.com', ''],
]))
out.append(E[132])

full_xml = ''.join(out)
assert '`' not in full_xml, 'Error: quedan backticks sin convertir en el XML'
assert '>PP<' not in full_xml and '>YY<' not in full_xml, 'Error: quedan textos ocultos PP/YY'

dest = d.save(out, DOC + 'APE6_Informe_Final.docx')
print('docx generado:', dest)

ps = ("$w=New-Object -ComObject Word.Application;$w.Visible=$false;try{$d=$w.Documents.Open('%s',$false,$true);"
      "$d.SaveAs([ref]'%s',[ref]17);$d.Close($false)}finally{$w.Quit()}") % (dest.replace('/', '\\'), dest.replace('/', '\\')[:-5] + '.pdf')
r = subprocess.run(['powershell', '-NoProfile', '-Command', ps], capture_output=True, text=True)
print('pdf:', 'ok' if r.returncode == 0 else 'error: ' + r.stderr[:200])
