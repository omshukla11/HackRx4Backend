# Generated by Django 4.2.3 on 2023-07-21 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0005_rename_bill_img_transaction_billimg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='billimg',
            new_name='bill_img',
        ),
    ]
