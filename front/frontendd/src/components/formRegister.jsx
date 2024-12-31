import React, { useState } from 'react';
import { Box, TextField, Button, Typography, Grid } from '@mui/material';

const RegistrationForm = () => {
  const [formData, setFormData] = useState({
    nombre: '',
    apellido: '',
    rut: '',
    añoNacimiento: '',
    correo: '',
    contraseña: ''
  });

  // Manejador de cambios para actualizar el estado de los campos
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  // Manejador del envío del formulario
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Formulario enviado:', formData);
    // Aquí puedes agregar la lógica para enviar los datos a tu backend o API
  };

  return (
    <Box sx={{ padding: 3, maxWidth: 600, margin: 'auto' }}>
      <Typography variant="h5" gutterBottom>Formulario de Registro</Typography>
      
      <form onSubmit={handleSubmit}>
        <Grid container spacing={2}>
          {/* Nombre */}
          <Grid item xs={12} sm={6}>
            <TextField
              label="Nombre"
              variant="outlined"
              fullWidth
              name="nombre"
              value={formData.nombre}
              onChange={handleChange}
              required
            />
          </Grid>

          {/* Apellido */}
          <Grid item xs={12} sm={6}>
            <TextField
              label="Apellido"
              variant="outlined"
              fullWidth
              name="apellido"
              value={formData.apellido}
              onChange={handleChange}
              required
            />
          </Grid>

          {/* RUT */}
          <Grid item xs={12}>
            <TextField
              label="RUT"
              variant="outlined"
              fullWidth
              name="rut"
              value={formData.rut}
              onChange={handleChange}
              required
            />
          </Grid>

          {/* Año de Nacimiento */}
          <Grid item xs={12}>
            <TextField
              label="Año de Nacimiento"
              variant="outlined"
              fullWidth
              name="añoNacimiento"
              value={formData.añoNacimiento}
              onChange={handleChange}
              required
              type="number"
              inputProps={{ min: 1900, max: new Date().getFullYear() }}
            />
          </Grid>

          {/* Correo */}
          <Grid item xs={12}>
            <TextField
              label="Correo Electrónico"
              variant="outlined"
              fullWidth
              name="correo"
              value={formData.correo}
              onChange={handleChange}
              required
              type="email"
            />
          </Grid>

          {/* Contraseña */}
          <Grid item xs={12}>
            <TextField
              label="Contraseña"
              variant="outlined"
              fullWidth
              name="contraseña"
              value={formData.contraseña}
              onChange={handleChange}
              required
              type="password"
            />
          </Grid>

          {/* Botón de Enviar */}
          <Grid item xs={12}>
            <Button variant="contained" color="primary" fullWidth type="submit">
              Registrarse
            </Button>
          </Grid>
        </Grid>
      </form>
    </Box>
  );
};

export default RegistrationForm;
