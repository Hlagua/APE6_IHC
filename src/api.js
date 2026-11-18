/**
 * APE 6 · CaféU · Capa de datos y reglas de negocio del pedido (Ajuste Post-Pilotaje)
 * Responsable: Alison Marcela Cobos Taco (@Itsuna18) · Desarrollador Back-End
 *
 * Continuación de APE 5: simula el servicio de pedidos de CaféU con regla de cobro único,
 * reembolso al cancelar, catálogo filtrable para la Tarea de Refuerzo (T3), validación de
 * límite de saldo ($10.00) y protocolo de reinicio de sesión (F5 / PedidoAPI.reiniciar()).
 */
(function (global) {
  'use strict';

  const STORAGE_KEY = 'ape6_cafeu_pedido_v1';

  const CATALOGO = [
    { id: 'cafe-americano', nombre: 'Café Americano', detalle: '12 oz · caliente', categoria: 'bebidas', precio: 1.50, base: true },
    { id: 'sanduche-jyq', nombre: 'Sánduche', detalle: 'jamón y queso', categoria: 'snacks', precio: 2.75, base: true },
    { id: 'capuchino-avena', nombre: 'Capuchino sin lactosa', detalle: '12 oz · leche de avena', categoria: 'bebidas', precio: 2.25, base: false },
    { id: 'jugo-naranja', nombre: 'Jugo natural de naranja', detalle: '14 oz · frío', categoria: 'bebidas', precio: 1.75, base: false },
    { id: 'cheesecake-mora', nombre: 'Postre Cheesecake de mora', detalle: 'porción individual', categoria: 'postres', precio: 2.50, base: false },
    { id: 'croissant-almendra', nombre: 'Croissant relleno', detalle: 'horneado del día', categoria: 'snacks', precio: 2.00, base: false }
  ];

  const CONFIG = {
    retiro: 'Edificio central',
    minutos: 10,
    saldoInicial: 10.00,
    primerNumero: 24 // #A24, continuidad directa con APE 4 y APE 5
  };

  const redondear = (n) => Math.round(n * 100) / 100;

  function itemsIniciales() {
    return [
      { id: 'cafe-americano', nombre: 'Café Americano', detalle: '12 oz · caliente', precio: 1.50, cantidad: 1, base: true },
      { id: 'sanduche-jyq', nombre: 'Sánduche', detalle: 'jamón y queso', precio: 2.75, cantidad: 1, base: true }
    ];
  }

  function calcularTotal(items) {
    return redondear(items.reduce((acc, it) => acc + it.precio * it.cantidad, 0));
  }

  function inicial() {
    const items = itemsIniciales();
    return {
      estado: 'pendiente', // pendiente | confirmado | cancelado
      items: items,
      total: calcularTotal(items),
      saldo: CONFIG.saldoInicial,
      numero: null,
      siguiente: CONFIG.primerNumero,
      cobros: 0,
      ultimoError: null
    };
  }

  function cargar() {
    try {
      const raw = sessionStorage.getItem(STORAGE_KEY);
      if (raw) {
        const parsed = JSON.parse(raw);
        if (parsed && Array.isArray(parsed.items)) {
          parsed.total = calcularTotal(parsed.items);
          return parsed;
        }
      }
    } catch (e) { /* modo sin sessionStorage */ }
    return inicial();
  }

  function guardar(datos) {
    try {
      sessionStorage.setItem(STORAGE_KEY, JSON.stringify(datos));
    } catch (e) { /* modo sin sessionStorage */ }
  }

  const PedidoAPI = {
    datos: {
      get productos() { return cargar().items; },
      get total() { return cargar().total; },
      retiro: CONFIG.retiro,
      minutos: CONFIG.minutos,
      saldoInicial: CONFIG.saldoInicial,
      primerNumero: CONFIG.primerNumero
    },

    catalogo: CATALOGO,

    obtenerEstado: function () {
      return cargar();
    },

    /**
     * Filtra el catálogo por texto y categoría (Tarea de refuerzo T3).
     */
    buscarProductos: function (termino, categoria) {
      const q = (termino || '').trim().toLowerCase();
      const cat = (categoria || 'todos').toLowerCase();
      return CATALOGO.filter((prod) => {
        const coincideCat = cat === 'todos' || prod.categoria === cat;
        const coincideTexto = !q ||
          prod.nombre.toLowerCase().includes(q) ||
          prod.detalle.toLowerCase().includes(q) ||
          prod.categoria.toLowerCase().includes(q);
        return coincideCat && coincideTexto;
      });
    },

    /**
     * Agrega 1 unidad de un producto del catálogo al pedido pendiente.
     */
    agregarProducto: function (idProducto) {
      const s = cargar();
      if (s.estado === 'confirmado') {
        return { exito: false, motivo: 'pedido_bloqueado', ...s };
      }
      const prod = CATALOGO.find((p) => p.id === idProducto);
      if (!prod) {
        return { exito: false, motivo: 'producto_no_encontrado', ...s };
      }
      const items = s.items.map((i) => ({ ...i }));
      const existente = items.find((i) => i.id === idProducto);
      if (existente) {
        existente.cantidad += 1;
      } else {
        items.push({
          id: prod.id,
          nombre: prod.nombre,
          detalle: prod.detalle,
          precio: prod.precio,
          cantidad: 1,
          base: !!prod.base
        });
      }
      const total = calcularTotal(items);
      const nuevo = {
        ...s,
        estado: 'pendiente',
        items: items,
        total: total,
        ultimoError: null
      };
      guardar(nuevo);
      return { exito: true, ...nuevo };
    },

    /**
     * Resta 1 unidad de un producto en el pedido pendiente (mínimo mantener 1 ítem en el pedido).
     */
    quitarProducto: function (idProducto) {
      const s = cargar();
      if (s.estado === 'confirmado') {
        return { exito: false, motivo: 'pedido_bloqueado', ...s };
      }
      const items = s.items.map((i) => ({ ...i }));
      const idx = items.findIndex((i) => i.id === idProducto);
      if (idx === -1) {
        return { exito: false, motivo: 'producto_no_encontrado', ...s };
      }
      if (items[idx].cantidad > 1) {
        items[idx].cantidad -= 1;
      } else if (items.length > 1) {
        items.splice(idx, 1);
      } else {
        return { exito: false, motivo: 'minimo_un_producto', ...s };
      }
      const total = calcularTotal(items);
      const nuevo = {
        ...s,
        estado: 'pendiente',
        items: items,
        total: total,
        ultimoError: null
      };
      guardar(nuevo);
      return { exito: true, ...nuevo };
    },

    /**
     * Confirma y cobra el pedido actual. Rechaza doble cobro y saldo insuficiente.
     */
    confirmarPedido: function () {
      const s = cargar();
      if (s.estado === 'confirmado') {
        return { exito: false, motivo: 'ya_confirmado', ...s };
      }
      if (s.total > s.saldo) {
        const faltante = redondear(s.total - s.saldo);
        const conError = {
          ...s,
          ultimoError: 'saldo_insuficiente',
          faltante: faltante
        };
        guardar(conError);
        return { exito: false, motivo: 'saldo_insuficiente', faltante: faltante, ...conError };
      }
      const nuevo = {
        ...s,
        estado: 'confirmado',
        saldo: redondear(s.saldo - s.total),
        numero: '#A' + s.siguiente,
        siguiente: s.siguiente + 1,
        cobros: s.cobros + 1,
        ultimoError: null
      };
      guardar(nuevo);
      return { exito: true, ...nuevo };
    },

    /**
     * Cancela el pedido confirmado y restituye el total cobrado a la tarjeta universitaria.
     */
    cancelarPedido: function () {
      const s = cargar();
      if (s.estado !== 'confirmado') {
        return { exito: false, motivo: 'sin_pedido', ...s };
      }
      const nuevo = {
        ...s,
        estado: 'cancelado',
        saldo: redondear(s.saldo + s.total),
        ultimoError: null
      };
      guardar(nuevo);
      return { exito: true, ...nuevo };
    },

    /**
     * Reinicia el estado a los valores de fábrica (Protocolo F5 entre sesiones de usuario).
     */
    reiniciar: function () {
      try {
        sessionStorage.removeItem(STORAGE_KEY);
      } catch (e) { /* sin sessionStorage */ }
      return inicial();
    }
  };

  global.PedidoAPI = PedidoAPI;
})(typeof window !== 'undefined' ? window : this);
