# Generated by Django 3.1.7 on 2022-01-02 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20220102_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='attvalid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.passedapprovals', verbose_name='Аттестация'),
        ),
    ]
