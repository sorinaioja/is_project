from django.db import models


# Create your models here.
from account.models import Company


class Job(models.Model):
    title = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=50, blank=True)
    work_time = models.CharField(max_length=30, blank=True)
    job_description = models.TextField(blank=True, null=True)
    qualifications = models.TextField(blank=True, null=True)
    benefits = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)



