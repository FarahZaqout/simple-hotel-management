from .serializers import (HotelSerializer,
  RoomCategorySerializer,
  RoomSerializer,
  RoomReservationSerializer,
  PaymentSerializer)
from .models import (Hotel, RoomCategory, Room, RoomReservation, Payment)
from rest_framework.viewsets import ModelViewSet


# Create your views here.
class HotelView(ModelViewSet):
  queryset = Hotel.objects.all()
  serializer_class = HotelSerializer


class RoomCategoryView(ModelViewSet):
    queryset = RoomCategory.objects.all()
    serializer_class = RoomCategorySerializer


class RoomView(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomReservationView(ModelViewSet):
    queryset = RoomReservation.objects.all()
    serializer_class = RoomReservationSerializer


class PaymentView(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
