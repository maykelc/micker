from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

# Modelo Chamba: Define los tipos de usuario (empleado o empleador)
class Chamba(models.Model):
    TIPO_CHOICES = [
        ('empleado', 'Empleado'),
        ('empleador', 'Empleador'),
    ]
    tipo_persona = models.CharField(max_length=50, choices=TIPO_CHOICES)

    def __str__(self):
        return self.tipo_persona


# Modelo Personal: Información personal del usuario
class Personal(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    correo = models.CharField(
        max_length=50,
        validators=[RegexValidator(regex=r'^\S+@\S+\.\S+$', message="Correo inválido")],
        db_index=True
    )
    telefono = models.IntegerField(null=True, blank=True)
    direccion = models.CharField(max_length=150)
    tipo_choise=[
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'), 
        ('Otro', 'Otro')
                 ]
    genero = models.CharField(max_length=15, choices=tipo_choise)
    password = models.CharField(max_length=128, validators=[MinLengthValidator(8)])
    # Relación con tipo de usuario (empleado o empleador)
    tipo_empleado = models.ForeignKey('Chamba', on_delete=models.CASCADE,null=True, blank=True)
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


# Modelo Document: Para almacenar documentos del usuario
class Document(models.Model):
    user_id = models.ForeignKey(Personal, on_delete=models.CASCADE)
    ftoCarnetFront = models.ImageField(upload_to='documents/carnet/', null=True, blank=True)
    ftoCarnetBack = models.ImageField(upload_to='documents/carnet/', null=True, blank=True)
    certAntecedentes = models.FileField(upload_to='documents/antecedentes/', null=True, blank=True)
    ftoPersonal = models.ImageField(upload_to='documents/personal/', null=True, blank=True)

    def __str__(self):
        return f"Documentos de {self.user_id.nombre}"

class Category(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.nombre



# Modelo Skill: Para almacenar habilidades
class Skill(models.Model):
    nombre = models.CharField(max_length=99)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="Habilidades")
    def __str__(self):
        return self.nombre


class Location(models.Model):
    region = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    def __str__(self):
        return self.direccion


# Modelo Task: Para almacenar tareas creadas por los empleadores
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    costo = models.IntegerField(null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Personal, related_name='tasks_solicited', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Personal, related_name='tasks_assigned', null=True, blank=True, on_delete=models.SET_NULL)
    done = models.BooleanField(default=False)
    applied = models.BooleanField(default=False)
    habilidades_requeridas = models.ManyToManyField(Skill, related_name="tareas_requeridas")

    def __str__(self):
        return self.title
    


class Califications(models.Model):
    puntuacion = models.IntegerField(null=True, blank=True)
    calificador = models.ForeignKey(Personal, related_name="calificador", on_delete=models.CASCADE, null=True, blank=True)
    calificado = models.ForeignKey(Personal, related_name="calificado", on_delete=models.CASCADE, null=True, blank=True)  # Permitir NULL

    def __str__(self):
        return f"Calificación de {self.calificador.nombre} a {self.calificado.nombre}: {self.puntuacion}"



