# Generated by Django 3.0.1 on 2020-05-03 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_company_no_of_backlogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='about',
            field=models.TextField(help_text='*optional', max_length=1000),
        ),
    ]
