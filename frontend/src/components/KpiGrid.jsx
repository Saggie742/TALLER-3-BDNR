import KpiCard from "./KpiCard";
import { formatearMonto, formatearNumero } from "../utils/formatters";

function KpiGrid({ resumen }) {
  if (!resumen) {
    return null;
  }

  return (
    <section className="kpi-grid">
      <KpiCard
        titulo="Total ventas"
        valor={formatearMonto(resumen.totalVentas)}
      />

      <KpiCard
        titulo="Promedio gasto"
        valor={formatearMonto(resumen.promedioGasto)}
      />

      <KpiCard
        titulo="Categoría top"
        valor={resumen.categoriaMasVendida?.categoria ?? "Sin datos"}
        detalle={`${formatearNumero(
          resumen.categoriaMasVendida?.cantidadCompras
        )} compras`}
      />

      <KpiCard
        titulo="Producto top"
        valor={resumen.productoMasVendido?.producto ?? "Sin datos"}
        detalle={`${formatearNumero(
          resumen.productoMasVendido?.cantidadCompras
        )} compras`}
      />

      <KpiCard
        titulo="Ciudad top"
        valor={resumen.ciudadConMasCompras?.ciudad ?? "Sin datos"}
        detalle={`${formatearNumero(
          resumen.ciudadConMasCompras?.cantidadCompras
        )} compras`}
      />

      <KpiCard
        titulo="Método top"
        valor={resumen.metodoPagoMasUsado?.metodoPago ?? "Sin datos"}
        detalle={`${formatearNumero(
          resumen.metodoPagoMasUsado?.cantidadUsos
        )} usos`}
      />
    </section>
  );
}

export default KpiGrid;