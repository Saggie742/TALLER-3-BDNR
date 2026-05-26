function FilterPanel({
  opcionesFiltros,
  filtrosFormulario,
  cargandoFiltros,
  errorFiltros,
  actualizarFiltro,
  aplicarFiltros,
  limpiarFiltros,
  hayFiltrosAplicados,
}) {
  if (cargandoFiltros) {
    return (
      <section className="filter-panel">
        <p>Cargando filtros...</p>
      </section>
    );
  }

  if (errorFiltros) {
    return (
      <section className="filter-panel">
        <p className="error">{errorFiltros}</p>
      </section>
    );
  }

  if (!opcionesFiltros) {
    return null;
  }

  return (
    <section className="filter-panel">
      <div className="filter-header">
        <div>
          <h2>Filtros dinámicos</h2>
          <p className="filter-date-help">
            Rango disponible: {opcionesFiltros.fechaMinima} a{" "}
            {opcionesFiltros.fechaMaxima}
          </p>
        </div>

        {hayFiltrosAplicados && (
          <span className="filter-badge">Filtros aplicados</span>
        )}
      </div>

      <div className="filter-grid">
        <label>
          Ciudad
          <select
            value={filtrosFormulario.ciudad}
            onChange={(event) => actualizarFiltro("ciudad", event.target.value)}
          >
            <option value="">Todas</option>
            {opcionesFiltros.ciudades.map((ciudad) => (
              <option key={ciudad} value={ciudad}>
                {ciudad}
              </option>
            ))}
          </select>
        </label>

        <label>
          Categoría
          <select
            value={filtrosFormulario.categoria}
            onChange={(event) =>
              actualizarFiltro("categoria", event.target.value)
            }
          >
            <option value="">Todas</option>
            {opcionesFiltros.categorias.map((categoria) => (
              <option key={categoria} value={categoria}>
                {categoria}
              </option>
            ))}
          </select>
        </label>

        <label>
          Método
          <select
            value={filtrosFormulario.metodoPago}
            onChange={(event) =>
              actualizarFiltro("metodoPago", event.target.value)
            }
          >
            <option value="">Todos</option>
            {opcionesFiltros.metodosPago.map((metodoPago) => (
              <option key={metodoPago} value={metodoPago}>
                {metodoPago}
              </option>
            ))}
          </select>
        </label>

        <label>
          Desde
          <input
            type="date"
            min={opcionesFiltros.fechaMinima}
            max={opcionesFiltros.fechaMaxima}
            value={filtrosFormulario.fechaDesde}
            onChange={(event) =>
              actualizarFiltro("fechaDesde", event.target.value)
            }
          />
        </label>

        <label>
          Hasta
          <input
            type="date"
            min={opcionesFiltros.fechaMinima}
            max={opcionesFiltros.fechaMaxima}
            value={filtrosFormulario.fechaHasta}
            onChange={(event) =>
              actualizarFiltro("fechaHasta", event.target.value)
            }
          />
        </label>

        <div className="filter-actions">
          <button type="button" onClick={aplicarFiltros}>
            Aplicar
          </button>

          <button
            type="button"
            className="secondary-button"
            onClick={limpiarFiltros}
          >
            Limpiar
          </button>
        </div>
      </div>
    </section>
  );
}

export default FilterPanel;