# Generated by Django 2.2 on 2019-06-07 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_delete_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Download',
            fields=[
                ('token', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('contentid', models.IntegerField()),
                ('filename', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'download',
                'managed': False,
            },
        ),
    ]