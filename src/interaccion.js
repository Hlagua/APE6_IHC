/**
 * APE 6 · CaféU · Controlador de interacción de «Mi pedido» + Catálogo (Ajuste Post-Pilotaje)
 * Responsable: Melany Saleth Cevallos Goyes (@SalyC15) · Desarrollador Front-End
 *
 * Conecta:
 * - T1: Confirmación y pago con cobro único (#A24).
 * - T2: Cancelación con devolución de saldo y margen de 600 ms.
 * - T3 (Tarea de refuerzo): Buscador en tiempo real, filtros por categoría y adición/remoción.
 * - Reinicio F5: botón #btn-reiniciar-lab y atajo Alt+R para limpiar sessionStorage entre sesiones.
 */
document.addEventListener('DOMContentLoaded', () => {
  const btnConfirmar = document.getElementById('btn-confirmar');
  const btnCancelar = document.getElementById('btn-cancelar');
  const btnReiniciarLab = document.getElementById('btn-reiniciar-lab');
  const estado = document.getElementById('estado');
  const resumen = document.querySelector('.resumen');
  const saldo = document.getElementById('saldo');
  const totalEl = document.getElementById('total');
  const listaPedido = document.getElementById('lista-pedido');
  const listaCatalogo = document.getElementById('lista-catalogo');
  const inputBuscar = document.getElementById('buscar-producto');
  const chipsFiltro = [...document.querySelectorAll('.chip-filtro')];

  const api = window.PedidoAPI;
  const dinero = (n) => '$' + Number(n).toFixed(2);

  // Margen de 600 ms contra el doble Enter (heredado de APE 5)
  const MARGEN_DOBLE_PULSACION_MS = 600;
  let cancelarBloqueadoHasta = 0;
  let categoriaActual = 'todos';

  function renderizarCatalogo() {
    if (!listaCatalogo || !api.buscarProductos) return;
    const termino = inputBuscar ? inputBuscar.value : '';
    const filtrados = api.buscarProductos(termino, categoriaActual);
    const s = api.obtenerEstado();
    const bloqueado = s.estado === 'confirmado';

    listaCatalogo.innerHTML = '';
    filtrados.forEach((prod) => {
      const enPedido = (s.items || []).find((i) => i.id === prod.id);
      const cant = enPedido ? enPedido.cantidad : 0;
      const li = document.createElement('li');
      li.className = 'item-catalogo';
      li.innerHTML =
        `<div class="item-catalogo__info">` +
          `<strong>${prod.nombre} · ${dinero(prod.precio)}</strong>` +
          `<small>${prod.detalle} ${cant > 0 ? '· En bandeja: ' + cant : ''}</small>` +
        `</div>` +
        `<div class="item-catalogo__acciones">` +
          `<button type="button" class="btn-cat" data-accion="quitar" data-id="${prod.id}" ${bloqueado || cant === 0 ? 'disabled' : ''} aria-label="Quitar ${prod.nombre}">−</button>` +
          `<button type="button" class="btn-cat btn-cat--agregar" data-accion="agregar" data-id="${prod.id}" ${bloqueado ? 'disabled' : ''} aria-label="Agregar ${prod.nombre}">+ Agregar</button>` +
        `</div>`;
      listaCatalogo.appendChild(li);
    });
  }

  function pintar(s) {
    const totalActual = typeof s.total === 'number' ? s.total : api.datos.total;
    if (totalEl) totalEl.textContent = dinero(totalActual);
    saldo.textContent = dinero(s.saldo);

    if (listaPedido && Array.isArray(s.items)) {
      listaPedido.innerHTML = s.items.map((it) => {
        const sub = it.precio * it.cantidad;
        return `<li><span>${it.cantidad} × ${it.nombre} <small>${it.detalle}</small></span> <span>${dinero(sub)}</span></li>`;
      }).join('');
    }

    if (s.ultimoError === 'saldo_insuficiente') {
      resumen.dataset.estado = 'error';
      estado.textContent = 'No se pudo procesar el pago: el total del pedido supera el saldo disponible en tu tarjeta universitaria.';
      btnConfirmar.disabled = false;
      btnConfirmar.textContent = 'Confirmar y pagar · ' + dinero(totalActual);
      btnCancelar.hidden = true;
      renderizarCatalogo();
      return;
    }

    resumen.dataset.estado = s.estado;

    if (s.estado === 'confirmado') {
      estado.textContent = 'Pedido ' + s.numero + ' confirmado y pagado (' + dinero(totalActual) +
        '). Estará listo en unos ' + api.datos.minutos + ' minutos en el ' + api.datos.retiro + '.';
      btnConfirmar.disabled = true;
      btnConfirmar.textContent = 'Pedido ' + s.numero + ' pagado';
      btnCancelar.hidden = false;
    } else {
      estado.textContent = s.estado === 'cancelado'
        ? 'Cancelaste el pedido ' + s.numero + '. Se devolvieron ' + dinero(totalActual) + ' a tu tarjeta universitaria.'
        : 'Aún no confirmas tu pedido. No se ha cobrado nada.';
      btnConfirmar.disabled = false;
      btnConfirmar.textContent = 'Confirmar y pagar · ' + dinero(totalActual);
      btnCancelar.hidden = true;
    }

    renderizarCatalogo();
  }

  pintar(api.obtenerEstado());

  if (listaCatalogo) {
    listaCatalogo.addEventListener('click', (e) => {
      const btn = e.target.closest('button[data-accion]');
      if (!btn) return;
      const id = btn.dataset.id;
      const r = btn.dataset.accion === 'agregar'
        ? api.agregarProducto(id)
        : api.quitarProducto(id);
      if (r.exito) pintar(r);
    });
  }

  if (inputBuscar) {
    inputBuscar.addEventListener('input', () => renderizarCatalogo());
  }

  chipsFiltro.forEach((chip) => {
    chip.addEventListener('click', () => {
      categoriaActual = chip.dataset.categoria || 'todos';
      chipsFiltro.forEach((c) => {
        const activo = c === chip;
        c.classList.toggle('activo', activo);
        c.setAttribute('aria-pressed', String(activo));
      });
      renderizarCatalogo();
    });
  });

  btnConfirmar.addEventListener('click', () => {
    if (resumen.dataset.estado === 'confirmado') return;
    const r = api.confirmarPedido();
    pintar(r);
    if (!r.exito) return;
    cancelarBloqueadoHasta = performance.now() + MARGEN_DOBLE_PULSACION_MS;
    btnCancelar.focus();
  });

  btnCancelar.addEventListener('click', () => {
    if (performance.now() < cancelarBloqueadoHasta) return;
    const r = api.cancelarPedido();
    if (!r.exito) return;
    pintar(r);
    btnConfirmar.focus();
  });

  function reiniciarSesionLaboratorio() {
    const limpio = api.reiniciar();
    if (inputBuscar) inputBuscar.value = '';
    categoriaActual = 'todos';
    chipsFiltro.forEach((c) => {
      const esTodos = c.dataset.categoria === 'todos';
      c.classList.toggle('activo', esTodos);
      c.setAttribute('aria-pressed', String(esTodos));
    });
    pintar(limpio);
  }

  if (btnReiniciarLab) {
    btnReiniciarLab.addEventListener('click', reiniciarSesionLaboratorio);
  }

  document.addEventListener('keydown', (e) => {
    if (e.altKey && (e.key === 'r' || e.key === 'R')) {
      e.preventDefault();
      reiniciarSesionLaboratorio();
    }
  });
});
