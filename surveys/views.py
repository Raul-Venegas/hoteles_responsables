from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Survey, Question, Answer, Resultado
# Create your views here.

def home_surveys(request):
    return render(request,'surveys/home_surveys.html')

def natural(request):
    return render(request,'surveys/natural.html')

#@login_required
class Natural_survey(View):
    def get(self, request):
        questions = Question.objects.filter(survey_id=1)
        context = {'questions': [], 'last_question_index': len(questions) - 1}
        for question in questions:
            answers = Answer.objects.filter(question_id=question.pk)
            context['questions'].append({
                'question': question,
                'answers': answers
            })

        return render(request,'surveys/natural_survey.html', context)
    
    def post(self, request):
        return render(request,'surveys/natural_survey.html')

def socio_cultural(request):
    return render(request,'surveys/socio-cultural.html')


class Socio_cultural_survey(View):
    def get(self, request):
        questions = Question.objects.filter(survey_id=2)
        context = {'questions': [], 'last_question_index': len(questions) - 1}
        for question in questions:
            answers = Answer.objects.filter(question_id=question.pk)
            context['questions'].append({
                'question': question,
                'answers': answers
            })

        return render(request,'surveys/socio_cultural_survey.html', context)
    
    def post(self, request):
        return render(request,'surveys/socio_cultural_survey.html')

def economico(request):
    return render(request,'surveys/economico.html')

@login_required
def economico_survey(request):
    return render(request,'surveys/economico_survey.html')