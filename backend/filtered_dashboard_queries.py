from typing import Any

from database import execute_query
from filters import construir_filtros


def consultar_total_ventas_filtrado(
    ciudad: str | None = None,
    categoria: str | None = None,
    fechaDesde: str | None = None,
    fechaHasta: str | None = None,
    metodoPago: str | None = None,
):
    where_clause, params = construir_filtros(
        ciudad=ciudad,
        categoria=categoria,
        fechaDesde=fechaDesde,
        fechaHasta=fechaHasta,
        metodoPago=metodoPago,
    )

    query = f"""
        SELECT
            COALESCE(SUM(precio), 0) AS totalVentas
        FROM compras
        {where_clause};
    """

    return execute_query(query, params)


def consultar_promedio_gasto_filtrado(
    ciudad: str | None = None,
    categoria: str | None = None,
    fechaDesde: str | None = None,
    fechaHasta: str | None = None,
    metodoPago: str | None = None,
):
    where_clause, params = construir_filtros(
        ciudad=ciudad,
        categoria=categoria,
        fechaDesde=fechaDesde,
        fechaHasta=fechaHasta,
        metodoPago=metodoPago,
    )

    query = f"""
        SELECT
            COALESCE(AVG(precio), 0) AS promedioGasto
        FROM compras
        {where_clause};
    """

    return execute_query(query, params)


def consultar_categoria_mas_vendida_filtrada(
    ciudad: str | None = None,
    categoria: str | None = None,
    fechaDesde: str | None = None,
    fechaHasta: str | None = None,
    metodoPago: str | None = None,
):
    where_clause, params = construir_filtros(
        ciudad=ciudad,
        categoria=categoria,
        fechaDesde=fechaDesde,
        fechaHasta=fechaHasta,
        metodoPago=metodoPago,
    )

    query = f"""
        SELECT
            categoria,
            COUNT(*) AS cantidadCompras
        FROM compras
        {where_clause}
        GROUP BY categoria
        ORDER BY cantidadCompras DESC
        LIMIT 1;
    """

    return execute_query(query, params)


def consultar_producto_mas_vendido_filtrado(
    ciudad: str | None = None,
    categoria: str | None = None,
    fechaDesde: str | None = None,
    fechaHasta: str | None = None,
    metodoPago: str | None = None,
):
    where_clause, params = construir_filtros(
        ciudad=ciudad,
        categoria=categoria,
        fechaDesde=fechaDesde,
        fechaHasta=fechaHasta,
        metodoPago=metodoPago,
    )

    query = f"""
        SELECT
            producto,
            COUNT(*) AS cantidadCompras
        FROM compras
        {where_clause}
        GROUP BY producto
        ORDER BY cantidadCompras DESC
        LIMIT 1;
    """

    return execute_query(query, params)


def consultar_ciudad_con_mas_compras_filtrada(
    ciudad: str | None = None,
    categoria: str | None = None,
    fechaDesde: str | None = None,
    fechaHasta: str | None = None,
    metodoPago: str | None = None,
):
    where_clause, params = construir_filtros(
        ciudad=ciudad,
        categoria=categoria,
        fechaDesde=fechaDesde,
        fechaHasta=fechaHasta,
        metodoPago=metodoPago,
    )

    query = f"""
        SELECT
            ciudad,
            COUNT(*) AS cantidadCompras
        FROM compras
        {where_clause}
        GROUP BY ciudad
        ORDER BY cantidadCompras DESC
        LIMIT 1;
    """

    return execute_query(query, params)


def consultar_metodo_pago_mas_usado_filtrado(
    ciudad: str | None = None,
    categoria: str | None = None,
    fechaDesde: str | None = None,
    fechaHasta: str | None = None,
    metodoPago: str | None = None,
):
    where_clause, params = construir_filtros(
        ciudad=ciudad,
        categoria=categoria,
        fechaDesde=fechaDesde,
        fechaHasta=fechaHasta,
        metodoPago=metodoPago,
    )

    query = f"""
        SELECT
            metodopago,
            COUNT(*) AS cantidadUsos
        FROM compras
        {where_clause}
        GROUP BY metodopago
        ORDER BY cantidadUsos DESC
        LIMIT 1;
    """

    return execute_query(query, params)

