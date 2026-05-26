import {
  Bar,
  BarChart,
  CartesianGrid,
  Cell,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

import { formatearMonto, formatearMontoCompacto } from "../utils/formatters";

const coloresCategorias = [
  "#2563eb",
  "#16a34a",
  "#f97316",
  "#9333ea",
  "#dc2626",
];

function VentasCategoriaChart({ data }) {
  if (!data || data.length === 0) {
    return <p>No hay datos de ventas por categoría.</p>;
  }

  return (
    <ResponsiveContainer width="100%" height={320}>
      <BarChart data={data} margin={{ top: 10, right: 24, left: 24, bottom: 10 }}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="categoria" />
        <YAxis
          tickFormatter={formatearMontoCompacto}
          width={80}
        />
        <Tooltip
          formatter={(value) => [formatearMonto(value), "Total ventas"]}
        />
        <Bar dataKey="totalVentas" name="Total ventas">
          {data.map((_, index) => (
            <Cell
              key={`cell-${index}`}
              fill={coloresCategorias[index % coloresCategorias.length]}
            />
          ))}
        </Bar>
      </BarChart>
    </ResponsiveContainer>
  );
}

export default VentasCategoriaChart;