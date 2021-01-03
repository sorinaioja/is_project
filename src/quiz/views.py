from django.shortcuts import render

from account.models import Company

from .forms import QuizForm, QuestionForm, AnswerQuestionForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Quiz, Question, UserAnswer


# Create your views here.

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


def take_quiz_view(request, pk):
    c_questions = Question.objects.filter(quiz_id=pk).order_by('?')[0:10]
    cpp_questions = Question.objects.filter(quiz_id=pk).order_by('?')[0:10]
    questions_obj = c_questions | cpp_questions
    id_list = []
    if request.session.get('questions'):
        id_list = request.session['questions']
    else:
        for question_obj in questions_obj:
            id_list.append(question_obj.id)
    questions = Question.objects.filter(quiz_id=pk)
    form = AnswerQuestionForm(request.POST or None, questions=questions)
    flag = False
    score = 0
    if request.method == 'POST':
        if form.is_valid():
            questions_list = []
            answers_list = []
            for (quiz_question, answer) in form.answers():
                questions_list.append(quiz_question)
                answers_list.append(answer)
                corectAnswer = Question.objects.filter(pk=quiz_question).values('correct_answer')
                totalQuestions = Quiz.objects.filter(pk=pk).values('questions_count')
                quiz=Quiz.objects.get(id=pk)
                print(totalQuestions)
                if corectAnswer[0]['correct_answer'] == answer:
                    score = score + 1
            total=totalQuestions[0]['questions_count']
            user_answers = UserAnswer(user=request.user.applicant, score=score,quiz=quiz)
            user_answers.save()
            flag = True
    if flag:
        print(total)
        # request.session.clear()
        return redirect('finish', score,total)
    content = zip(questions, form)
    request.session['questions'] = id_list
    context = {'content': content}
    return render(request, 'quiz.html', context)


# Finish page. Redirects to login page.
def finish_view(request, score, total):
    context = {'score': score,'total':total}
    return render(request, 'finish.html', context)
