import { useEffect, useState } from "react";
import { obtenerOpcionesFiltros } from "../api/dashboardApi";
import { filtrosIniciales, hayFiltrosActivos } from "../utils/filterUtils";

export function useDashboardFilters() {
  const [opcionesFiltros, setOpcionesFiltros] = useState(null);
  const [filtrosFormulario, setFiltrosFormulario] = useState(filtrosIniciales);
  const [filtrosAplicados, setFiltrosAplicados] = useState(filtrosIniciales);

  const [cargandoFiltros, setCargandoFiltros] = useState(true);
  const [errorFiltros, setErrorFiltros] = useState("");

  useEffect(() => {
    async function cargarOpcionesFiltros() {
      try {
        setCargandoFiltros(true);
        setErrorFiltros("");

        const data = await obtenerOpcionesFiltros();
        setOpcionesFiltros(data);
      } catch (error) {
        setErrorFiltros(error.message);
      } finally {
        setCargandoFiltros(false);
      }
    }

    cargarOpcionesFiltros();
  }, []);

  function actualizarFiltro(nombre, valor) {
    setFiltrosFormulario((prev) => ({
      ...prev,
      [nombre]: valor,
    }));
  }

  function aplicarFiltros() {
    setFiltrosAplicados(filtrosFormulario);
  }

  function limpiarFiltros() {
    setFiltrosFormulario(filtrosIniciales);
    setFiltrosAplicados(filtrosIniciales);
  }

  return {
    opcionesFiltros,
    filtrosFormulario,
    filtrosAplicados,
    cargandoFiltros,
    errorFiltros,
    actualizarFiltro,
    aplicarFiltros,
    limpiarFiltros,
    hayFiltrosAplicados: hayFiltrosActivos(filtrosAplicados),
  };
}