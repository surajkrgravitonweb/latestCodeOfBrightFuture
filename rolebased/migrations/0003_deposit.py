# Generated by Django 3.2.8 on 2023-12-15 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rolebased', '0002_accountdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=15)),
                ('Email', models.CharField(max_length=15)),
                ('Amount', models.CharField(max_length=15)),
            ],
        ),
    ]
