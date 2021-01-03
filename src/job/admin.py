from django.contrib import admin

# Register your models here.
from job.models import Job, JobApplication

admin.site.register(Job)
admin.site.register(JobApplication)