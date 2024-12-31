import React, { useState } from 'react'; // Importa useState
import { Box, Typography, Grid, Link, Button } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import Login from "../components/login"; // Asegúrate de que la ruta sea correcta

const HomePage = () => {
    const navigate = useNavigate();
    const [openLoginModal, setOpenLoginModal] = useState(false); // Estado para abrir/cerrar el modal

    // Funciones para manejar la apertura y cierre del modal
    const handleOpenLogin = () => {
        setOpenLoginModal(true); // Abrir el modal
    };
    const handleCloseLogin = () => {
        setOpenLoginModal(false); // Cerrar el modal
    };

    return (
        <div>
            {/* Header */}
            <Box sx={{ padding: 2, backgroundColor: '#f4f4f4', textAlign: 'center' }}>
                <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <Box>
                        <img src="logo.png" alt="Logo" style={{ height: '50px' }} />
                    </Box>

                    <Box>
                        <Button
                            variant="outlined"
                            sx={{ margin: "0 10px" }}
                            onClick={() => navigate("/register")}>
                            Registrarse
                        </Button>
                        <Button
                            variant="outlined"
                            sx={{ margin: '0 10px' }}
                            onClick={handleOpenLogin} // Abrir el modal al hacer clic
                        >
                            Iniciar sesión
                        </Button>
                    </Box>
                </Box>
                <Typography variant="h4" component="h1">Bienvenido a la Página Principal</Typography>
            </Box>

            {/* Main Container */}
            <Box sx={{ padding: 2 }}>
                <Grid container spacing={2}>
                    {[...Array(7)].map((_, index) => (
                        <Grid item xs={12} sm={6} md={4} key={index}>
                            <Box sx={{ border: '1px solid #ccc', padding: 2, textAlign: 'center' }}>
                                <Typography variant="h6">Div {index + 1}</Typography>
                                <Typography variant="body2">Contenido de la sección {index + 1}</Typography>
                            </Box>
                        </Grid>
                    ))}
                </Grid>
            </Box>

            {/* Footer */}
            <Box sx={{ padding: 2, backgroundColor: '#f4f4f4', textAlign: 'center' }}>
                <Typography variant="h6">Sobre nosotros</Typography>
                <Box>
                    <Link href="/quienes-somos" sx={{ margin: '0 10px' }}>Quiénes somos</Link>
                    <Link href="/mision" sx={{ margin: '0 10px' }}>Misión</Link>
                    <Link href="/vision" sx={{ margin: '0 10px' }}>Visión</Link>
                    <Link href="/redes-sociales" sx={{ margin: '0 10px' }}>Redes Sociales</Link>
                </Box>
                <Box>
                    <Typography variant="body1">Categorías</Typography>
                    <ul>
                        <li><Link href="/categoria1">Categoría 1</Link></li>
                        <li><Link href="/categoria2">Categoría 2</Link></li>
                        <li><Link href="/categoria3">Categoría 3</Link></li>
                    </ul>
                </Box>
            </Box>

            {/* Login Modal */}
            <Login open={openLoginModal} onClose={handleCloseLogin} />
        </div>
    );
};

export default HomePage;
