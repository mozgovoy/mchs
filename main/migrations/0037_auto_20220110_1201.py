# Generated by Django 3.1.7 on 2022-01-10 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_auto_20220110_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='initialtrainingperiod',
            name='fullname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='passedapprovals',
            name='approvalsname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.attvalid', verbose_name='Название аттестации'),
        ),
    ]