# Generated by Django 5.1 on 2024-10-23 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_alter_doctorreview_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='isReviewed',
            field=models.BooleanField(default=False),
        ),
    ]