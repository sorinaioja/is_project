from django import forms

from account.models import Company
from .models import Job, JobApplication


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


class JobFormApplication(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            'name',
            'email',
            'phone_number',
            'applying_position',
            'start_date',
        ]
