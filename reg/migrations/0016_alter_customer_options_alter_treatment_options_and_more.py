# Generated by Django 4.0.6 on 2022-08-12 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0015_treatment_customer_treatment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='treatment',
            options={'ordering': ['treatment_type']},
        ),
        migrations.RemoveField(
            model_name='customer',
            name='treatment',
        ),
    ]
