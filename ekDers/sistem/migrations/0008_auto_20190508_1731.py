# Generated by Django 2.2.1 on 2019-05-08 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistem', '0007_auto_20190508_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dersYuku',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Ders Yuku'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fakulte',
            field=models.CharField(max_length=30, null=True, verbose_name='Fakultesi'),
        ),
    ]