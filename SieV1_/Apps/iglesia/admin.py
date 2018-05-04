from django.contrib import admin

# Register your models here.
from .models import Iglesia, Grupo_Pequeño

admin.site.register(Iglesia)
admin.site.register(Grupo_Pequeño)