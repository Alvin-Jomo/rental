# Generated by Django 5.1.5 on 2025-01-30 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0010_booking_contact_booking_room_no'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paymentrecord',
            options={'verbose_name': 'Payment Record', 'verbose_name_plural': 'Payment Records'},
        ),
        migrations.AddField(
            model_name='paymentrecord',
            name='amount_received',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
