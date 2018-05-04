from django.db import models

# Create your models here.
class Iglesia(models.Model):
    nombre = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Iglesia"
        verbose_name_plural = "Iglesias"


class Grupo_Pequeño(models.Model):
    nombre = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"
