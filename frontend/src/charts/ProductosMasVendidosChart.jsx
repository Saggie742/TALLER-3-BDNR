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

const coloresProductos = [
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

function ProductosMasVendidosChart({ data }) {
  if (!data || data.length === 0) {
    return <p>No hay datos de productos más vendidos.</p>;
  }

  return (
    <ResponsiveContainer width="100%" height={420}>
      <BarChart
        data={data}
        layout="vertical"
        margin={{ top: 10, right: 24, left: 60, bottom: 10 }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis type="number" tickFormatter={formatearNumero} />
        <YAxis dataKey="producto" type="category" width={130} />
        <Tooltip
          formatter={(value) => [formatearNumero(value), "Compras"]}
        />
        <Bar dataKey="cantidadCompras" name="Compras">
          {data.map((_, index) => (
            <Cell
              key={`cell-producto-${index}`}
              fill={coloresProductos[index % coloresProductos.length]}
            />
          ))}
        </Bar>
      </BarChart>
    </ResponsiveContainer>
  );
}

export default ProductosMasVendidosChart;