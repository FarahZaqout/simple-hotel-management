from rest_framework.serializers import ModelSerializer
from .models import Hotel, RoomCategory, Room, RoomReservation, Payment


class HotelSerializer(ModelSerializer):
  class Meta():
    model = Hotel
    fields = '__all__'


class RoomCategorySerializer(ModelSerializer):
  class Meta():
    model = RoomCategory
    fields = '__all__'


class RoomSerializer(ModelSerializer):
  class Meta():
    model = Room
    fields = '__all__'


class RoomReservationSerializer(ModelSerializer):
  class Meta():
    model = RoomReservation
    fields = '__all__'


class PaymentSerializer(ModelSerializer):
  class Meta():
    model = Payment
    fields = '__all__'