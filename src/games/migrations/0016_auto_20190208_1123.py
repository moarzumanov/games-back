# Generated by Django 2.1.5 on 2019-02-08 08:23

from django.db import migrations, models
import games.validators


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0015_auto_20190202_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='game_3_obj',
            name='audio',
            field=models.FileField(blank=True, help_text='до 5 мб', null=True, upload_to='audios/', validators=[games.validators.validate_file_extension, games.validators.validate_file_size], verbose_name='Аудио'),
        ),
        migrations.AddField(
            model_name='game_3_obj',
            name='audio_eng',
            field=models.FileField(blank=True, help_text='до 5 мб', null=True, upload_to='audios/', validators=[games.validators.validate_file_extension, games.validators.validate_file_size], verbose_name='Аудио на английском'),
        ),
    ]
