# Generated by Django 4.1.6 on 2023-02-05 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=90)),
                ('subject', models.CharField(max_length=90)),
                ('marks', models.IntegerField()),
            ],
        ),
    ]
