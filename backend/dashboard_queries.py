from database import execute_query


def consultar_estado_importacion():
    query = """
        SELECT
            COUNT(*) AS totalRegistros,
            MIN(fecha) AS fechaMinima,
            MAX(fecha) AS fechaMaxima,
            COUNT(DISTINCT ciudad) AS totalCiudades,
            COUNT(DISTINCT categoria) AS totalCategorias,
            COUNT(DISTINCT producto) AS totalProductos,
            COUNT(DISTINCT metodopago) AS totalMetodosPago
        FROM compras;
    """

    return execute_query(query)


def consultar_total_ventas():
    query = """
        SELECT
            SUM(precio) AS totalVentas
        FROM compras;
    """

    return execute_query(query)


def consultar_promedio_gasto():
    query = """
        SELECT
            AVG(precio) AS promedioGasto
        FROM compras;
    """

    return execute_query(query)


def consultar_categoria_mas_vendida():
    query = """
        SELECT
            categoria,
            COUNT(*) AS cantidadCompras
        FROM compras
        GROUP BY categoria
        ORDER BY cantidadCompras DESC
        LIMIT 1;
    """

    return execute_query(query)


def consultar_producto_mas_vendido():
    query = """
        SELECT
            producto,
            COUNT(*) AS cantidadCompras
        FROM compras
        GROUP BY producto
        ORDER BY cantidadCompras DESC
        LIMIT 1;
    """

    return execute_query(query)


def consultar_ciudad_con_mas_compras():
    query = """
        SELECT
            ciudad,
            COUNT(*) AS cantidadCompras
        FROM compras
        GROUP BY ciudad
        ORDER BY cantidadCompras DESC
        LIMIT 1;
    """

    return execute_query(query)


def consultar_metodo_pago_mas_usado():
    query = """
        SELECT
            metodopago,
            COUNT(*) AS cantidadUsos
        FROM compras
        GROUP BY metodopago
        ORDER BY cantidadUsos DESC
        LIMIT 1;
    """

    return execute_query(query)

def consultar_ventas_por_categoria():
    query = """
        SELECT
            categoria,
            SUM(precio) AS totalVentas
        FROM compras
        GROUP BY categoria
        ORDER BY totalVentas DESC;
    """

    return execute_query(query)


def consultar_compras_por_ciudad():
    query = """
        SELECT
            ciudad,
            COUNT(*) AS cantidadCompras
        FROM compras
        GROUP BY ciudad
        ORDER BY cantidadCompras DESC;
    """

    return execute_query(query)


def consultar_metodos_pago():
    query = """
        SELECT
            metodopago,
            COUNT(*) AS cantidadUsos
        FROM compras
        GROUP BY metodopago
        ORDER BY cantidadUsos DESC;
    """

    return execute_query(query)

def consultar_productos_mas_vendidos():
    query = """
        SELECT
            producto,
            COUNT(*) AS cantidadCompras
        FROM compras
        GROUP BY producto
        ORDER BY cantidadCompras DESC
        LIMIT 10;
    """

    return execute_query(query)


def consultar_compras_por_rango_etario():
    query = """
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

    return execute_query(query)

def consultar_ventas_por_fecha():
    query = """
        SELECT
            fecha,
            SUM(precio) AS totalVentas
        FROM compras
        GROUP BY fecha
        ORDER BY fecha ASC;
    """

    return execute_query(query)
def consultar_ciudades_disponibles():
    query = """
        SELECT
            ciudad
        FROM compras
        GROUP BY ciudad
        ORDER BY ciudad;
    """

    return execute_query(query)


def consultar_categorias_disponibles():
    query = """
        SELECT
            categoria
        FROM compras
        GROUP BY categoria
        ORDER BY categoria;
    """

    return execute_query(query)


def consultar_metodos_pago_disponibles():
    query = """
        SELECT
            metodopago
        FROM compras
        GROUP BY metodopago
        ORDER BY metodopago;
    """

    return execute_query(query)

def consultar_rango_fechas_disponible():
    query = """
        SELECT
            MIN(fecha) AS fechaMinima,
            MAX(fecha) AS fechaMaxima
        FROM compras;
    """

    return execute_query(query)
