from fastapi import APIRouter

from dashboard_service import (
    obtener_estado_importacion,
    obtener_resumen_dashboard,
    obtener_ventas_por_categoria,
    obtener_compras_por_ciudad,
    obtener_metodos_pago,
    obtener_productos_mas_vendidos,
    obtener_compras_por_rango_etario,
    obtener_ventas_por_fecha,
    obtener_opciones_filtros,
)

router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"],
)


@router.get("/estado-importacion")
def estado_importacion():
    return obtener_estado_importacion()


@router.get("/resumen")
def resumen_dashboard():
    return obtener_resumen_dashboard()

@router.get("/ventas-por-categoria")
def ventas_por_categoria():
    return obtener_ventas_por_categoria()


@router.get("/compras-por-ciudad")
def compras_por_ciudad():
    return obtener_compras_por_ciudad()


@router.get("/metodos-pago")
def metodos_pago():
    return obtener_metodos_pago()

@router.get("/productos-mas-vendidos")
def productos_mas_vendidos():
    return obtener_productos_mas_vendidos()


@router.get("/compras-por-rango-etario")
def compras_por_rango_etario():
    return obtener_compras_por_rango_etario()


@router.get("/ventas-por-fecha")
def ventas_por_fecha():
    return obtener_ventas_por_fecha()

@router.get("/filtros")
def opciones_filtros():
    return obtener_opciones_filtros()
