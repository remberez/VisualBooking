from rest_framework.routers import DefaultRouter
from booking.view.objects import ObjectView
from booking.view.city import CityView

router = DefaultRouter()

router.register('objects', ObjectView, basename='objects')
router.register('city', CityView, basename='city')

urlpatterns = [

]

urlpatterns += router.urls
