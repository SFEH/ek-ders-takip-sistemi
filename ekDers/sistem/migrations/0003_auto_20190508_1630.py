# Generated by Django 2.2.1 on 2019-05-08 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistem', '0002_auto_20190507_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bolum',
            field=models.CharField(choices=[('Bilgisayar Mühendisliği', 'Bilgisayar Mühendisliği'), ('Makine Mühendisliği', 'Makine Mühendisliği'), ('İnşaat Mühendisliği', 'İnşaat Mühendisliği'), ('Elektrik-Elektronik Mühendisliği', 'Elektrik-Elektronik Mühendisliği'), ('Genetik ve Biyomühendislik', 'Genetik ve Biyomühendislik'), ('Metalurji ve Malzeme Mühendisliği', 'Metalurji ve Malzeme Mühendisliği'), ('Gıda Mühendisliği', 'Gıda Mühendisliği'), ('İşletme Mühendisliği', 'İşletme Mühendisliği'), ('Endüstri Mühendisliği', 'Endüstri Mühendisliği')], max_length=50),
        ),
    ]
