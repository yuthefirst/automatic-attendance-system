# Generated by Django 3.1.5 on 2021-01-31 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vilight', '0004_delete_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Axxxx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=255, null=True)),
                ('staff_id', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('position', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]