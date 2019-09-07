from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html',redirect_authenticated_user=True), name= 'login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name= 'logout'),
    url(r'^home/$', views.home, name = 'home'),
    url(r'^profile/$', views.profile, name = 'profile'),
    url(r'^galeria/$', views.galeria, name = 'galeria'),
    url(r'^usimg/$', views.usimg, name = 'usimg'),
    url(r'^opciones/$', views.opciones, name = 'opciones'),


]
