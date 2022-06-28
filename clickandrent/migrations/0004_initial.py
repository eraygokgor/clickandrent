# Generated by Django 4.0 on 2022-05-18 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clickandrent', '0003_delete_websiteusers'),
    ]

    operations = [
        migrations.CreateModel(
            name='ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('fee', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=25)),
                ('est_rooms', models.CharField(max_length=10)),
                ('est_area', models.CharField(max_length=10)),
                ('est_age', models.CharField(max_length=10)),
            ],
        ),
    ]