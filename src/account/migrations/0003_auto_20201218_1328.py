# Generated by Django 3.1.4 on 2020-12-18 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_applicant_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='first_name',
            new_name='field',
        ),
        migrations.AddField(
            model_name='company',
            name='about',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='company',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
