from django.db import models


# Create your models here.
from account.models import Company


class Job(models.Model):
    title = models.CharField(max_length=40, blank=True)
    location = models.CharField(max_length=30, blank=True)
    work_time = models.CharField(max_length=30, blank=True)
    job_description = models.CharField(max_length=500, blank=True)
    qualifications = models.CharField(max_length=1000, blank=True)
    benefits = models.CharField(max_length=500, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)



