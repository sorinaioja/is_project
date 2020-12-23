from django.shortcuts import render, redirect

# Create your views here.
from question.forms import QuestionForm
from question.models import Question


def questions_view(request):
    context = {
        'questions': Question.objects.all(),
    }
    return render(request, 'question/questions.html', context)


def question_create_view(request):
    if request.POST:

        q_form = QuestionForm(request.POST)

        if q_form.is_valid():

            field = request.POST.get('field')
            answer = request.POST.get('answer')
            q_text = request.POST.get('question')
            company = request.user.company
            q_form.save(commit=False)
            q_form = Question.objects.create(field=field, answer=answer, question_text=q_text, company=company, stars=None)
            q_form.save()
            return redirect("home")
    else:
        q_form = QuestionForm()
    context = {
        'q_form': q_form
    }
    return render(request, "question/question_create.html", context)
