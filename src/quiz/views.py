from django.shortcuts import render

from account.models import Company

from .forms import QuizForm, QuestionForm, AnswerQuestionForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Quiz, Question, UserAnswer



def quiz_create_view(request):
    if request.POST:

        q_form = QuizForm(request.POST)

        if q_form.is_valid():
            company = request.user.company
            name = request.POST.get('name')
            category = request.POST.get('category')
            description = request.POST.get('description')

            quiz = q_form.save(commit=False)
            quiz.company = company
            quiz.category = category
            quiz.save()
            print(category)
            return redirect("createQuestion", quiz.id)
    else:
        q_form = QuizForm()
    context = {
        'q_form': q_form
    }
    return render(request, "createQuiz.html", context)


def quiz_question_create_view(request, pk):
    if request.POST:

        q_form = QuestionForm(request.POST)

        if q_form.is_valid():
            question = q_form.save(commit=False)
            question.quiz = Quiz.objects.get(id=pk)
            print(question)
            question.save()
            return redirect("createQuestion", pk)
    else:
        q_form = QuestionForm()
    context = {
        'q_form': q_form
    }
    return render(request, "createQuestion.html", context)


def present_quizzes_view(request):
    context = {
        'quizzes': Quiz.objects.all(),
    }
    return render(request, "viewQuizzez.html", context)

def results_view(request):

    user = request.user.applicant
    pk = user.aid

    context = {
        'results': UserAnswer.objects.filter(user_id=pk),
    }
    return render(request, "viewResults.html", context)

def results_company_view(request):

    user = request.user.company
    pk = user.cip
    quiz = Quiz.objects.filter(company_id=pk)
    print(quiz)
    id_list = []
    result = []
    for id in quiz:
        id_list.append(id.id)
        print(id.id)

    if not id_list:
        id = 0

    context = {
        'results': UserAnswer.objects.filter(quiz_id=id),
    }
    return render(request, "viewResultsCompany.html", context)

def take_quiz_view(request, pk):


    questions = Question.objects.filter(quiz_id=pk)

    id_list = []
    if request.session.get('questions'):
        id_list = request.session['questions']
    else:
        for question in questions:
            id_list.append(question.id)



    form = AnswerQuestionForm(request.POST or None, questions=questions)
    flag = False
    score = 0

    if request.method == 'POST':
        if form.is_valid():


            for (quiz_question, answer) in form.answers():

                corectAnswer = Question.objects.filter(pk=quiz_question).values('correct_answer')
                totalQuestions = Quiz.objects.filter(pk=pk).values('questions_count')

                quiz=Quiz.objects.get(id=pk)

                if corectAnswer[0]['correct_answer'] == answer:
                    score = score + 1

            total=totalQuestions[0]['questions_count']

            user_answers = UserAnswer(user=request.user.applicant, score=score,quiz=quiz)
            user_answers.save()
            flag = True

    if flag:

        return redirect('finish', score,total)

    content = zip(questions, form)
    request.session['questions'] = id_list
    context = {'content': content}
    return render(request, 'quiz.html', context)


# Finish page. Redirects to login page.
def finish_view(request, score, total):
    context = {'score': score,'total':total}
    return render(request, 'finish.html', context)
