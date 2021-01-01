from django.contrib import admin

# Register your models here.

from forum.models import Forum, Discussion

admin.site.register(Forum)
admin.site.register(Discussion)