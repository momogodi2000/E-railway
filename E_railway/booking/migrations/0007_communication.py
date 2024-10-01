# Generated by Django 5.1.1 on 2024-10-01 11:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='communications/')),
                ('destination', models.CharField(choices=[('employer', 'Employer'), ('maintenance', 'Maintenance'), ('passenger', 'Passenger')], max_length=30)),
            ],
        ),
    ]
