# Generated by Django 4.0.6 on 2022-10-04 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0002_customer_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='date',
        ),
        migrations.AddField(
            model_name='customer',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
