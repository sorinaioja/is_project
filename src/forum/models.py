
from django.db import models


# Create your models here.
from account.models import Applicant


#parent model
class Forum(models.Model):
    topic = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=50, blank=True)
    link = models.CharField(max_length=30, blank=True)
    date_created = models.TextField(blank=True, null=True)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)

#child model
class Discussion(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)
