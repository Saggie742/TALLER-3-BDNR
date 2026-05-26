from fastapi import APIRouter, Query
from filtered_dashboard_service import (
    obtener_resumen_filtrado,
    obtener_ventas_por_categoria_filtrado,
    obtener_compras_por_ciudad_filtrado,
    obtener_metodos_pago_filtrado,
    obtener_productos_mas_vendidos_filtrado,
    obtener_compras_por_rango_etario_filtrado,
    obtener_ventas_por_fecha_filtrado,
)

router = APIRouter(
    prefix="/api/dashboard/filtrado",
    tags=["Dashboard Filtrado"],
)


@router.get("/resumen")
def resumen_filtrado(
    ciudad: str | None = Query(default=None),
    categoria: str | None = Query(default=None),
    fechaDesde: str | None = Query(default=None),
    fechaHasta: str | None = Query(default=None),
    metodoPago: str | None = Query(default=None),
):
    return obtener_resumen_filtrado(
        ciudad=ciudad,
        categoria=categoria,
        fechaDesde=fechaDesde,
        fechaHasta=fechaHasta,
        metodoPago=metodoPago,
    )

@router.get("/ventas-por-categoria")
def ventas_por_categoria_filtrado(
    ciudad: str | None = Query(default=None),
    categoria: str | None = Query(default=None),
    fechaDesde: str | None = Query(default=None),
    fechaHasta: str | None = Query(default=None),
    metodoPago: str | None = Query(default=None),
):
    return obtener_ventas_por_categoria_filtrado(
        ciudad=ciudad,
        categoria=categoria,
        fechaDesde=fechaDesde,
        fechaHasta=fechaHasta,
        metodoPago=metodoPago,
    )


@router.get("/compras-por-ciudad")
def compras_por_ciudad_filtrado(
    ciudad: str | None = Query(default=None),
    categoria: str | None = Query(default=None),
    fechaDesde: str | None = Query(default=None),
    fechaHasta: str | None = Query(default=None),
    metodoPago: str | None = Query(default=None),
):
    return obtener_compras_por_ciudad_filtrado(
        ciudad=ciudad,
        categoria=categoria,
        fechaDesde=fechaDesde,
        fechaHasta=fechaHasta,
        metodoPago=metodoPago,
    )


@router.get("/metodos-pago")
def metodos_pago_filtrado(
    ciudad: str | None = Query(default=None),
    categoria: str | None = Query(default=None),
    fechaDesde: str | None = Query(default=None),
    fechaHasta: str | None = Query(default=None),
    metodoPago: str | None = Query(default=None),
):
    return obtener_metodos_pago_filtrado(
        ciudad=ciudad,
        categoria=categoria,
        fechaDesde=fechaDesde,
        fechaHasta=fechaHasta,
        metodoPago=metodoPago,
    )

@router.get("/productos-mas-vendidos")
def productos_mas_vendidos_filtrado(
    ciudad: str | None = Query(default=None),
    categoria: str | None = Query(default=None),
    fechaDesde: str | None = Query(default=None),
    fechaHasta: str | None = Query(default=None),
    metodoPago: str | None = Query(default=None),
):
    return obtener_productos_mas_vendidos_filtrado(
        ciudad=ciudad,
        categoria=categoria,
        fechaDesde=fechaDesde,
        fechaHasta=fechaHasta,
        metodoPago=metodoPago,
    )


@router.get("/compras-por-rango-etario")
def compras_por_rango_etario_filtrado(
    ciudad: str | None = Query(default=None),
    categoria: str | None = Query(default=None),
    fechaDesde: str | None = Query(default=None),
    fechaHasta: str | None = Query(default=None),
    metodoPago: str | None = Query(default=None),
):
    return obtener_compras_por_rango_etario_filtrado(
        ciudad=ciudad,
        categoria=categoria,
        fechaDesde=fechaDesde,
        fechaHasta=fechaHasta,
        metodoPago=metodoPago,
    )


@router.get("/ventas-por-fecha")
def ventas_por_fecha_filtrado(
    ciudad: str | None = Query(default=None),
    categoria: str | None = Query(default=None),
    fechaDesde: str | None = Query(default=None),
    fechaHasta: str | None = Query(default=None),
    metodoPago: str | None = Query(default=None),
):
    return obtener_ventas_por_fecha_filtrado(
        ciudad=ciudad,
        categoria=categoria,
        fechaDesde=fechaDesde,
        fechaHasta=fechaHasta,
        metodoPago=metodoPago,
    )