def consultar_ventas_por_categoria_filtrado(
    ciudad: str | None = None,
    categoria: str | None = None,
    fechaDesde: str | None = None,
    fechaHasta: str | None = None,
    metodoPago: str | None = None,
):
    where_clause, params = construir_filtros(
        ciudad=ciudad,
        categoria=categoria,
        fechaDesde=fechaDesde,
        fechaHasta=fechaHasta,
        metodoPago=metodoPago,
    )

    query = f"""
        SELECT
            categoria,
            SUM(precio) AS totalVentas
        FROM compras
        {where_clause}
        GROUP BY categoria
        ORDER BY totalVentas DESC;
    """

    return execute_query(query, params)


def consultar_compras_por_ciudad_filtrado(
    ciudad: str | None = None,
    categoria: str | None = None,
    fechaDesde: str | None = None,
    fechaHasta: str | None = None,
    metodoPago: str | None = None,
):
    where_clause, params = construir_filtros(
        ciudad=ciudad,
        categoria=categoria,
        fechaDesde=fechaDesde,
        fechaHasta=fechaHasta,
        metodoPago=metodoPago,
    )

    query = f"""
        SELECT
            ciudad,
            COUNT(*) AS cantidadCompras
        FROM compras
        {where_clause}
        GROUP BY ciudad
        ORDER BY cantidadCompras DESC;
    """

    return execute_query(query, params)


def consultar_metodos_pago_filtrado(
    ciudad: str | None = None,
    categoria: str | None = None,
    fechaDesde: str | None = None,
    fechaHasta: str | None = None,
    metodoPago: str | None = None,
):
    where_clause, params = construir_filtros(
        ciudad=ciudad,
        categoria=categoria,
        fechaDesde=fechaDesde,
        fechaHasta=fechaHasta,
        metodoPago=metodoPago,
    )

    query = f"""
        SELECT
            metodopago,
            COUNT(*) AS cantidadUsos
        FROM compras
        {where_clause}
        GROUP BY metodopago
        ORDER BY cantidadUsos DESC;
    """

    return execute_query(query, params)

def consultar_productos_mas_vendidos_filtrado(
    ciudad: str | None = None,
    categoria: str | None = None,
    fechaDesde: str | None = None,
    fechaHasta: str | None = None,
    metodoPago: str | None = None,
):
    where_clause, params = construir_filtros(
        ciudad=ciudad,
        categoria=categoria,
        fechaDesde=fechaDesde,
        fechaHasta=fechaHasta,
        metodoPago=metodoPago,
    )

    query = f"""
        SELECT
            producto,
            COUNT(*) AS cantidadCompras
        FROM compras
        {where_clause}
        GROUP BY producto
        ORDER BY cantidadCompras DESC
        LIMIT 10;
    """

    return execute_query(query, params)


def consultar_compras_por_rango_etario_filtrado(
    ciudad: str | None = None,
    categoria: str | None = None,
    fechaDesde: str | None = None,
    fechaHasta: str | None = None,
    metodoPago: str | None = None,
):
    where_clause, params = construir_filtros(
        ciudad=ciudad,
        categoria=categoria,
        fechaDesde=fechaDesde,
        fechaHasta=fechaHasta,
        metodoPago=metodoPago,
    )

    query = f"""
        SELECT
            CASE
                WHEN edad BETWEEN 18 AND 25 THEN '18-25'
                WHEN edad BETWEEN 26 AND 35 THEN '26-35'
                WHEN edad BETWEEN 36 AND 45 THEN '36-45'
                WHEN edad BETWEEN 46 AND 55 THEN '46-55'
                WHEN edad BETWEEN 56 AND 70 THEN '56-70'
                ELSE 'Otro'
            END AS rangoEtario,
            COUNT(*) AS cantidadCompras
        FROM compras
        {where_clause}
        GROUP BY rangoEtario
        ORDER BY
            CASE rangoEtario
                WHEN '18-25' THEN 1
                WHEN '26-35' THEN 2
                WHEN '36-45' THEN 3
                WHEN '46-55' THEN 4
                WHEN '56-70' THEN 5
                ELSE 6
            END;
    """

    return execute_query(query, params)

def consultar_ventas_por_fecha_filtrado(
    ciudad: str | None = None,
    categoria: str | None = None,
    fechaDesde: str | None = None,
    fechaHasta: str | None = None,
    metodoPago: str | None = None,
):
    where_clause, params = construir_filtros(
        ciudad=ciudad,
        categoria=categoria,
        fechaDesde=fechaDesde,
        fechaHasta=fechaHasta,
        metodoPago=metodoPago,
    )

    query = f"""
    SELECT
        fecha,
        SUM(precio) AS totalVentas
    FROM compras
    {where_clause}
    GROUP BY fecha
    ORDER BY fecha ASC;
    """

    return execute_query(query, params)
