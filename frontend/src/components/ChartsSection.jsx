import ChartCard from "./ChartCard";

import ComprasCiudadChart from "../charts/ComprasCiudadChart";
import MetodosPagoChart from "../charts/MetodosPagoChart";
import ProductosMasVendidosChart from "../charts/ProductosMasVendidosChart";
import RangoEtarioChart from "../charts/RangoEtarioChart";
import VentasCategoriaChart from "../charts/VentasCategoriaChart";
import VentasFechaChart from "../charts/VentasFechaChart";

function ChartsSection({
  ventasPorCategoria,
  comprasPorCiudad,
  metodosPago,
  productosMasVendidos,
  comprasPorRangoEtario,
  ventasPorFecha,
  cargandoGraficos,
  errorGraficos,
}) {
  return (
    <section className="charts-grid">
      <ChartCard titulo="Ventas por categoría">
        {cargandoGraficos && <p>Cargando gráfico...</p>}
        {errorGraficos && <p className="error">{errorGraficos}</p>}
        {!cargandoGraficos && !errorGraficos && (
          <VentasCategoriaChart data={ventasPorCategoria} />
        )}
      </ChartCard>

      <ChartCard titulo="Compras por ciudad">
        {cargandoGraficos && <p>Cargando gráfico...</p>}
        {errorGraficos && <p className="error">{errorGraficos}</p>}
        {!cargandoGraficos && !errorGraficos && (
          <ComprasCiudadChart data={comprasPorCiudad} />
        )}
      </ChartCard>

      <ChartCard titulo="Métodos de pago">
        {cargandoGraficos && <p>Cargando gráfico...</p>}
        {errorGraficos && <p className="error">{errorGraficos}</p>}
        {!cargandoGraficos && !errorGraficos && (
          <MetodosPagoChart data={metodosPago} />
        )}
      </ChartCard>

      <ChartCard titulo="Productos más vendidos">
        {cargandoGraficos && <p>Cargando gráfico...</p>}
        {errorGraficos && <p className="error">{errorGraficos}</p>}
        {!cargandoGraficos && !errorGraficos && (
          <ProductosMasVendidosChart data={productosMasVendidos} />
        )}
      </ChartCard>

      <ChartCard titulo="Compras por rango etario">
        {cargandoGraficos && <p>Cargando gráfico...</p>}
        {errorGraficos && <p className="error">{errorGraficos}</p>}
        {!cargandoGraficos && !errorGraficos && (
          <RangoEtarioChart data={comprasPorRangoEtario} />
        )}
      </ChartCard>

      <div className="chart-span-full">
        <ChartCard titulo="Ventas por fecha">
          {cargandoGraficos && <p>Cargando gráfico...</p>}
          {errorGraficos && <p className="error">{errorGraficos}</p>}
          {!cargandoGraficos && !errorGraficos && (
            <VentasFechaChart data={ventasPorFecha} />
          )}
        </ChartCard>
      </div>
    </section>
  );
}

export default ChartsSection;