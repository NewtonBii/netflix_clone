from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
 url(r'^$', views.movies, name='myMovies'),
 url(r'^movie/(\d+)', views.single_movie, name = 'oneMovie')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
