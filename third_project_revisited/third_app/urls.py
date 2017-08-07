from django.conf.urls import url
from third_app import views

urlpatterns = [
    url(r'^$',views.users,name='users')
]
