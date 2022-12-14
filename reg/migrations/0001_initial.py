# Generated by Django 4.0.6 on 2022-10-04 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Transgender')], max_length=1, null=True)),
                ('email', models.EmailField(blank=True, max_length=25, null=True)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=10, null=True)),
                ('complaints', models.CharField(blank=True, max_length=100, null=True)),
                ('pulse', models.CharField(blank=True, max_length=10, null=True)),
                ('blood_pressure', models.CharField(blank=True, max_length=10, null=True)),
                ('temprature', models.CharField(blank=True, max_length=10, null=True)),
                ('blood_suger_level', models.CharField(blank=True, max_length=10, null=True)),
                ('genral_exams', models.CharField(blank=True, max_length=100, null=True)),
                ('treatment_type_1', models.CharField(blank=True, choices=[('Injection', 'Injection'), ('Medicines/Capsules', 'Medicines/Capsules'), ('Syrup', 'Syrup'), ('Tube', 'Tube')], max_length=100, null=True)),
                ('treatment_name_1', models.CharField(blank=True, max_length=100, null=True)),
                ('units_1', models.IntegerField(blank=True, null=True)),
                ('details_1', models.CharField(blank=True, max_length=90, null=True)),
                ('treatment_type_2', models.CharField(blank=True, choices=[('Injection', 'Injection'), ('Medicines/Capsules', 'Medicines/Capsules'), ('Syrup', 'Syrup'), ('Tube', 'Tube')], max_length=100, null=True)),
                ('treatment_name_2', models.CharField(blank=True, max_length=100)),
                ('units_2', models.IntegerField(blank=True, null=True)),
                ('details_2', models.CharField(blank=True, max_length=90)),
                ('treatment_type_3', models.CharField(blank=True, choices=[('Injection', 'Injection'), ('Medicines/Capsules', 'Medicines/Capsules'), ('Syrup', 'Syrup'), ('Tube', 'Tube')], max_length=100, null=True)),
                ('treatment_name_3', models.CharField(blank=True, max_length=100, null=True)),
                ('units_3', models.IntegerField(blank=True, null=True)),
                ('details_3', models.CharField(blank=True, max_length=90, null=True)),
                ('treatment_type_4', models.CharField(blank=True, choices=[('Injection', 'Injection'), ('Medicines/Capsules', 'Medicines/Capsules'), ('Syrup', 'Syrup'), ('Tube', 'Tube')], max_length=100, null=True)),
                ('treatment_name_4', models.CharField(blank=True, max_length=100, null=True)),
                ('units_4', models.IntegerField(blank=True, null=True)),
                ('details_4', models.CharField(blank=True, max_length=90)),
                ('treatment_type_5', models.CharField(blank=True, choices=[('Injection', 'Injection'), ('Medicines/Capsules', 'Medicines/Capsules'), ('Syrup', 'Syrup'), ('Tube', 'Tube')], max_length=100, null=True)),
                ('treatment_name_5', models.CharField(blank=True, max_length=100, null=True)),
                ('units_5', models.IntegerField(blank=True, null=True)),
                ('details_5', models.CharField(blank=True, max_length=90, null=True)),
                ('treatment_type_6', models.CharField(blank=True, choices=[('Injection', 'Injection'), ('Medicines/Capsules', 'Medicines/Capsules'), ('Syrup', 'Syrup'), ('Tube', 'Tube')], max_length=100, null=True)),
                ('treatment_name_6', models.CharField(blank=True, max_length=100, null=True)),
                ('units_6', models.IntegerField(blank=True, null=True)),
                ('details_6', models.CharField(blank=True, max_length=90, null=True)),
                ('total_fees', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=70)),
                ('Email', models.EmailField(max_length=254)),
                ('Mobile_no', models.IntegerField()),
                ('Password', models.CharField(max_length=10)),
            ],
        ),
    ]
