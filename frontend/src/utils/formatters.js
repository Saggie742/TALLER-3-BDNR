export function formatearMonto(valor) {
  return new Intl.NumberFormat("es-CL", {
    style: "currency",
    currency: "CLP",
    maximumFractionDigits: 0,
  }).format(valor ?? 0);
}

export function formatearNumero(valor) {
  return new Intl.NumberFormat("es-CL").format(valor ?? 0);
}
export function formatearMontoCompacto(valor) {
  const numero = Number(valor ?? 0);

  if (numero >= 1_000_000_000) {
    return `$${Math.round(numero / 1_000_000_000)}MM`;
  }

  if (numero >= 1_000_000) {
    return `$${Math.round(numero / 1_000_000)}M`;
  }

  return new Intl.NumberFormat("es-CL", {
    style: "currency",
    currency: "CLP",
    maximumFractionDigits: 0,
  }).format(numero);
}