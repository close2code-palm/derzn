# Generated by Django 3.2.4 on 2022-04-20 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drevo', '0010_author_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата и время редактирования'),
        ),
    ]
