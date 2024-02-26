# Generated by Django 5.0.2 on 2024-02-18 15:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_lnmae_member_lname'),
    ]

    operations = [
        migrations.CreateModel(
            name='fff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.member')),
            ],
        ),
    ]