
from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index, name='contact page'),
    #url(r'^movie/', include('movie.urls'), name='movie'),
]
