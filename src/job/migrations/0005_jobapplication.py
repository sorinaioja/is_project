# Generated by Django 3.1.3 on 2021-01-03 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_auto_20201222_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=10)),
                ('applying_position', models.CharField(blank=True, max_length=50)),
                ('start_date', models.TextField(blank=True, null=True)),
                ('display_CV', models.FileField(upload_to='')),
            ],
        ),
    ]
