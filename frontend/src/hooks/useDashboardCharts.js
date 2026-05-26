import { useEffect, useState } from "react";

import {
  obtenerVentasPorCategoria,
  obtenerComprasPorCiudad,
  obtenerMetodosPago,
  obtenerProductosMasVendidos,
  obtenerComprasPorRangoEtario,
  obtenerVentasPorFecha,
} from "../api/dashboardApi";

import {
  obtenerVentasPorCategoriaFiltrado,
  obtenerComprasPorCiudadFiltrado,
  obtenerMetodosPagoFiltrado,
  obtenerProductosMasVendidosFiltrado,
  obtenerComprasPorRangoEtarioFiltrado,
  obtenerVentasPorFechaFiltrado,
} from "../api/filteredDashboardApi";

import { hayFiltrosActivos } from "../utils/filterUtils";

export function useDashboardCharts() {
  const [ventasPorCategoria, setVentasPorCategoria] = useState([]);
  const [comprasPorCiudad, setComprasPorCiudad] = useState([]);
  const [metodosPago, setMetodosPago] = useState([]);
  const [productosMasVendidos, setProductosMasVendidos] = useState([]);
  const [comprasPorRangoEtario, setComprasPorRangoEtario] = useState([]);
  const [ventasPorFecha, setVentasPorFecha] = useState([]);

  const [cargandoGraficos, setCargandoGraficos] = useState(true);
  const [errorGraficos, setErrorGraficos] = useState("");

  useEffect(() => {
    cargarGraficosGlobales();
  }, []);

  function actualizarDatosGraficos({
    ventasCategoriaData,
    comprasCiudadData,
    metodosPagoData,
    productosMasVendidosData,
    rangoEtarioData,
    ventasFechaData,
  }) {
    setVentasPorCategoria(ventasCategoriaData);
    setComprasPorCiudad(comprasCiudadData);
    setMetodosPago(metodosPagoData);
    setProductosMasVendidos(productosMasVendidosData);
    setComprasPorRangoEtario(rangoEtarioData);
    setVentasPorFecha(ventasFechaData);
  }

  async function cargarGraficosGlobales() {
    try {
      setCargandoGraficos(true);
      setErrorGraficos("");

      const [
        ventasCategoriaData,
        comprasCiudadData,
        metodosPagoData,
        productosMasVendidosData,
        rangoEtarioData,
        ventasFechaData,
      ] = await Promise.all([
        obtenerVentasPorCategoria(),
        obtenerComprasPorCiudad(),
        obtenerMetodosPago(),
        obtenerProductosMasVendidos(),
        obtenerComprasPorRangoEtario(),
        obtenerVentasPorFecha(),
      ]);

      actualizarDatosGraficos({
        ventasCategoriaData,
        comprasCiudadData,
        metodosPagoData,
        productosMasVendidosData,
        rangoEtarioData,
        ventasFechaData,
      });
    } catch (error) {
      setErrorGraficos(error.message);
    } finally {
      setCargandoGraficos(false);
    }
  }

  async function cargarGraficosPorFiltros(filtros) {
    try {
      setCargandoGraficos(true);
      setErrorGraficos("");

      if (!hayFiltrosActivos(filtros)) {
        await cargarGraficosGlobales();
        return;
      }

      const [
        ventasCategoriaData,
        comprasCiudadData,
        metodosPagoData,
        productosMasVendidosData,
        rangoEtarioData,
        ventasFechaData,
      ] = await Promise.all([
        obtenerVentasPorCategoriaFiltrado(filtros),
        obtenerComprasPorCiudadFiltrado(filtros),
        obtenerMetodosPagoFiltrado(filtros),
        obtenerProductosMasVendidosFiltrado(filtros),
        obtenerComprasPorRangoEtarioFiltrado(filtros),
        obtenerVentasPorFechaFiltrado(filtros),
      ]);

      actualizarDatosGraficos({
        ventasCategoriaData,
        comprasCiudadData,
        metodosPagoData,
        productosMasVendidosData,
        rangoEtarioData,
        ventasFechaData,
      });
    } catch (error) {
      setErrorGraficos(error.message);
    } finally {
      setCargandoGraficos(false);
    }
  }

  return {
    ventasPorCategoria,
    comprasPorCiudad,
    metodosPago,
    productosMasVendidos,
    comprasPorRangoEtario,
    ventasPorFecha,
    cargandoGraficos,
    errorGraficos,
    cargarGraficosGlobales,
    cargarGraficosPorFiltros,
  };
}