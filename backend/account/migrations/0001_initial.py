# Generated by Django 4.2.7 on 2023-12-13 15:51

import account.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(error_messages={'blank': 'Это обязательное поле.', 'unique': 'Имя пользователя занято.'}, max_length=64, unique=True, validators=[account.validators.validate_username])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
