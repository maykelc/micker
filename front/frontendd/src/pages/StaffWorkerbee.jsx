import React, { useState, useEffect } from "react";
import { getUsers } from "../api/userEndPoint";
import RegistrationForm from '../components/formRegister';

const StaffWorkerbee = () => {
  const [users, setUsers] = useState([]); // Estado para los usuarios
  const [loading, setLoading] = useState(true); // Estado para la carga

  // Función para obtener usuarios
  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const response = await getUsers();
        console.log("Usuarios obtenidos:", response);
        setUsers(response.data || []); // Extrae los usuarios de la clave `data`
      } catch (error) {
        console.error("Error al obtener los usuarios:", error);
        setUsers([]); // Maneja el caso de error con un array vacío
      } finally {
        setLoading(false);
      }
    };

    fetchUsers();
  }, []);

  if (loading) {
    return <p>Cargando usuarios...</p>;
  }

  return (
    <div>
        <div>
            <RegistrationForm /> {/* Componente del formulario */}
        </div>
      <h1>Gestión de Personal</h1>
      <div>
        <h2>Lista de Usuarios</h2>
        {users.length > 0 ? (
          users.map((user) => (
            <div key={user.id}>
              <h3>{user.nombre} {user.apellidos}</h3>
              <p>Correo: {user.correo}</p>
            </div>
          ))
        ) : (
          <p>No hay usuarios disponibles.</p>
        )}
      </div>
    </div>
  );
};

export default StaffWorkerbee;
