# Generated by Django 5.1.1 on 2024-10-10 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_tickethistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketbought',
            name='reserved_places',
            field=models.JSONField(default=list),
        ),
    ]
