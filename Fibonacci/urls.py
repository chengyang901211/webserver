from django.conf.urls import url

from . import views

urlpatterns = [
    url('Fibonacci/(?P<n>-?\d+)/$', views.Fibonacci, name='Fibonacci'),
]
