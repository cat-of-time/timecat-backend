# Generated by Django 2.0.1 on 2018-02-07 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20180202_1503'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plan',
            options={'ordering': ('created_datetime',)},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('created_datetime',)},
        ),
        migrations.RenameField(
            model_name='plan',
            old_name='created',
            new_name='created_datetime',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='created',
            new_name='created_datetime',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='begin',
            new_name='begin_datetime',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='created',
            new_name='created_datetime',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='end',
            new_name='end_datetime',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='finished',
            new_name='finished_datetime',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='is_finish',
            new_name='is_finished',
        ),
    ]
