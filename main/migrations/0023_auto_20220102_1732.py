# Generated by Django 3.1.7 on 2022-01-02 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20220102_1729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passedapprovals',
            old_name='peopleid',
            new_name='fullname',
        ),
    ]
