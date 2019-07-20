from rest_framework.routers import DefaultRouter
from .views import (HotelView,
  RoomCategoryView,
  RoomView,
  RoomReservationView,
  PaymentView)

router = DefaultRouter()
router.register('hotels', HotelView)
router.register('categories', RoomCategoryView)
router.register('rooms', RoomView)
router.register('reservations', RoomReservationView)
router.register('payments', PaymentView)

urlpatterns = router.urls