import { get } from "./apiClient";

export function obtenerResumenDashboard() {
  return get(
    "/resumen",
    "No se pudo obtener el resumen del dashboard"
  );
}

export function obtenerEstadoImportacion() {
  return get(
    "/estado-importacion",
    "No se pudo obtener el estado de importación"
  );
}

export function obtenerVentasPorCategoria() {
  return get(
    "/ventas-por-categoria",
    "No se pudo obtener las ventas por categoría"
  );
}

export function obtenerComprasPorCiudad() {
  return get(
    "/compras-por-ciudad",
    "No se pudo obtener las compras por ciudad"
  );
}

export function obtenerMetodosPago() {
  return get(
    "/metodos-pago",
    "No se pudo obtener los métodos de pago"
  );
}

export function obtenerProductosMasVendidos() {
  return get(
    "/productos-mas-vendidos",
    "No se pudo obtener los productos más vendidos"
  );
}
export function obtenerComprasPorRangoEtario() {
  return get(
    "/compras-por-rango-etario",
    "No se pudo obtener las compras por rango etario"
  );
}

export function obtenerVentasPorFecha() {
  return get(
    "/ventas-por-fecha",
    "No se pudo obtener las ventas por fecha"
  );
}
export function obtenerOpcionesFiltros() {
  return get(
    "/filtros",
    "No se pudieron obtener las opciones de filtros"
  );
}