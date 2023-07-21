# Generated by Django 4.2.3 on 2023-07-21 13:51

import budget.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0007_ocr_remove_transaction_bill_img'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OCR',
        ),
        migrations.AddField(
            model_name='transaction',
            name='bill_img',
            field=models.ImageField(blank=True, null=True, upload_to=budget.models.upload_bill_img_path_handler),
        ),
    ]