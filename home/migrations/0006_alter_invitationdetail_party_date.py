# Generated by Django 5.0.1 on 2024-05-20 13:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_dietpreference_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invitationdetail",
            name="party_date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
