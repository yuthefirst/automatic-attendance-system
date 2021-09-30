# Generated by Django 3.1.5 on 2021-01-30 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vilight', '0002_auto_20210130_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendant',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='position',
            field=models.CharField(choices=[('0', 'Giám đốc'), ('1', 'Quản lý'), ('2', 'Quản lý kho'), ('3', 'Kế toán'), ('4', 'Kỹ thuật'), ('5', 'QA - Quality Assurance'), ('6', 'QC - Quality Control'), ('7', 'Công nhân'), ('8', 'Bảo vệ'), ('9', 'Lao công')], max_length=255, null=True),
        ),
    ]
