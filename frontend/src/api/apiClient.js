const API_BASE_URL = "http://localhost:8000/api/dashboard";

export async function get(endpoint, errorMessage = "Error al consultar la API") {
  const response = await fetch(`${API_BASE_URL}${endpoint}`);

  if (!response.ok) {
    throw new Error(errorMessage);
  }

  return response.json();
}