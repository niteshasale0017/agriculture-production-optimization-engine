# Generated by Django 3.2.25 on 2024-05-03 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]