# Generated by Django 4.0.5 on 2022-07-29 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='username',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
