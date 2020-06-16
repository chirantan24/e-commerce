# Generated by Django 3.0.3 on 2020-06-14 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailverified',
            name='unique_string',
        ),
        migrations.AddField(
            model_name='emailverified',
            name='unique_number',
            field=models.PositiveIntegerField(default=605088, editable=False, unique=True),
        ),
    ]
