# Generated by Django 4.2.16 on 2024-12-30 10:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vidoe_text', '0011_alter_subclip_options_subclip_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textfile',
            name='fps',
        ),
        migrations.AddField(
            model_name='textfile',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
