from django import forms

from account.models import Company
from .models import Job


class JobForm(forms.ModelForm):

    title = forms.CharField(max_length=100, help_text='Title')
    location = forms.CharField(max_length=100, help_text='location')
    work_time = forms.CharField(max_length=100, help_text='work_time')
    job_description = forms.CharField(max_length=100, help_text='job_description')
    qualifications = forms.CharField(max_length=100, help_text='qualifications')
    benefits = forms.CharField(max_length=100, help_text='benefits')

    class Meta:
        model = Job
        fields = [
            'title',
            'location',
            'work_time',
            'job_description',
            'qualifications',
            'benefits',
        ]

