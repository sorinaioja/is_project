from django.shortcuts import render

# Create your views here.
from question.models import Question

def questions_view(request):
    context = {
        'questions': Question.objects.all(),
    }
    return render(request, 'question/questions.html', context)