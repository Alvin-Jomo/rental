# Generated by Django 5.1.5 on 2025-01-26 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0003_complaint'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='contacts',
            new_name='contact',
        ),
        migrations.RenameField(
            model_name='complaint',
            old_name='created_at',
            new_name='date_submitted',
        ),
        migrations.RenameField(
            model_name='complaint',
            old_name='admin_response',
            new_name='response',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='is_resolved',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='response_media',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='user',
        ),
        migrations.AddField(
            model_name='complaint',
            name='date_responded',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='complaint_images/'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='complaint_videos/'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='room_number',
            field=models.CharField(max_length=10),
        ),
    ]
