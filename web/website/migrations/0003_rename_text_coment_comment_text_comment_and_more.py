# Generated by Django 5.0 on 2023-12-26 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text_coment',
            new_name='text_comment',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='yourname',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
