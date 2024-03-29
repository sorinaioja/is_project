# Generated by Django 3.1.4 on 2021-01-03 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_useranswer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useranswer',
            name='answers',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='questions',
        ),
        migrations.AddField(
            model_name='quiz',
            name='questions_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='useranswer',
            name='response_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='useranswer',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
