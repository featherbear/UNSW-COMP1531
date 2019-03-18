import pytest

from customer import Customer

class TestCustomer():
  def test_customer(self):
    customer = Customer(1, 2, 3, 4)
    assert(customer.name is 1)
    assert(customer.age is 2)
    assert(customer.licence is 3)
    assert(customer.email is 4)