# Generated by Django 4.2.3 on 2023-07-21 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_rename_goal_url_budget_goal_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='imgurl',
            new_name='bill_img',
        ),
    ]
