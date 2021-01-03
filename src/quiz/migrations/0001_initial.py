# Generated by Django 3.1.4 on 2021-01-03 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0009_merge_20201223_0304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.company')),
            ],
            options={
                'ordering': ('-category',),
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('answer_one', models.CharField(max_length=200)),
                ('answer_two', models.CharField(max_length=200)),
                ('answer_three', models.CharField(max_length=200)),
                ('answer_four', models.CharField(max_length=200)),
                ('correct_answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=2)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz')),
            ],
        ),
    ]
