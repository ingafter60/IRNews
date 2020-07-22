"""_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
# from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from news import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^$', views.home, name="homepage"),
    url(r'^$', views.IndexView.as_view(), name="homepage"),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^login/$', auth_views.login, name="login"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    # url(r'^logout/$', auth_views.logout, name="logout"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),

]
