# Generated by Django 3.0.7 on 2020-06-03 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='likenumber',
            new_name='likelion_number',
        ),
    ]
