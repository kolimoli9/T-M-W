# Generated by Django 4.0.5 on 2022-06-25 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0007_alter_users_pwd'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='email',
            field=models.CharField(default='kolimoli9@gmail.com', max_length=20),
            preserve_default=False,
        ),
    ]
