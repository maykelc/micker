import axios from 'axios';

axios.defaults.baseURL = 'http://localhost:8000/api/v1/';

export const apiRequest = async (method, endpoint, data = null) => {
    try {
        const response = await axios({ method, url: endpoint, data });
        return response.data;
    } catch (error) {
        console.error(`Error en ${method.toUpperCase()} ${endpoint}:`, error);
        throw error;
    }
};

