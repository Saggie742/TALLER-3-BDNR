function ChartCard({ titulo, children }) {
  return (
    <section className="chart-card">
      <h2>{titulo}</h2>
      <div className="chart-content">{children}</div>
    </section>
  );
}

export default ChartCard;