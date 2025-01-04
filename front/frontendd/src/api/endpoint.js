import axios from 'axios';

const BASE_URL = 'http://localhost:8000/api/v1/'; // Define una base URL fija

export const apiRequest = async (method, endpoint, data = null) => {
  try {
    const response = await axios({
      method,
      url: `${BASE_URL}${endpoint}`, // Combina la base URL con el endpoint recibido
      data,
      headers: { 'Content-Type': 'application/json' }, // Configura los encabezados
    });
    return response;
  } catch (error) {
    console.error(`Error en ${method.toUpperCase()} ${BASE_URL}${endpoint}:`, error);
    throw error; // Re-lanza el error para manejarlo externamente
  }
};
