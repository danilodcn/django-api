from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Student(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    rg = models.CharField(max_length=9, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False)
    birth_date = models.DateField(blank=False, null=False)
    create_at = models.DateTimeField(editable=False, default=timezone.now)

    class Meta:
        verbose_name = "Estudante"
        verbose_name_plural = "Estudantes"

    def __str__(self) -> str:
        return "{}".format(self.name)


class Course(models.Model):
    BASIC = "B"
    INTERMEDIARY = "I"
    ADVANCED = "A"

    LEVEL_CHOICES = (
        (BASIC, _("Basic")),
        (INTERMEDIARY, _("Intermediary")),
        (ADVANCED, _("Advanced")),
    )

    code = models.CharField(max_length=10, blank=False, null=False)
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=250, null=True, blank=True)
    level = models.CharField(
        choices=LEVEL_CHOICES, max_length=1, blank=False, null=False
    )

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self) -> str:
        return "{} - {}".format(self.code, self.title)
