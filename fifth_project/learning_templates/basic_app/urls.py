from django.conf.urls import url
from basic_app import views

# TEMPLATE TAGGING SCRIPT - you need the global - app_name in order to facilitate django to find the templates for the app
app_name = 'basic_app'
urlpatterns= [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$', views.other, name='other'),
]
