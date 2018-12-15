# Generated by Django 2.1.4 on 2018-12-15 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('windhunt', '0006_delete_windforecast'),
    ]

    operations = [
        migrations.CreateModel(
            name='WindForecast',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('forecast_time', models.DateTimeField()),
                ('runtime', models.DateTimeField()),
                ('wind_max', models.FloatField()),
                ('wind_average', models.FloatField()),
                ('wind_angle', models.FloatField()),
            ],
        ),
    ]
