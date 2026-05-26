import { useEffect } from "react";

import ChartsSection from "../components/ChartsSection";
import DashboardHeader from "../components/DashboardHeader";
import EstadoImportacion from "../components/EstadoImportacion";
import ErrorMessage from "../components/ErrorMessage";
import FilterPanel from "../components/FilterPanel";
import KpiGrid from "../components/KpiGrid";
import LoadingMessage from "../components/LoadingMessage";

import { useDashboardBase } from "../hooks/useDashboardBase";
import { useDashboardCharts } from "../hooks/useDashboardCharts";
import { useDashboardFilters } from "../hooks/useDashboardFilters";
import { useDashboardSummary } from "../hooks/useDashboardSummary";

function DashboardPage() {
  const { estadoImportacion, cargandoBase, errorBase } = useDashboardBase();

  const {
    resumen,
    cargandoResumen,
    errorResumen,
    cargarResumenPorFiltros,
  } = useDashboardSummary();

  const {
    ventasPorCategoria,
    comprasPorCiudad,
    metodosPago,
    productosMasVendidos,
    comprasPorRangoEtario,
    ventasPorFecha,
    cargandoGraficos,
    errorGraficos,
    cargarGraficosPorFiltros,
  } = useDashboardCharts();

  const {
    opcionesFiltros,
    filtrosFormulario,
    filtrosAplicados,
    cargandoFiltros,
    errorFiltros,
    actualizarFiltro,
    aplicarFiltros,
    limpiarFiltros,
    hayFiltrosAplicados,
  } = useDashboardFilters();

  useEffect(() => {
    cargarResumenPorFiltros(filtrosAplicados);
    cargarGraficosPorFiltros(filtrosAplicados);
  }, [filtrosAplicados]);

  if (cargandoBase || cargandoResumen) {
    return <LoadingMessage />;
  }

  if (errorBase) {
    return <ErrorMessage mensaje={errorBase} />;
  }

  if (errorResumen) {
    return <ErrorMessage mensaje={errorResumen} />;
  }

  return (
    <main className="page">
      <DashboardHeader />

      <EstadoImportacion estado={estadoImportacion} />

      <FilterPanel
        opcionesFiltros={opcionesFiltros}
        filtrosFormulario={filtrosFormulario}
        cargandoFiltros={cargandoFiltros}
        errorFiltros={errorFiltros}
        actualizarFiltro={actualizarFiltro}
        aplicarFiltros={aplicarFiltros}
        limpiarFiltros={limpiarFiltros}
        hayFiltrosAplicados={hayFiltrosAplicados}
      />

      <KpiGrid resumen={resumen} />

      <ChartsSection
        ventasPorCategoria={ventasPorCategoria}
        comprasPorCiudad={comprasPorCiudad}
        metodosPago={metodosPago}
        productosMasVendidos={productosMasVendidos}
        comprasPorRangoEtario={comprasPorRangoEtario}
        ventasPorFecha={ventasPorFecha}
        cargandoGraficos={cargandoGraficos}
        errorGraficos={errorGraficos}
      />
    </main>
  );
}

export default DashboardPage;