# Generated by Django 3.2.1 on 2021-05-15 08:50

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('journal', '0004_alter_journal_key_moments'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.contrib.auth.models.User, to='auth.user'),
            preserve_default=False,
        ),
    ]