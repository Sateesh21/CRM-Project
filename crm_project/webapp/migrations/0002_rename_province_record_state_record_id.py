# Generated by Django 5.0.6 on 2024-06-20 07:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='province',
            new_name='state',
        ),
        migrations.AddField(
            model_name='record',
            name='Id',
            field=models.CharField(default=django.utils.timezone.now, max_length=10, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
