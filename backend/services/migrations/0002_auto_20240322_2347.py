# Generated by Django 3.2.15 on 2024-03-22 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoryservice',
            options={'verbose_name': 'категория сервисов', 'verbose_name_plural': 'Категории сервисов'},
        ),
        migrations.AddField(
            model_name='service',
            name='url',
            field=models.URLField(default=1, verbose_name='Ссылка на сервис'),
            preserve_default=False,
        ),
    ]
