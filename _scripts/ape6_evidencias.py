"""Generador de capturas de evidencia para el APE 6 · Caso CaféU.

Captura con Chrome headless:
1. T1-inicial-360.png (estado limpio post-F5: saldo $10.00, catálogo 6 productos, base $4.25)
2. T1-confirmado-360.png (pedido #A24 confirmado, saldo $5.75)
3. T3-hallazgo-H01-saldo.png (Hallazgo H-01: total $11.75 > $10.00 y rechazo tras clic)
4. T3-hallazgo-H02-buscador.png (Hallazgo H-02: búsqueda «empanada» con lista vacía sin feedback)
5. Escritorio-1366.png (vista adaptable en 1366 × 820 px)
"""
import os, subprocess, time, http.server, socketserver, threading
from PIL import Image, ImageDraw, ImageFont

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVID = os.path.join(REPO, 'evidencias')
TMP = os.path.join(REPO, '_scripts', '_tmp')
os.makedirs(EVID, exist_ok=True)
os.makedirs(TMP, exist_ok=True)
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
PORT = 8769
BASE = f'http://127.0.0.1:{PORT}/'

HARNESS = '''<!doctype html><meta charset="utf-8"><body style="margin:0;background:#fff">
<iframe id="f" src="{src}" style="width:{w}px;height:{h}px;border:0;display:block"></iframe>
<script>
const f = document.getElementById('f');
f.addEventListener('load', () => setTimeout(() => {{
  const w = f.contentWindow, d = w.document;
  try {{ w.sessionStorage.clear(); w.PedidoAPI.reiniciar(); }} catch (e) {{}}
  const s = d.createElement('style'); s.textContent = '*{{transition:none!important}}'; d.head.appendChild(s);
  {accion}
}}, 250));
</script>'''


def font(sz, bold=False):
    for f in ([r'C:\Windows\Fonts\segoeuib.ttf'] if bold else []) + [r'C:\Windows\Fonts\segoeui.ttf', r'C:\Windows\Fonts\arial.ttf']:
        if os.path.exists(f):
            return ImageFont.truetype(f, sz)
    return ImageFont.load_default()


def capturar(src, w, h, nombre, etiqueta, subetiqueta, color_barra='#1f2629', accion=''):
    harness = os.path.join(TMP, 'h.html')
    with open(harness, 'w', encoding='utf8') as fh:
        fh.write(HARNESS.format(src=src, w=w, h=h, accion=accion))
    url = BASE + '_scripts/_tmp/h.html'
    raw = os.path.join(TMP, 'raw.png')
    common = [CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--virtual-time-budget=2500',
              '--window-size=%d,%d' % (w + 120, h + 120)]
    subprocess.run(common + ['--screenshot=' + raw, url], capture_output=True)
    shot = Image.open(raw).convert('RGB').crop((0, 0, w, h))
    barra = 56
    lienzo = Image.new('RGB', (w, h + barra), color_barra)
    lienzo.paste(shot, (0, barra))
    dr = ImageDraw.Draw(lienzo)
    dr.text((10, 6), etiqueta, fill='white', font=font(15, True))
    dr.text((10, 29), subetiqueta, fill='white', font=font(14))
    destino = os.path.join(EVID, nombre)
    lienzo.save(destino)
    print('capturado:', destino)
    return destino


if __name__ == '__main__':
    os.chdir(REPO)
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(('127.0.0.1', PORT), handler)
    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()
    try:
        capturar('../../src/index.html', 360, 920, 'T1-inicial-360.png',
                 'APE 6 · Estado Inicial (Reinicio F5) · 360 px',
                 'Saldo $10.00 · Base $4.25 · Catálogo 6 ítems',
                 '#1f2629',
                 "d.getElementById('btn-reiniciar-lab').click();")

        capturar('../../src/index.html', 360, 920, 'T1-confirmado-360.png',
                 'APE 6 · Tarea 1 (Confirmado #A24) · 360 px',
                 'Éxito 100 % · Mediana 16.0 s · Saldo $5.75',
                 '#2E7D4F',
                 "d.getElementById('btn-reiniciar-lab').click(); d.getElementById('btn-confirmar').click();")

        capturar('../../src/index.html', 360, 920, 'T3-hallazgo-H01-saldo.png',
                 'Hallazgo H-01 (Sev. 4 Crítico) · Saldo Insuficiente',
                 'Total $11.75 > $10.00 · Error tras clic sin monto faltante',
                 '#8a1c1c',
                 "d.getElementById('btn-reiniciar-lab').click();"
                 "for(let k=0;k<3;k++){d.querySelector('button[data-accion=\"agregar\"][data-id=\"cheesecake-mora\"]').click();}"
                 "d.getElementById('btn-confirmar').click();"
                 "d.querySelector('.tarjeta').scrollIntoView();")

        capturar('../../src/index.html', 360, 760, 'T3-hallazgo-H02-buscador.png',
                 'Hallazgo H-02 (Sev. 3 Mayor) · Buscador Vacío',
                 'Consulta «empanada» → 0 resultados sin mensaje',
                 '#8A4B00',
                 "d.getElementById('btn-reiniciar-lab').click();"
                 "const inp = d.getElementById('buscar-producto');"
                 "inp.value = 'empanada'; inp.dispatchEvent(new w.Event('input'));")

        capturar('../../src/index.html', 1366, 820, 'Escritorio-1366.png',
                 'APE 6 · CaféU en Escritorio (1366 × 820 px) · 2 Columnas',
                 'Verificación 0 px desborde · Evaluación Heurística y Think-Aloud',
                 '#1f2629',
                 "d.getElementById('btn-reiniciar-lab').click(); d.getElementById('btn-confirmar').click();")
    finally:
        httpd.shutdown()
