from django.contrib import admin
from .models import Songs, Album
from django_admin_listfilter_dropdown.filters import DropdownFilter

# Register your models here.


class SongsAdmin(admin.ModelAdmin):
    fields = ('album', 'title')
    search_fields = ['title', 'id']
    list_display = ('album', 'title')


class AlbumAdmin(admin.ModelAdmin):
    fields = ('artist', 'album_title', 'genre', 'album_logo', 'year')
    search_fields = ['artist', 'album_title']
    list_filter = (
        ('year', DropdownFilter),
        ('album_title', DropdownFilter)
    )
    list_display = ['artist', 'album_title', 'genre', 'year']


admin.site.register(Songs, SongsAdmin)
admin.site.register(Album, AlbumAdmin)

