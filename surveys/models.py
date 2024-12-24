from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def custom_upload_to(instance, filename):
    old_instance = Applied_solutions.objects.get(pk=instance.pk)
    old_instance.evidence.delete()
    return 'solutions/' + filename

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
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = "respuesta"
        verbose_name_plural = "respuestas"

    def __str__(self):
        return self.text
    

class Resultado(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resultados')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='resultados')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    answered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.question.text}'

class Solutions(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='solutions')
    title_solution = models.TextField(max_length=100, null=True, blank=True, default="Título predeterminado")
    text = models.TextField()
    score_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    score_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = "solución"
        verbose_name_plural = "soluciones"

    def __str__(self):
        return self.text

class Applied_solutions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_solutionsApplied')
    solution = models.ForeignKey(Solutions, on_delete=models.CASCADE, related_name='solutions_applied')
    applied = models.BooleanField(default=False)
    evidence = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)


    class Meta:
        verbose_name = "solución aplicada"
        verbose_name_plural = "soluciones aplicadas"