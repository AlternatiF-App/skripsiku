from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from users.models import User

class Student(models.Model):
    fullname = models.CharField(max_length=60, blank=False)
    id_minat = models.IntegerField(blank=False)
    student_class = models.IntegerField(blank=False)
    score_math = models.IntegerField(blank=False)
    score_science = models.IntegerField(blank=False)
    score_indonesian = models.IntegerField(blank=False)
    cluster = models.CharField(blank=True, default="", max_length=10)

    teacher = models.ForeignKey(to=User, on_delete=models.CASCADE)


    class Meta:
        ordering = ['id']