from filtered_dashboard_queries import (
    consultar_total_ventas_filtrado,
    consultar_promedio_gasto_filtrado,
    consultar_categoria_mas_vendida_filtrada,
    consultar_producto_mas_vendido_filtrado,
    consultar_ciudad_con_mas_compras_filtrada,
    consultar_metodo_pago_mas_usado_filtrado,
    consultar_ventas_por_categoria_filtrado,
    consultar_compras_por_ciudad_filtrado,
    consultar_metodos_pago_filtrado,
    consultar_productos_mas_vendidos_filtrado,
    consultar_compras_por_rango_etario_filtrado,
    consultar_ventas_por_fecha_filtrado,
)


def obtener_resumen_filtrado(
    ciudad: str | None = None,
    categoria: str | None = None,
    fechaDesde: str | None = None,
    fechaHasta: str | None = None,
    metodoPago: str | None = None,
):
    total_ventas = consultar_total_ventas_filtrado(
        ciudad, categoria, fechaDesde, fechaHasta, metodoPago
    )

    promedio_gasto = consultar_promedio_gasto_filtrado(
        ciudad, categoria, fechaDesde, fechaHasta, metodoPago
    )

    categoria_mas_vendida = consultar_categoria_mas_vendida_filtrada(
        ciudad, categoria, fechaDesde, fechaHasta, metodoPago
    )

    producto_mas_vendido = consultar_producto_mas_vendido_filtrado(
        ciudad, categoria, fechaDesde, fechaHasta, metodoPago
    )

    ciudad_con_mas_compras = consultar_ciudad_con_mas_compras_filtrada(
        ciudad, categoria, fechaDesde, fechaHasta, metodoPago
    )

    metodo_pago_mas_usado = consultar_metodo_pago_mas_usado_filtrado(
        ciudad, categoria, fechaDesde, fechaHasta, metodoPago
    )

    return {
        "filtrosAplicados": {
            "ciudad": ciudad,
            "categoria": categoria,
            "fechaDesde": fechaDesde,
            "fechaHasta": fechaHasta,
            "metodoPago": metodoPago,
        },
        "totalVentas": total_ventas[0]["totalVentas"] if total_ventas else 0,
        "promedioGasto": float(promedio_gasto[0]["promedioGasto"]) if promedio_gasto else 0,
        "categoriaMasVendida": {
            "categoria": categoria_mas_vendida[0]["categoria"],
            "cantidadCompras": categoria_mas_vendida[0]["cantidadCompras"],
        } if categoria_mas_vendida else None,
        "productoMasVendido": {
            "producto": producto_mas_vendido[0]["producto"],
            "cantidadCompras": producto_mas_vendido[0]["cantidadCompras"],
        } if producto_mas_vendido else None,
        "ciudadConMasCompras": {
            "ciudad": ciudad_con_mas_compras[0]["ciudad"],
            "cantidadCompras": ciudad_con_mas_compras[0]["cantidadCompras"],
        } if ciudad_con_mas_compras else None,
        "metodoPagoMasUsado": {
            "metodoPago": metodo_pago_mas_usado[0]["metodopago"],
            "cantidadUsos": metodo_pago_mas_usado[0]["cantidadUsos"],
        } if metodo_pago_mas_usado else None,
    }

def obtener_ventas_por_categoria_filtrado(
    ciudad: str | None = None,
    categoria: str | None = None,
    fechaDesde: str | None = None,
    fechaHasta: str | None = None,
    metodoPago: str | None = None,
):
    resultado = consultar_ventas_por_categoria_filtrado(
        ciudad=ciudad,
        categoria=categoria,
        fechaDesde=fechaDesde,
        fechaHasta=fechaHasta,
        metodoPago=metodoPago,
    )

    return [
        {
            "categoria": fila["categoria"],
            "totalVentas": fila["totalVentas"],
        }
        for fila in resultado
    ]


def obtener_compras_por_ciudad_filtrado(
    ciudad: str | None = None,
    categoria: str | None = None,
    fechaDesde: str | None = None,
    fechaHasta: str | None = None,
    metodoPago: str | None = None,
):
    resultado = consultar_compras_por_ciudad_filtrado(
        ciudad=ciudad,
        categoria=categoria,
        fechaDesde=fechaDesde,
        fechaHasta=fechaHasta,
        metodoPago=metodoPago,
    )

    return [
        {
            "ciudad": fila["ciudad"],
            "cantidadCompras": fila["cantidadCompras"],
        }
        for fila in resultado
    ]


def obtener_metodos_pago_filtrado(
    ciudad: str | None = None,
    categoria: str | None = None,
    fechaDesde: str | None = None,
    fechaHasta: str | None = None,
    metodoPago: str | None = None,
):
    resultado = consultar_metodos_pago_filtrado(
        ciudad=ciudad,
        categoria=categoria,
        fechaDesde=fechaDesde,
        fechaHasta=fechaHasta,
        metodoPago=metodoPago,
    )

    return [
        {
            "metodoPago": fila["metodopago"],
            "cantidadUsos": fila["cantidadUsos"],
        }
        for fila in resultado
    ]
def obtener_productos_mas_vendidos_filtrado(
    ciudad: str | None = None,
    categoria: str | None = None,
    fechaDesde: str | None = None,
    fechaHasta: str | None = None,
    metodoPago: str | None = None,
):
    resultado = consultar_productos_mas_vendidos_filtrado(
        ciudad=ciudad,
        categoria=categoria,
        fechaDesde=fechaDesde,
        fechaHasta=fechaHasta,
        metodoPago=metodoPago,
    )

    return [
        {
            "producto": fila["producto"],
            "cantidadCompras": fila["cantidadCompras"],
        }
        for fila in resultado
    ]


def obtener_compras_por_rango_etario_filtrado(
    ciudad: str | None = None,
    categoria: str | None = None,
    fechaDesde: str | None = None,
    fechaHasta: str | None = None,
    metodoPago: str | None = None,
):
    resultado = consultar_compras_por_rango_etario_filtrado(
        ciudad=ciudad,
        categoria=categoria,
        fechaDesde=fechaDesde,
        fechaHasta=fechaHasta,
        metodoPago=metodoPago,
    )

    return [
        {
            "rangoEtario": fila["rangoEtario"],
            "cantidadCompras": fila["cantidadCompras"],
        }
        for fila in resultado
    ]


def obtener_ventas_por_fecha_filtrado(
    ciudad: str | None = None,
    categoria: str | None = None,
    fechaDesde: str | None = None,
    fechaHasta: str | None = None,
    metodoPago: str | None = None,
):
    resultado = consultar_ventas_por_fecha_filtrado(
        ciudad=ciudad,
        categoria=categoria,
        fechaDesde=fechaDesde,
        fechaHasta=fechaHasta,
        metodoPago=metodoPago,
    )

    return [
        {
            "fecha": str(fila["fecha"]),
            "totalVentas": fila["totalVentas"],
        }
        for fila in resultado
    ]
