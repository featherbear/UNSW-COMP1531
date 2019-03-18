import pytest

from booking import Booking

class TestBooking():
  def test_booking(self):
    class _CarStub:
      def calculatePrice(self, *_, **__):
        return 999
    carStub = _CarStub()
    booking = Booking(1, carStub, 3, 4)

    assert(booking.customer == 1)
    assert(booking.car == carStub)
    assert(booking.period == 3)
    assert(booking.location == 4)
    assert(booking.price == 999)