# Generated by Django 3.1.5 on 2021-01-30 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vilight', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='gender',
            field=models.CharField(choices=[('0', 'NAM'), ('1', 'NỮ')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='position',
            field=models.CharField(max_length=255, null=True),
        ),
    ]