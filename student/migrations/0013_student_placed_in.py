# Generated by Django 3.0.1 on 2020-05-03 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_auto_20200503_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='placed_in',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
