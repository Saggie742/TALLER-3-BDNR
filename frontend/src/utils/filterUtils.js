export const filtrosIniciales = {
  ciudad: "",
  categoria: "",
  fechaDesde: "",
  fechaHasta: "",
  metodoPago: "",
};

export function hayFiltrosActivos(filtros) {
  return Boolean(
    filtros.ciudad ||
      filtros.categoria ||
      filtros.fechaDesde ||
      filtros.fechaHasta ||
      filtros.metodoPago
  );
}

export function construirQueryParams(filtros) {
  const params = new URLSearchParams();

  if (filtros.ciudad) {
    params.append("ciudad", filtros.ciudad);
  }

  if (filtros.categoria) {
    params.append("categoria", filtros.categoria);
  }

  if (filtros.fechaDesde) {
    params.append("fechaDesde", filtros.fechaDesde);
  }

  if (filtros.fechaHasta) {
    params.append("fechaHasta", filtros.fechaHasta);
  }

  if (filtros.metodoPago) {
    params.append("metodoPago", filtros.metodoPago);
  }

  const queryString = params.toString();

  return queryString ? `?${queryString}` : "";
}