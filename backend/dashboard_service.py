from dashboard_queries import (
    consultar_estado_importacion,
    consultar_total_ventas,
    consultar_promedio_gasto,
    consultar_categoria_mas_vendida,
    consultar_producto_mas_vendido,
    consultar_ciudad_con_mas_compras,
    consultar_metodo_pago_mas_usado,
    consultar_ventas_por_categoria,
    consultar_compras_por_ciudad,
    consultar_metodos_pago,
    consultar_productos_mas_vendidos,
    consultar_compras_por_rango_etario,
    consultar_ventas_por_fecha,
    consultar_ciudades_disponibles,
    consultar_categorias_disponibles,
    consultar_metodos_pago_disponibles,
    consultar_rango_fechas_disponible,
)

def obtener_estado_importacion():
    resultado = consultar_estado_importacion()

    if not resultado:
        return {
            "totalRegistros": 0,
            "fechaMinima": None,
            "fechaMaxima": None,
            "totalCiudades": 0,
            "totalCategorias": 0,
            "totalProductos": 0,
            "totalMetodosPago": 0,
        }

    fila = resultado[0]

    return {
        "totalRegistros": fila["totalRegistros"],
        "fechaMinima": str(fila["fechaMinima"]),
        "fechaMaxima": str(fila["fechaMaxima"]),
        "totalCiudades": fila["totalCiudades"],
        "totalCategorias": fila["totalCategorias"],
        "totalProductos": fila["totalProductos"],
        "totalMetodosPago": fila["totalMetodosPago"],
    }


def obtener_resumen_dashboard():
    total_ventas = consultar_total_ventas()
    promedio_gasto = consultar_promedio_gasto()
    categoria_mas_vendida = consultar_categoria_mas_vendida()
    producto_mas_vendido = consultar_producto_mas_vendido()
    ciudad_con_mas_compras = consultar_ciudad_con_mas_compras()
    metodo_pago_mas_usado = consultar_metodo_pago_mas_usado()

    return {
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

def obtener_ventas_por_categoria():
    resultado = consultar_ventas_por_categoria()

    return [
        {
            "categoria": fila["categoria"],
            "totalVentas": fila["totalVentas"],
        }
        for fila in resultado
    ]


def obtener_compras_por_ciudad():
    resultado = consultar_compras_por_ciudad()

    return [
        {
            "ciudad": fila["ciudad"],
            "cantidadCompras": fila["cantidadCompras"],
        }
        for fila in resultado
    ]


def obtener_metodos_pago():
    resultado = consultar_metodos_pago()

    return [
        {
            "metodoPago": fila["metodopago"],
            "cantidadUsos": fila["cantidadUsos"],
        }
        for fila in resultado
    ]

def obtener_productos_mas_vendidos():
    resultado = consultar_productos_mas_vendidos()

    return [
        {
            "producto": fila["producto"],
            "cantidadCompras": fila["cantidadCompras"],
        }
        for fila in resultado
    ]


def obtener_compras_por_rango_etario():
    resultado = consultar_compras_por_rango_etario()

    return [
        {
            "rangoEtario": fila["rangoEtario"],
            "cantidadCompras": fila["cantidadCompras"],
        }
        for fila in resultado
    ]


def obtener_ventas_por_fecha():
    resultado = consultar_ventas_por_fecha()

    return [
        {
            "fecha": str(fila["fecha"]),
            "totalVentas": fila["totalVentas"],
        }
        for fila in resultado
    ]
def obtener_opciones_filtros():
    ciudades = consultar_ciudades_disponibles()
    categorias = consultar_categorias_disponibles()
    metodos_pago = consultar_metodos_pago_disponibles()
    rango_fechas = consultar_rango_fechas_disponible()

    fechas = rango_fechas[0] if rango_fechas else None

    return {
        "ciudades": [
            fila["ciudad"]
            for fila in ciudades
        ],
        "categorias": [
            fila["categoria"]
            for fila in categorias
        ],
        "metodosPago": [
            fila["metodopago"]
            for fila in metodos_pago
        ],
        "fechaMinima": str(fechas["fechaMinima"]) if fechas else None,
        "fechaMaxima": str(fechas["fechaMaxima"]) if fechas else None,
    }