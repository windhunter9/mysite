# Generated by Django 2.1.4 on 2018-12-15 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('windhunt', '0013_auto_20181215_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='WindForecas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('forecast_time', models.DateTimeField(default=0)),
                ('runtime', models.DateTimeField()),
                ('wind_max', models.FloatField()),
                ('wind_average', models.FloatField()),
                ('wind_angle', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='WindForecast',
        ),
        migrations.AlterUniqueTogether(
            name='windforecas',
            unique_together={('forecast_time', 'runtime')},
        ),
    ]
