from django.urls import path, include
from rest_framework import routers
from . import views 

router = routers.DefaultRouter()
router.register(r'clientprofiles', views.ClientProfileViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'employees', views.EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls))
]