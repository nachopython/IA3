# adopcion/models.py

from django.db import models

class Animal(models.Model):
    """
    Modelo que representa un animal disponible para adopción.
    Los campos coinciden con el esquema de datos del dataset CSV.
    """
    # 1. Información Básica
    nombre = models.CharField(max_length=100, help_text="Nombre del animal.")
    especie = models.CharField(max_length=50, help_text="Perro o Gato.")
    raza = models.CharField(max_length=150, help_text="Raza del animal (puede ser compuesta/mestizo).")
    sexo = models.CharField(max_length=10, help_text="Macho o Hembra.")
    edad_años = models.IntegerField(help_text="Edad del animal en años.")
    peso = models.DecimalField(max_digits=4, decimal_places=1, help_text="Peso en kg.")
    tamaño = models.CharField(max_length=50, help_text="Pequeño, Mediano, Grande, Gigante.")
    color_pelaje = models.CharField(max_length=150, help_text="Descripción del color y tipo de pelo.")
    
    # 2. Requisitos y Condición Especial
    apto_con = models.TextField(help_text="Lista de requisitos obligatorios del hogar (separados por coma).")
    condicion_especial = models.CharField(max_length=255, help_text="Nombre de la condición médica o conductual, si aplica.")
    
    # 3. Estado de Salud (Booleano)
    # Utilizamos BooleanField para campos 'Si'/'No'
    desparasitado = models.BooleanField(default=False, help_text="¿Está desparasitado?")
    esterilizado = models.BooleanField(default=False, help_text="¿Está esterilizado?")
    con_microchip = models.BooleanField(default=False, help_text="¿Tiene microchip?")
    vacunado = models.BooleanField(default=False, help_text="¿Está vacunado?")
    
    # 4. Estado de Adopción
    adoptado = models.BooleanField(default=False, help_text="True si ya fue adoptado.")
    
    # 5. Descripciones (Texto largo)
    caracter_necesidad = models.TextField(help_text="Palabras clave de carácter y necesidades (separadas por coma).")
    historia_breve = models.TextField(help_text="Historia de rescate o procedencia.")
    
    # La biografía generada (tu tarea de IA)
    biografia_final = models.TextField(help_text="Biografía emocional generada (Manual o por IA).")

    # 6. Campo para la imagen
    # Usaremos un campo para simular que cada animal tiene una foto.
    foto = models.ImageField(upload_to='animal_pics/', blank=True, null=True, help_text="Foto principal del animal.")

    def __str__(self):
        """Devuelve el nombre del animal para una fácil identificación."""
        return self.nombre

    class Meta:
        verbose_name_plural = "Animales"
        ordering = ['nombre']

# NOTA: Este modelo NO es el que usaré para la Generación de Bio (IA 3). 
# La lógica de IA 3 se usará en el proceso de Carga de Datos o en la Edición.