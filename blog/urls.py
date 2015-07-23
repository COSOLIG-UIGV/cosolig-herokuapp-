from django.conf.urls import patterns, include, url
from rest_framework import routers
from .views import PostViewSet
from .views import MiembrosViewSet
router = routers.DefaultRouter()
router.register(r'events', PostViewSet)
router.register(r'miembros', MiembrosViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('cosoligrest.urls', namespace='cosoligrest')),
)