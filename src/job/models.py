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

class JobApplication(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=10, blank=True)
    applying_position = models.CharField(max_length=50, blank=True)
    start_date = models.TextField(blank=True, null=True)




