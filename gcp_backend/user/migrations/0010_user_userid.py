# Generated by Django 4.1.4 on 2022-12-23 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_user_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userid',
            field=models.CharField(default='usr1', max_length=10, unique=True),
            preserve_default=False,
        ),
    ]
