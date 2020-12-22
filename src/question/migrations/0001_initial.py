# Generated by Django 3.1.3 on 2020-12-22 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0008_auto_20201222_2108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(blank=True, max_length=100, null=True)),
                ('question_text', models.TextField(blank=True, null=True)),
                ('answer', models.TextField(blank=True, null=True)),
                ('stars', models.IntegerField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.company')),
            ],
        ),
    ]
