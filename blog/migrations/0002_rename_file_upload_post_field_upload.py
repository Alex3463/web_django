# Generated by Django 3.2.12 on 2022-08-02 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='file_upload',
            new_name='field_upload',
        ),
    ]