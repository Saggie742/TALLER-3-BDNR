from typing import Any


def construir_filtros(
    ciudad: str | None = None,
    categoria: str | None = None,
    fechaDesde: str | None = None,
    fechaHasta: str | None = None,
    metodoPago: str | None = None,
) -> tuple[str, tuple[Any, ...]]:
    condiciones = []
    parametros: list[Any] = []

    if ciudad:
        condiciones.append("ciudad = %s")
        parametros.append(ciudad)

    if categoria:
        condiciones.append("categoria = %s")
        parametros.append(categoria)

    if fechaDesde:
        condiciones.append("fecha >= %s")
        parametros.append(fechaDesde)

    if fechaHasta:
        condiciones.append("fecha <= %s")
        parametros.append(fechaHasta)

    if metodoPago:
        condiciones.append("metodopago = %s")
        parametros.append(metodoPago)

    if not condiciones:
        return "", tuple()

    where_clause = "WHERE " + " AND ".join(condiciones)

    return where_clause, tuple(parametros)
