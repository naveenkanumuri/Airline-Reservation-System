# Generated by Django 4.1.1 on 2022-10-19 17:23

import bookings.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.CharField(default=bookings.models.Booking.generate_pk, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('user_id', models.DecimalField(decimal_places=0, max_digits=2)),
                ('flight_id', models.CharField(max_length=30)),
                ('flight_name', models.CharField(max_length=30)),
                ('source', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
                ('no_of_seats', models.PositiveBigIntegerField()),
                ('price', models.PositiveBigIntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(choices=[('B', 'Booked'), ('C', 'Cancelled')], default='B', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.CharField(default=bookings.models.Flight.generate_pk, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('flight_name', models.CharField(max_length=30)),
                ('source', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
                ('no_of_seats', models.PositiveBigIntegerField()),
                ('remaining_seats', models.PositiveBigIntegerField()),
                ('price', models.PositiveBigIntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
