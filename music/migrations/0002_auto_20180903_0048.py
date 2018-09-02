# Generated by Django 2.0 on 2018-09-02 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['year']},
        ),
        migrations.RemoveField(
            model_name='album',
            name='_year',
        ),
        migrations.AddField(
            model_name='album',
            name='year',
            field=models.IntegerField(default=2018, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]