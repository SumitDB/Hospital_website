# Generated by Django 4.0.6 on 2022-08-17 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0019_remove_customer_treatment_customer_details_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='treatment_type_1',
            field=models.CharField(choices=[('Injection', 'Injection'), ('Medicines/Capsules', 'Medicines/Capsules'), ('Syrup', 'Syrup'), ('Tube', 'Tube')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='treatment_type_2',
            field=models.CharField(choices=[('Injection', 'Injection'), ('Medicines/Capsules', 'Medicines/Capsules'), ('Syrup', 'Syrup'), ('Tube', 'Tube')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='treatment_type_3',
            field=models.CharField(choices=[('Injection', 'Injection'), ('Medicines/Capsules', 'Medicines/Capsules'), ('Syrup', 'Syrup'), ('Tube', 'Tube')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='treatment_type_4',
            field=models.CharField(choices=[('Injection', 'Injection'), ('Medicines/Capsules', 'Medicines/Capsules'), ('Syrup', 'Syrup'), ('Tube', 'Tube')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='treatment_type_5',
            field=models.CharField(choices=[('Injection', 'Injection'), ('Medicines/Capsules', 'Medicines/Capsules'), ('Syrup', 'Syrup'), ('Tube', 'Tube')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='treatment_type_6',
            field=models.CharField(choices=[('Injection', 'Injection'), ('Medicines/Capsules', 'Medicines/Capsules'), ('Syrup', 'Syrup'), ('Tube', 'Tube')], max_length=100, null=True),
        ),
    ]
