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

const coloresCiudades = [
  "#2563eb",
  "#16a34a",
  "#f97316",
  "#9333ea",
  "#dc2626",
  "#0891b2",
  "#ca8a04",
  "#4f46e5",
  "#be123c",
  "#15803d",
];

function ComprasCiudadChart({ data }) {
  if (!data || data.length === 0) {
    return <p>No hay datos de compras por ciudad.</p>;
  }

  return (
    <ResponsiveContainer width="100%" height={360}>
      <BarChart
        data={data}
        layout="vertical"
        margin={{ top: 10, right: 24, left: 40, bottom: 10 }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis type="number" tickFormatter={formatearNumero} />
        <YAxis dataKey="ciudad" type="category" width={110} />
        <Tooltip
          formatter={(value) => [formatearNumero(value), "Compras"]}
        />
        <Bar dataKey="cantidadCompras" name="Compras">
          {data.map((_, index) => (
            <Cell
              key={`cell-ciudad-${index}`}
              fill={coloresCiudades[index % coloresCiudades.length]}
            />
          ))}
        </Bar>
      </BarChart>
    </ResponsiveContainer>
  );
}

export default ComprasCiudadChart;