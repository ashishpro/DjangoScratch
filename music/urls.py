from rest_framework.routers import SimpleRouter
from django.conf.urls import url
from . import views
from django.urls import path

router = SimpleRouter()
router.register('songs', views.SongsView)
router.register('album', views.AlbumView)
urlpatterns = router.urls
