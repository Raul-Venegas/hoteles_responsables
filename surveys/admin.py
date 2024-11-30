from django.contrib import admin
from .models import Survey, Question, Answer, Resultado
# Register your models here.

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Resultado)