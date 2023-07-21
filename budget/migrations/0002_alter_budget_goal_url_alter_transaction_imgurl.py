# Generated by Django 4.2.3 on 2023-07-21 05:36

import budget.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='goal_url',
            field=models.ImageField(blank=True, null=True, upload_to=budget.models.upload_goal_img_path_handler),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='imgurl',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
