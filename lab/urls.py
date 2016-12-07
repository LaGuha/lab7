from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.auth, name='auth'),
    url(r'^enter$', views.enter, name='enter'),
    url(r'^1$', views.auth1, name='auth'),
    url(r'^main/$', views.main, name='main'),

]