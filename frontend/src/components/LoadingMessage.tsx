function LoadingMessage({ mensaje = "Cargando dashboard..." }) {
  return <main className="page">{mensaje}</main>;
}

export default LoadingMessage;