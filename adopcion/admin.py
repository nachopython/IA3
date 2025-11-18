# adopcion/admin.py

from django.contrib import admin
from .models import Animal

# Registra tu modelo 'Animal' para que sea visible y gestionable en /admin
admin.site.register(Animal)