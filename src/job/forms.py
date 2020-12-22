from django import forms

from account.models import Company
from .models import Job


class JobForm(forms.ModelForm):

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

