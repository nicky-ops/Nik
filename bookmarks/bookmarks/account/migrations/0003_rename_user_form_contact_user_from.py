# Generated by Django 4.1.13 on 2024-05-20 09:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0002_contact_contact_account_con_created_8bdae6_idx"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contact",
            old_name="user_form",
            new_name="user_from",
        ),
    ]
