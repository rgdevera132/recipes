# Generated by Django 2.0.1 on 2018-02-09 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0007_auto_20180209_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='cookbook.Category'),
        ),
    ]
