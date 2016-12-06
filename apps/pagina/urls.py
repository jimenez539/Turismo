from django.conf.urls import url, include
from apps.pagina.views import index

urlpatterns = [
    url(r'^$', index),
]
