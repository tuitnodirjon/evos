# Generated by Django 4.1 on 2022-08-19 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12, null=True)),
                ('full_name', models.CharField(max_length=355, null=True)),
                ('token', models.CharField(max_length=455, null=True)),
            ],
        ),
    ]
