# Generated by Django 2.2.1 on 2019-05-08 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistem', '0006_auto_20190508_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bolum',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sistem.Bolum', verbose_name='Bolumu'),
        ),
    ]
