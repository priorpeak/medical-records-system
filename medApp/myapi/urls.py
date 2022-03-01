from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'billing', views.BillingViewSet)
router.register(r'medical_history', views.Medical_HistoryViewSet)
router.register(r'roles', views.RolesViewSet)
router.register(r'user_roles', views.User_RolesViewSet)
router.register(r'measurements', views.MeasurementsViewSet)
router.register(r'device', views.DeviceViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]