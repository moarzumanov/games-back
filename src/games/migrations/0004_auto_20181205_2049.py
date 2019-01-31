# Generated by Django 2.1.3 on 2018-12-05 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20181111_2041'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game_1_obj',
            options={'verbose_name': 'Объект игры №1', 'verbose_name_plural': 'Массив изображений №1'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователя (родителя)', 'verbose_name_plural': 'Пользователи (родители)'},
        ),
        migrations.AddField(
            model_name='game_1_obj',
            name='last_changed',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='game_1_obj',
            name='image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Загрузить изображение'),
        ),
    ]
