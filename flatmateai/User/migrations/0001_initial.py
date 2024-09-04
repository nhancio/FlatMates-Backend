# Generated by Django 4.2.8 on 2024-08-27 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('food_choice', models.CharField(blank=True, max_length=100)),
                ('drinking', models.BooleanField(default=False)),
                ('smoking', models.BooleanField(default=False)),
                ('pet', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
