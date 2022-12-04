# Generated by Django 4.1.2 on 2022-12-02 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('print_hello', '0004_product2bidding'),
    ]

    operations = [
        migrations.CreateModel(
            name='product3Bidding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.BigIntegerField()),
                ('bprice', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='product4Bidding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.BigIntegerField()),
                ('bprice', models.IntegerField()),
            ],
        ),
    ]
