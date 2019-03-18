import pytest

from location import Location

class TestLocation():
  def test_location(self):
    location = Location(None, None)
    assert(location.pickup is None)
    assert(location.dropoff is None)