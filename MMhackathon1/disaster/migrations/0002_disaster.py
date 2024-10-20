# Generated by Django 5.1.1 on 2024-10-19 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disaster', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volunteer_name', models.CharField(max_length=100)),
                ('disaster_type', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('date_reported', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
