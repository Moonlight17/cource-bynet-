# Generated by Django 4.1 on 2022-09-02 13:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='ListEmails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregated.participants')),
            ],
        ),
        migrations.CreateModel(
            name='Aggregate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_on_less', models.IntegerField(verbose_name='Time On Lesson')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregated.participants')),
            ],
        ),
    ]
