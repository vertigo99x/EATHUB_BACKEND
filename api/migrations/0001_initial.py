# Generated by Django 3.2.4 on 2022-10-29 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlluserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('usercat', models.CharField(choices=[('vendor', 'vendor'), ('client', 'client'), ('dispatch', 'dispatch')], max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('firstname', models.CharField(max_length=255)),
                ('middlename', models.CharField(blank=True, max_length=255, null=True)),
                ('lastname', models.CharField(max_length=255)),
                ('phonenumber', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['username'],
            },
        ),
        migrations.CreateModel(
            name='FoodItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(max_length=255)),
                ('food_title', models.CharField(max_length=255)),
                ('food_description', models.CharField(max_length=255)),
                ('food_price', models.IntegerField()),
                ('total_rating', models.CharField(max_length=255)),
                ('total_raters', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['food_title'],
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(max_length=255)),
                ('order_id', models.CharField(max_length=255)),
                ('food_id_array', models.CharField(max_length=255)),
                ('total_price', models.IntegerField()),
                ('is_payment_verified', models.BooleanField(default=False)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('is_shipped', models.BooleanField(default=False)),
                ('is_delivered', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['order_id'],
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(max_length=255)),
                ('client_username', models.CharField(max_length=255)),
                ('message', models.TextField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['date_created'],
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendorname', models.CharField(max_length=255)),
                ('businessphonenumber', models.CharField(max_length=255)),
                ('businessemail', models.CharField(blank=True, max_length=255, null=True)),
                ('mainbusinessaddress', models.CharField(blank=True, max_length=255, null=True)),
                ('total_rating', models.CharField(max_length=255)),
                ('total_raters', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['vendorname'],
            },
        ),
    ]
