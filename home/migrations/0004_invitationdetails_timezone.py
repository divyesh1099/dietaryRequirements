# Generated by Django 5.0.1 on 2024-05-20 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_invitationdetails_gift"),
    ]

    operations = [
        migrations.AddField(
            model_name="invitationdetails",
            name="timezone",
            field=models.CharField(default="INR", max_length=40),
            preserve_default=False,
        ),
    ]