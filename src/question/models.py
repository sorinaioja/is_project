from django.db import models

from account.models import Company


class Question(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    field = models.CharField(max_length=100, blank=True, null=True)
    question_text = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    stars = models.IntegerField(blank=True, null=True) #ceva sa se vada cat de frecventa e, eventual in functie de asta sa fie ordonate, si sa existe un buton d eunde userul sa i poata da + sau -
