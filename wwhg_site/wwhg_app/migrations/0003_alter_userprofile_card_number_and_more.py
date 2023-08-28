# Generated by Django 4.2.4 on 2023-08-28 17:25

from django.db import migrations, models
import wwhg_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('wwhg_app', '0002_shoppingcart_session_key_alter_shoppingcart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='card_number',
            field=models.CharField(max_length=16, validators=[wwhg_app.models.validate_credit_card_number]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=models.CharField(default='Estonia', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(max_length=15, validators=[wwhg_app.models.validate_phone_number]),
        ),
    ]
