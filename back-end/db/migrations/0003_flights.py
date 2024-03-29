# Generated by Django 4.0.4 on 2022-05-19 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_userroles_users_customers_admins_airlines_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_time', models.DateTimeField(verbose_name='Departure Time')),
                ('arrival_time', models.DateTimeField(verbose_name='Arrival Time')),
                ('tickets_left', models.IntegerField(default=50)),
                ('airlineID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.airlines')),
                ('destenation_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destenation', to='db.countries')),
                ('origin_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country', to='db.countries')),
            ],
        ),
    ]
