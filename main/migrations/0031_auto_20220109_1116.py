# Generated by Django 3.1.7 on 2022-01-09 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_auto_20220108_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passedapprovals',
            name='approvalsname',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.attvalid'),
        ),
    ]
