# Generated by Django 4.1.2 on 2022-12-02 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('print_hello', '0003_alter_product1bidding_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='product2Bidding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.BigIntegerField()),
                ('bprice', models.IntegerField()),
            ],
        ),
    ]
