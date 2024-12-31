import React from "react";
import { Box, Typography, Button } from "@mui/material";
import RegistrationForm from "../components/formRegister";
import { ButtonBack } from "../components/ButtonBack";

const RegistrationPage = () => {
  return (
    <Box sx={{ padding: 4, textAlign: "center" }}>
      <Typography variant="h4" component="h1" sx={{ marginBottom: 2 }}>
        Registro
      </Typography>
      <RegistrationForm />
      <ButtonBack/>
    </Box>
  );
};

export default RegistrationPage;
