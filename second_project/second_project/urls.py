"""second_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from second_app import views

urlpatterns = [
    url(r'^$',views.index, name = 'index'),
    url(r'^$', views.help, name = 'help'),
    url(r'^$', views.banjo_club, name = 'banjo_club'),
    url(r'^help/', include('second_app.urls')),
    url(r'^banjo_club/', include('second_app.urls')),
    url(r'^second_app/', include('second_app.urls')),
    url(r'^admin/', admin.site.urls),
]
