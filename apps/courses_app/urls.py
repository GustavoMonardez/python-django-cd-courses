from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r"^$", views.index),
    url(r"^courses/new$", views.new),
    url(r"^courses/destroy/(?P<course_id>\d+)$", views.confirm),
    url(r"^courses/destroy/(?P<course_id>\d+)/confirm$", views.destroy)
]