# Generated by Django 5.1 on 2024-10-06 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_doctorreview_delete_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='google_meet_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]