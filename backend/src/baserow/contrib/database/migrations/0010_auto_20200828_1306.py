# Generated by Django 2.2.11 on 2020-08-28 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0009_linkrowfield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textfield',
            name='text_default',
            field=models.CharField(
                blank=True,
                default='',
                help_text='If set, this value is going to be added every time a new '
                          'row created.',
                max_length=255
            ),
        ),
    ]
