from django.shortcuts import render
from django.views import View
from .models import Question, Answer, Solutions, Applied_solutions
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from django.http import JsonResponse
# Create your views here.

def home_surveys(request):
    return render(request,'surveys/home_surveys.html')

def natural(request):
    return render(request,'surveys/natural.html')

class Natural_survey(LoginRequiredMixin, View):
    def get(self, request):
        
        if not request.user.profile.points_natural:

            questions = Question.objects.filter(survey_id=1)
            context = {'questions': [], 'last_question_index': len(questions) - 1}
            for question in questions:
                answers = Answer.objects.filter(question_id=question.pk)
                context['questions'].append({
                    'question': question,
                    'answers': answers
                })

            return render(request,'surveys/natural_survey.html', context)
        
        else:
            points = request.user.profile.points_natural
            return render(request, 'surveys/score_obtained.html', context={'survey': 'Natural', 'points': points})



def socio_cultural(request):
    return render(request,'surveys/socio-cultural.html')


class Socio_cultural_survey(LoginRequiredMixin, View):
    def get(self, request):
        
        if not request.user.profile.points_socio:

            questions = Question.objects.filter(survey_id=2)
            context = {'questions': [], 'last_question_index': len(questions) - 1}
            for question in questions:
                answers = Answer.objects.filter(question_id=question.pk)
                context['questions'].append({
                    'question': question,
                    'answers': answers
                })

            return render(request,'surveys/socio_cultural_survey.html', context)
        
        else:
            points = request.user.profile.points_socio
            return render(request, 'surveys/score_obtained.html', context={'survey': 'Socio - cultural', 'points': points})


def economico(request):
    return render(request,'surveys/economico.html')

class Economico_survey(LoginRequiredMixin, View):
    def get(self, request):
        
        if not request.user.profile.points_eco:

            questions = Question.objects.filter(survey_id=3)
            context = {'questions': [], 'last_question_index': len(questions) - 1}
            for question in questions:
                answers = Answer.objects.filter(question_id=question.pk)
                context['questions'].append({
                    'question': question,
                    'answers': answers
                })

            return render(request,'surveys/economico_survey.html', context)
        
        else:
            points = request.user.profile.points_eco
            return render(request, 'surveys/score_obtained.html', context={'survey': 'Económico', 'points': points})


class Score_obtained(LoginRequiredMixin, View):
    def post(self, request):
        survey = request.POST.get('survey')
        points = float(request.POST.get('points'))

        if survey == "Natural":
            if not request.user.profile.points_natural:
                request.user.profile.points_natural = points
                request.user.profile.save()
            
            solutions_natural = Solutions.objects.filter(survey_id=1)

            for solution in solutions_natural:
                if points >= solution.score_min and points <= solution.score_max:
                    Applied_solutions.objects.create(
                        user = request.user,
                        solution=solution,
                        applied=False,
                        evidence=None
                    )

        elif survey == "Economico":
            if not request.user.profile.points_eco:
                request.user.profile.points_eco = points
                request.user.profile.save()
            
            solutions_eco = Solutions.objects.filter(survey_id=3)

            for solution in solutions_eco:
                if points >= solution.score_min and points <= solution.score_max:
                    Applied_solutions.objects.create(
                        user = request.user,
                        solution=solution,
                        applied=False,
                        evidence=None
                    )
        else:
            if not request.user.profile.points_socio:
                request.user.profile.points_socio = points
                request.user.profile.save()

                solutions_socio = Solutions.objects.filter(survey_id=2)

            for solution in solutions_socio:
                if points >= solution.score_min and points <= solution.score_max:
                    Applied_solutions.objects.create(
                        user = request.user,
                        solution=solution,
                        applied=False,
                        evidence=None
                    )

        # Renderizar el template con los datos
        return render(request, 'surveys/score_obtained.html', context={'survey': survey, 'points': points})

class Solutions_view(LoginRequiredMixin, View):
    def get(self, request):

        solutions_natural = Applied_solutions.objects.filter(
            user=request.user,
            solution__survey_id=1
        )

        solutions_socio = Applied_solutions.objects.filter(
            user=request.user,
            solution__survey_id=2
        )

        solutions_eco = Applied_solutions.objects.filter(
            user=request.user,
            solution__survey_id=3
        )

        print(len(solutions_natural))
        context = {'Natural': solutions_natural, 'Eco': solutions_socio, 'Socio': solutions_eco}
        
        return render(request,'surveys/solutions.html', context=context)