# Generated by Django 3.1.5 on 2021-01-30 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Attendant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=255, null=True)),
                ('staff_id', models.CharField(max_length=255, null=True)),
                ('position', models.CharField(max_length=255, null=True)),
                ('checkin', models.CharField(max_length=255, null=True)),
                ('checkmid', models.CharField(max_length=255, null=True)),
                ('checkout', models.CharField(max_length=255, null=True)),
                ('comment', models.CharField(max_length=255, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Vilight.staff')),
            ],
        ),
    ]
