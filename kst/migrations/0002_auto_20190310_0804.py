# Generated by Django 2.1.4 on 2019-03-10 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kst', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionresponse',
            name='integer_type_submission',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]