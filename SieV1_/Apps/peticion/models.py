from django.db import models

# Create your models here.
class Pastor(models.Model):
    nombre = models.CharField(max_length=120, blank=True, null=True)
    correo = models.EmailField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Pastor"
        verbose_name_plural = "Pastores"
