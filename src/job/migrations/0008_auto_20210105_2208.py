# Generated by Django 3.1.3 on 2021-01-05 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20210105_2208'),
        ('job', '0007_auto_20210104_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='account.company'),
        ),
    ]
