# Generated by Django 4.2.3 on 2023-07-21 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='usertype',
            field=models.CharField(choices=[('U', 'Upper Class'), ('M', 'Middle Class'), ('L', 'Lower Class')], default='M', max_length=20),
        ),
    ]
