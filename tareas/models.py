from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Personal(BaseModel):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    correo = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(regex=r'^\S+@\S+\.\S+$', message="Correo inválido")
        ],
        db_index=True
    )
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=150)
    genero = models.CharField(max_length=50)
    password = models.CharField(max_length=128, validators=[MinLengthValidator(8)])
    habilidades = models.ManyToManyField("Skill", related_name="usuarios")

    def __str__(self):
        return self.nombre

class Chamba(BaseModel):
    tipo_persona = models.CharField(max_length=50)
    userr = models.ForeignKey(Personal, on_delete=models.CASCADE, related_name="chambausers")

    def __str__(self):
        return self.tipo_persona

class Document(BaseModel):
    user = models.ForeignKey(Personal, on_delete=models.CASCADE)
    ftoCarnetFront = models.ImageField(upload_to='documents/carnet/', null=True, blank=True)
    ftoCarnetBack = models.ImageField(upload_to='documents/carnet/', null=True, blank=True)
    certAntecedentes = models.FileField(upload_to='documents/antecedentes/', null=True, blank=True)
    ftoPersonal = models.ImageField(upload_to='documents/personal/', null=True, blank=True)

    def __str__(self):
        return f"Documentos de {self.user.nombre}"

class Category(BaseModel):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Skill(BaseModel):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="habilidades")

    def __str__(self):
        return self.nombre

class Task(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    created_by = models.ForeignKey(Personal, related_name='tasks_solicited', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Personal, related_name='tasks_assigned', null=True, blank=True, on_delete=models.SET_NULL)
    done = models.BooleanField(default=False)
    applied = models.BooleanField(default=False)
    habilidades_requeridas = models.ManyToManyField(Skill, related_name="tareas_requeridas")

    def __str__(self):
        return self.title

class Califications(BaseModel):
    puntuacion = models.IntegerField()
    personal = models.ForeignKey(Personal, related_name="calificaciones", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.personal.nombre}: {self.puntuacion}"


