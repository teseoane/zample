from django.db import models

from core.references import StudentState


class Student(models.Model):
    """Student Model."""
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True)
    matches = models.ManyToManyField('core.Student', blank=True)
    state = models.CharField(
        max_length=10,
        choices=StudentState.STUDENT_STATE_CHOICES,
        blank=False,
        null=False,
        default=StudentState.ACTIVE
    )

    def __str__(self):
        return f'{self.name} - {self.code}'
