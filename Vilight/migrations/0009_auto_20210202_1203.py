# Generated by Django 3.1.5 on 2021-02-02 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vilight', '0008_auto_20210202_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendant',
            name='admin_comment',
            field=models.CharField(choices=[('Đã xử lý', 'Đã xử lý'), ('Chưa hợp lệ', 'Chưa hợp lệ')], max_length=255, null=True),
        ),
    ]
