# Generated by Django 4.0.6 on 2022-10-04 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0007_alter_customer_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
