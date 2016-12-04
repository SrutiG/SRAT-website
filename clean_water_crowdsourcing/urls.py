from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'register/', views.register, name='register'),
    url(r'main/', views.main, name='main'),
    url(r'addReport/', views.addReport, name='addReport'),
    url(r'addPurityReport/', views.addPurityReport, name='addPurityReport'),
    url(r'deleteReport/(?P<reportNum>[0-9]+)', views.deleteReport, name='deleteReport'),
]