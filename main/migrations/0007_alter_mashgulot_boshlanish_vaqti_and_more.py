# Generated by Django 5.0 on 2024-01-05 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_boshlainish_vaqti_mashgulot_boshlanish_vaqti_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mashgulot',
            name='boshlanish_vaqti',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='mashgulot',
            name='tugash_vaqti',
            field=models.TimeField(),
        ),
    ]
