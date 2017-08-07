from django.conf.urls import url
from second_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^help/', views.help, name='help'),
    url(r'^banjo_club', views.banjo_club, name = 'banjo_club'),
]
