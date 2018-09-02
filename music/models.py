from django.db import models
from django.utils import timezone
from rest_framework.exceptions import ValidationError


YEAR_CHOICES = []
for r in range(1980, (timezone.now().year + 1)):
    YEAR_CHOICES.append((r, r))


class Album(models.Model):
    artist = models.CharField(max_length=50)
    album_title = models.TextField(null=True, blank=True)
    genre = models.CharField(max_length=50,null=True, blank=True)
    album_logo = models.CharField(max_length=1000,null=True, blank=True)
    year = models.IntegerField(default=timezone.now().year, null=True)

    class Meta:
        ordering = ['year']
        db_table = 'album'

    def save(self, **kwargs):
        if self.year > timezone.now().year:
            raise ValidationError("Invalid Year")
        super(Album, self).save(**kwargs)


class Songs(models.Model):
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    title = models.TextField()

    class Meta:
        ordering = ['title']
        db_table = 'songs'

