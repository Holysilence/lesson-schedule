# Generated by Django 4.1 on 2022-09-02 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='time',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]