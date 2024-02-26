# Generated by Django 5.0.2 on 2024-02-20 16:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_msg'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='fff',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='participant', to=settings.AUTH_USER_MODEL),
        ),
    ]
