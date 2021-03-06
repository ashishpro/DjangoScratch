# Generated by Django 2.0 on 2018-09-02 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=50)),
                ('album_title', models.TextField(blank=True, null=True)),
                ('genre', models.CharField(max_length=50)),
                ('album_logo', models.CharField(max_length=1000)),
                ('_year', models.IntegerField(db_column='year', default=2018, null=True)),
            ],
            options={
                'db_table': 'album',
                'ordering': ['_year'],
            },
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Album')),
            ],
            options={
                'db_table': 'songs',
                'ordering': ['title'],
            },
        ),
    ]
