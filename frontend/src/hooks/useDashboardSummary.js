import { useEffect, useState } from "react";
import { obtenerResumenDashboard } from "../api/dashboardApi";
import { obtenerResumenFiltrado } from "../api/filteredDashboardApi";
import { hayFiltrosActivos } from "../utils/filterUtils";

export function useDashboardSummary() {
  const [resumen, setResumen] = useState(null);
  const [cargandoResumen, setCargandoResumen] = useState(true);
  const [errorResumen, setErrorResumen] = useState("");

  useEffect(() => {
    cargarResumenGlobal();
  }, []);

  async function cargarResumenGlobal() {
    try {
      setCargandoResumen(true);
      setErrorResumen("");

      const resumenData = await obtenerResumenDashboard();
      setResumen(resumenData);
    } catch (error) {
      setErrorResumen(error.message);
    } finally {
      setCargandoResumen(false);
    }
  }

  async function cargarResumenPorFiltros(filtros) {
    try {
      setCargandoResumen(true);
      setErrorResumen("");

      if (hayFiltrosActivos(filtros)) {
        const resumenData = await obtenerResumenFiltrado(filtros);
        setResumen(resumenData);
      } else {
        const resumenData = await obtenerResumenDashboard();
        setResumen(resumenData);
      }
    } catch (error) {
      setErrorResumen(error.message);
    } finally {
      setCargandoResumen(false);
    }
  }

  return {
    resumen,
    cargandoResumen,
    errorResumen,
    cargarResumenGlobal,
    cargarResumenPorFiltros,
  };
}