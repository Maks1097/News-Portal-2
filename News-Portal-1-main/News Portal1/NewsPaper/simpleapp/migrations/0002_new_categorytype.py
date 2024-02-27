# Generated by Django 5.0 on 2024-01-15 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='categoryType',
            field=models.CharField(choices=[('NW', 'Новости'), ('AR', 'Статья')], default='NW', max_length=2),
        ),
    ]