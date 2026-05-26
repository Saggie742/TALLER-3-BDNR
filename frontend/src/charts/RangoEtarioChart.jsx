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

import { formatearNumero } from "../utils/formatters";

const coloresRangos = [
  "#2563eb",
  "#16a34a",
  "#f97316",
  "#9333ea",
  "#dc2626",
];

function RangoEtarioChart({ data }) {
  if (!data || data.length === 0) {
    return <p>No hay datos de compras por rango etario.</p>;
  }

  return (
    <ResponsiveContainer width="100%" height={320}>
      <BarChart data={data} margin={{ top: 10, right: 24, left: 24, bottom: 10 }}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="rangoEtario" />
        <YAxis tickFormatter={formatearNumero} width={80} />
        <Tooltip formatter={(value) => [formatearNumero(value), "Compras"]} />
        <Bar dataKey="cantidadCompras" name="Compras">
          {data.map((_, index) => (
            <Cell
              key={`cell-rango-${index}`}
              fill={coloresRangos[index % coloresRangos.length]}
            />
          ))}
        </Bar>
      </BarChart>
    </ResponsiveContainer>
  );
}

export default RangoEtarioChart;