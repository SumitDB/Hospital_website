# Generated by Django 4.0.6 on 2022-08-12 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0014_customer_temprature_alter_customer_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment_type', models.CharField(choices=[('Injection', 'Injection'), ('Medicines/Capsules', 'Medicines/Capsules'), ('Syrup', 'Syrup'), ('Injection', 'Injection'), ('Tube', 'Tube')], max_length=100)),
                ('treatment_name', models.CharField(max_length=100)),
                ('units', models.IntegerField(null=True)),
                ('details', models.CharField(max_length=90)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='treatment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reg.treatment'),
        ),
    ]
