# Generated by Django 2.0 on 2018-05-05 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0004_auto_20180505_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beat',
            name='genre',
            field=models.CharField(choices=[('BONGO', 'bongo'), ('GOSPEL', 'gospel'), ('REGGAE', 'reggae'), ('HIPHOP', 'hiphop'), ('BLUES', 'blues'), ('R & B', 'r & b'), ('ROCK', 'rock'), ('SOUND TRACK', 'sound_track')], max_length=25),
        ),
        migrations.AlterField(
            model_name='beat',
            name='playback',
            field=models.FileField(upload_to='media/'),
        ),
    ]
