from django.conf.urls import url
from . import views
from views import BookListView
urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^books/$', BookListView.as_view()),

]