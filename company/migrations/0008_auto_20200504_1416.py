# Generated by Django 3.0.1 on 2020-05-04 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_auto_20200504_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='last_date_to_apply',
            field=models.DateField(blank=True, null=True),
        ),
    ]
