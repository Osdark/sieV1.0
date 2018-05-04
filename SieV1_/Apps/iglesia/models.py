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
    iglesia = models.ForeignKey(Iglesia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Grupo pequeño"
        verbose_name_plural = "Grupos pequeños"
