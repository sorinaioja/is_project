from django import forms

from account.models import Company
from .models import Question


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = [
            'field',
            'question_text',
            'answer',
            ]
