# Generated by Django 4.0.6 on 2022-07-25 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_extension_number_users_extension'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='profile_image_name',
            field=models.ImageField(blank=True, db_column='txt_image', default=None, max_length=256, null=True, upload_to=''),
        ),
    ]
