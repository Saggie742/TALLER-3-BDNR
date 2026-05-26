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

const coloresMetodos = [
  "#2563eb",
  "#16a34a",
  "#f97316",
  "#9333ea",
];

function MetodosPagoChart({ data }) {
  if (!data || data.length === 0) {
    return <p>No hay datos de métodos de pago.</p>;
  }

  return (
    <ResponsiveContainer width="100%" height={320}>
      <BarChart data={data} margin={{ top: 10, right: 24, left: 24, bottom: 10 }}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="metodoPago" />
        <YAxis tickFormatter={formatearNumero} width={80} />
        <Tooltip
          formatter={(value) => [formatearNumero(value), "Usos"]}
        />
        <Bar dataKey="cantidadUsos" name="Usos">
          {data.map((_, index) => (
            <Cell
              key={`cell-metodo-${index}`}
              fill={coloresMetodos[index % coloresMetodos.length]}
            />
          ))}
        </Bar>
      </BarChart>
    </ResponsiveContainer>
  );
}

export default MetodosPagoChart;