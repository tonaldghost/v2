# Generated by Django 3.0.6 on 2020-05-20 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20200520_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='account_email',
            field=models.CharField(max_length=254, unique=True),
        ),
    ]
