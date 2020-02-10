# Generated by Django 3.0 on 2020-02-10 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Customer_Id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Customer_First_Name', models.CharField(default='Harry', max_length=100)),
                ('Customer_Last_Name', models.CharField(default='Harry', max_length=100)),
                ('Customer_Email', models.CharField(default='Harry', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('Match_Id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Match_Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('User_Id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('User_Email', models.CharField(max_length=100)),
                ('User_Password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('Booking_Id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('No_Of_Tickets', models.CharField(max_length=100)),
                ('Type_Of_Seats', models.CharField(default='seat', max_length=100)),
                ('Customer_id', models.CharField(default='1', max_length=100)),
                ('Match', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TicketBooking.Match')),
            ],
        ),
         migrations.RunSQL('insert into ticketbooking_user(User_Email,User_Password) values("admin@gmail.com","admin")')

    ]
