# Generated by Django 4.0.3 on 2022-03-27 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0003_alter_friend_status_id_alter_group_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, to='scheduler.profile'),
        ),
    ]