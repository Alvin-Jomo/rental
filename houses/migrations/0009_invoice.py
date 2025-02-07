# Generated by Django 5.1.5 on 2025-01-29 18:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0008_paymentrecord_remove_payment_invoice_delete_invoice_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_bill', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('garbage_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='houses.booking')),
            ],
        ),
    ]
