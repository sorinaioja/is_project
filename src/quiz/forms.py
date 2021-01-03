from django import forms

from account.models import Company
from .models import Quiz, Question,UserAnswer
from crispy_forms.helper import FormHelper
from django.forms import widgets


class QuizForm(forms.ModelForm):

    class Meta:
        model = Quiz
        fields = [
            'name',
            'questions_count',
           # 'question_count',
            'description',

        ]

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = [
            'question',
            'answer_one',
            'answer_two',
            'answer_three',
            'answer_four',
            'correct_answer',



        ]

class AnswerQuestionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')  # pop questions array from kwargs
        super().__init__(*args, **kwargs)
        if questions:
            for question in questions:  # add a form field for each question
                CHOICES = (
                    ('A', question.answer_one),
                    ('B', question.answer_two),
                    ('C', question.answer_three),
                    ('D', question.answer_four),
                )
                self.fields[str(question.id)] = forms.ChoiceField(required=False, choices=CHOICES,
                                                                           widget=widgets.RadioSelect)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


    def answers(self):  # return questions and answers for result processing
        for name, question in self.cleaned_data.items():
            yield (name, question)