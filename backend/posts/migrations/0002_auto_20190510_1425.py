# Generated by Django 2.2 on 2019-05-10 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='checklist',
            table='Checklist',
        ),
        migrations.AlterModelTable(
            name='contentstate',
            table='Contentstate',
        ),
    ]
