from django.contrib import admin

# Register your models here.
from question.models import Question

admin.site.register(Question)