# Generated by Django 3.1.5 on 2021-02-02 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vilight', '0006_attendant_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendant',
            name='admin_comment',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
