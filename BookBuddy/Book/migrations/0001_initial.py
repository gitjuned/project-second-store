# Generated by Django 2.1.7 on 2019-03-15 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=30)),
                ('useremail', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('userpassword', models.CharField(max_length=50)),
            ],
        ),
    ]