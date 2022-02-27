# Generated by Django 4.0.2 on 2022-02-27 01:56

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=250)),
                ('gamer_profiles', models.JSONField(default=dict)),
                ('friends', models.ManyToManyField(to='scheduler.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Timezone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateField()),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.schedule')),
            ],
        ),
        migrations.AddField(
            model_name='schedule',
            name='timezones',
            field=models.ManyToManyField(to='scheduler.Timezone'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.profile'),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('users', models.ManyToManyField(to='scheduler.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='friend_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepting_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accepting_user', to='scheduler.profile')),
                ('inviting_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inviting_user', to='scheduler.profile')),
            ],
        ),
    ]
