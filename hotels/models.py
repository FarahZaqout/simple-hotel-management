from django.db import models
from users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

''' Room rates should be variables that go into the the min and max validator '''

# Hotel model
class Hotel(models.Model):
  name = models.CharField(max_length=200)
  owner = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name


class RoomCategories(models.Model):
  name = models.CharField(max_length=20)
  rate = models.IntegerField(default=75, validators=[MinValueValidator(75), MaxValueValidator(150)])

  def __str__(self):
    return f'Category: {self.name}, Rate: ${str(self.rate)}'


class Rooms(models.Model):
  number = models.CharField(
    verbose_name = 'room number',
    max_length = 3,
  )
  hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
  category = models.ForeignKey(RoomCategories, on_delete=models.CASCADE)

  def __str__(self):
    return f'Hotel: {self.hotel}, Room: {self.number}'


class RoomReservations(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  starting_date = models.DateTimeField(verbose_name='reserved from')
  ending_date = models.DateTimeField(verbose_name='reserved until')
  room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  is_deleted = models.BooleanField(default=False)

  def __str__(self):
    return f'Room: {self.room},
    from: {self.starting_date},
    until:{self.ending_date},
    deleted: {self.is_deleted}'


class Payment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  amount = models.IntegerField(validators=[MinValueValidator(75), MaxValueValidator(150)])
