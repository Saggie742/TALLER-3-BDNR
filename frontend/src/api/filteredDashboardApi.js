import { get } from "./apiClient";
import { construirQueryParams } from "../utils/filterUtils";

export function obtenerResumenFiltrado(filtros) {
  const queryParams = construirQueryParams(filtros);

  return get(
    `/filtrado/resumen${queryParams}`,
    "No se pudo obtener el resumen filtrado"
  );
}

export function obtenerVentasPorCategoriaFiltrado(filtros) {
  const queryParams = construirQueryParams(filtros);

  return get(
    `/filtrado/ventas-por-categoria${queryParams}`,
    "No se pudo obtener las ventas por categoría filtradas"
  );
}

export function obtenerComprasPorCiudadFiltrado(filtros) {
  const queryParams = construirQueryParams(filtros);

  return get(
    `/filtrado/compras-por-ciudad${queryParams}`,
    "No se pudo obtener las compras por ciudad filtradas"
  );
}

export function obtenerMetodosPagoFiltrado(filtros) {
  const queryParams = construirQueryParams(filtros);

  return get(
    `/filtrado/metodos-pago${queryParams}`,
    "No se pudo obtener los métodos de pago filtrados"
  );
}

export function obtenerProductosMasVendidosFiltrado(filtros) {
  const queryParams = construirQueryParams(filtros);

  return get(
    `/filtrado/productos-mas-vendidos${queryParams}`,
    "No se pudo obtener los productos más vendidos filtrados"
  );
}

export function obtenerComprasPorRangoEtarioFiltrado(filtros) {
  const queryParams = construirQueryParams(filtros);

  return get(
    `/filtrado/compras-por-rango-etario${queryParams}`,
    "No se pudo obtener las compras por rango etario filtradas"
  );
}

export function obtenerVentasPorFechaFiltrado(filtros) {
  const queryParams = construirQueryParams(filtros);

  return get(
    `/filtrado/ventas-por-fecha${queryParams}`,
    "No se pudo obtener las ventas por fecha filtradas"
  );
}