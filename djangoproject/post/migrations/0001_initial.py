# Generated by Django 2.2.7 on 2019-11-18 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('price', models.FloatField(max_length=25)),
                ('stock', models.IntegerField(max_length=10)),
                ('image_url', models.CharField(max_length=1000)),
            ],
        ),
    ]
