import { formatearNumero } from "../utils/formatters";

function EstadoImportacion({ estado }) {
  if (!estado) {
    return null;
  }

  return (
    <section className="import-status">
      <div className="status-item">
        <span>Registros</span>
        <strong>{formatearNumero(estado.totalRegistros)}</strong>
      </div>

      <div className="status-item">
        <span>Fechas</span>
        <strong>
          {estado.fechaMinima} / {estado.fechaMaxima}
        </strong>
      </div>

      <div className="status-item">
        <span>Ciudades</span>
        <strong>{formatearNumero(estado.totalCiudades)}</strong>
      </div>

      <div className="status-item">
        <span>Categorías</span>
        <strong>{formatearNumero(estado.totalCategorias)}</strong>
      </div>

      <div className="status-item">
        <span>Productos</span>
        <strong>{formatearNumero(estado.totalProductos)}</strong>
      </div>

      <div className="status-item">
        <span>Métodos</span>
        <strong>{formatearNumero(estado.totalMetodosPago)}</strong>
      </div>
    </section>
  );
}

export default EstadoImportacion;