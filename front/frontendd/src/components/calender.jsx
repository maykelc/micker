import React, { useState } from "react";
import { Box, Typography, Modal, Grid } from "@mui/material";

const daysOfWeek = ["LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO", "DOMINGO"];


const Calendar = ({ open, onClose }) => {
  return (
    <Modal open={open} onClose={onClose}>
      <Box sx={{ 
        position: 'absolute', 
        top: '50%', 
        left: '50%', 
        transform: 'translate(-50%, -50%)', 
        bgcolor: '#fff', 
        color: '#333', 
        boxShadow: 20, 
        borderRadius: 5, 
        p: 4, 
        width: 700, 
        outline: 'none',
        overflow: 'auto',
      }}>
        <Typography variant="h6" sx={{ mb: 2, textAlign: 'center' }}>
          Calendario
        </Typography>
        <Grid container spacing={2}>
          {daysOfWeek.map((day, index) => (
            <Grid item xs={2} key={index} sx={{ textAlign: 'center' }}>
              <Typography variant="body1" sx={{ fontWeight: 'bold' }}>{day}</Typography>
            </Grid>
          ))}

        </Grid>
      </Box>
    </Modal>
  );
};

export default Calendar;
