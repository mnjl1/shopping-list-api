# Generated by Django 4.0.5 on 2023-03-05 14:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=100)),
                ('purchased', models.BooleanField()),
            ],
        ),
    ]
