from django import forms

from account.models import Applicant

from .models import Forum, Discussion


class ForumForm(forms.ModelForm):

    class Meta:
        model = Forum
        fields = [
            'topic',
            'description',
            'link',
        ]

class DiscussionForm(forms.ModelForm):

    class Meta:
        model = Discussion
        fields = [
            'discuss',
        ]




