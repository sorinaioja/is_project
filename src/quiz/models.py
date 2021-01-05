from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from account.models import Company, Applicant
from django.db import models


class Quiz(models.Model):
    company = models.ForeignKey(Company, related_name="quiz", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    questions_count = models.IntegerField(default=0)
    description = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ('-category',)

    def __str__(self):
        return self.name


ANSWER_CHOICES = [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
]


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    answer_one = models.CharField(max_length=200)
    answer_two = models.CharField(max_length=200)
    answer_three = models.CharField(max_length=200)
    answer_four = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=2, blank=False, null=False, choices=ANSWER_CHOICES)

    def __str__(self):
        return self.question


class UserAnswer(models.Model):
    user = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,default=1)
    score = models.IntegerField(default=0)
    response_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)



    def __str__(self):
        return str(self.user)
