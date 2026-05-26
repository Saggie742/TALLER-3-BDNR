import {
  CartesianGrid,
  Line,
  LineChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

import { formatearMonto, formatearMontoCompacto } from "../utils/formatters";

function VentasFechaChart({ data }) {
  if (!data || data.length === 0) {
    return <p>No hay datos de ventas por fecha.</p>;
  }

  return (
    <ResponsiveContainer width="100%" height={340}>
      <LineChart data={data} margin={{ top: 10, right: 24, left: 24, bottom: 10 }}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="fecha" minTickGap={32} />
        <YAxis tickFormatter={formatearMontoCompacto} width={80} />
        <Tooltip formatter={(value) => [formatearMonto(value), "Total ventas"]} />
        <Line
          type="monotone"
          dataKey="totalVentas"
          name="Total ventas"
          stroke="#2563eb"
          strokeWidth={2}
          dot={false}
        />
      </LineChart>
    </ResponsiveContainer>
  );
}

export default VentasFechaChart;