from django.conf.urls import url
from . import views

# app_name = 'resapp'

urlpatterns = [
    url(r'^$', views.resumeForm, name='resume_form'),
    url(r'^resumeform', views.resumeForm, name='resume_form'),
    url(r'^resumeview', views.resumeView, name='resume_view'),
]
