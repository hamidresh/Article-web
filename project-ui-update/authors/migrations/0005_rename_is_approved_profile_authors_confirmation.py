# Generated by Django 4.2.7 on 2024-01-10 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0004_profile_authors_is_approved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile_authors',
            old_name='is_approved',
            new_name='confirmation',
        ),
    ]
