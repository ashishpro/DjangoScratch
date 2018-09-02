from django.db import models
from django.utils import timezone
from rest_framework.exceptions import ValidationError


YEAR_CHOICES = []
for r in range(1980, (timezone.now().year + 1)):
    YEAR_CHOICES.append((r, r))


class Album(models.Model):
    artist = models.CharField(max_length=50)
    album_title = models.TextField(null=True, blank=True)
    genre = models.CharField(max_length=50)
    album_logo = models.CharField(max_length=1000)
    _year = models.IntegerField(default=timezone.now().year, null=True, db_column='year')

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if value > timezone.now().year:
            ValidationError("Future year can't be selected")
        self._year = value

    class Meta:
        ordering = ['_year']
        db_table = 'album'


class Songs(models.Model):
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    title = models.TextField()

    class Meta:
        ordering = ['title']
        db_table = 'songs'

