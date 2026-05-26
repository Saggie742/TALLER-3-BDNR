function KpiCard({ titulo, valor, detalle }) {
  return (
    <div className="kpi-card">
      <p className="kpi-title">{titulo}</p>
      <h2 className="kpi-value">{valor}</h2>
      {detalle && <p className="kpi-detail">{detalle}</p>}
    </div>
  );
}

export default KpiCard;