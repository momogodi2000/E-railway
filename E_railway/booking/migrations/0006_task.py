# Generated by Django 5.1.1 on 2024-10-01 10:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_maintenancetask'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('task_type', models.CharField(choices=[('periodic', 'Periodic'), ('monthly', 'Monthly')], max_length=20)),
                ('ticket_quota', models.IntegerField()),
                ('is_on_guard', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('done', 'Done'), ('not_done', 'Not Done')], default='not_done', max_length=20)),
                ('sanction', models.CharField(choices=[('none', 'None'), ('warning', 'Warning'), ('temporary_ban', 'Temporary Ban')], default='none', max_length=20)),
                ('assigned_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assigned_to', models.ForeignKey(limit_choices_to={'role': 'employer'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
