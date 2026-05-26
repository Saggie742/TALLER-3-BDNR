import { useEffect, useState } from "react";
import { obtenerEstadoImportacion } from "../api/dashboardApi";

export function useDashboardBase() {
  const [estadoImportacion, setEstadoImportacion] = useState(null);
  const [cargandoBase, setCargandoBase] = useState(true);
  const [errorBase, setErrorBase] = useState("");

  useEffect(() => {
    async function cargarDatosBase() {
      try {
        setCargandoBase(true);
        setErrorBase("");

        const estadoData = await obtenerEstadoImportacion();
        setEstadoImportacion(estadoData);
      } catch (error) {
        setErrorBase(error.message);
      } finally {
        setCargandoBase(false);
      }
    }

    cargarDatosBase();
  }, []);

  return {
    estadoImportacion,
    cargandoBase,
    errorBase,
  };
}