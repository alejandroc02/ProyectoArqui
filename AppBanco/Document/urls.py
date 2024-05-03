from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'documents', views.DocumentViewSet)
router.register(r'requests', views.RequestViewSet)

urlpatterns = [
    path('', include(router.urls))
]