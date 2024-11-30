from django.db import models

# Create your models here.

class Survey(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "cuestionario"
        verbose_name_plural = "cuestionarios"

    def __str__(self):
        return self.name
    
class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='preguntas')
    question = models.TextField()
    value = models.IntegerField(default=0)
    OPEN = 'open'
    MULTIPLE_CHOICE = 'multiple_choice'
    QUESTION_TYPES = [
        (OPEN, 'Pregunta abierta'),
        (MULTIPLE_CHOICE, 'Opción múltiple'),
    ]
    type = models.CharField(
        max_length=20,
        choices=QUESTION_TYPES,
        default=MULTIPLE_CHOICE,
    )

    class Meta:
        verbose_name = "pregunta"
        verbose_name_plural = "preguntas"

    def __str__(self):
        return self.question

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='respuestas')
    text = models.CharField(max_length=255)
    value = models.IntegerField(default=0)

    class Meta:
        verbose_name = "respuesta"
        verbose_name_plural = "respuestas"

    def __str__(self):
        return self.text
    
from django.contrib.auth.models import User

class Resultado(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resultados')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='resultados')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    answered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.question.text}'

