import math
from number_list import *


def test_reverse():
    assert find_reverse([0]) == [0]
    assert find_reverse([-3, -2, -1, 0, 1, 2, 3])               == [3, 2, 1, 0, -1, -2, -3]
    assert find_reverse([0, 0, 2, 2, 2, 12, 12])                == [12, 12, 2, 2, 2, 0, 0]
    assert find_reverse([30, 22, 12, 2, 3, -1])                 == [-1, 3, 2, 12, 22, 30]
    assert find_reverse([0, 0, 0, 0, 0, 0, 0])                  == [0, 0, 0, 0, 0, 0, 0] 
    assert find_reverse([-3, 52, 0, 12, 0, 2, 3, -1])           == [-1, 3, 2, 0, 12, 0, 52, -3] 
    assert find_reverse([-3.2, 5.2, 0.341, -2, 3.32, -1.22])    == [-1.22, 3.32, -2, 0.341, 5.2, -3.2]
    assert find_reverse([-67, 5, 32.5, -322, 123.33, 434.1])    == [434.1, 123.33, -322, 32.5, 5, -67]



def test_max():
    assert find_max([0]) == 0
    assert find_max([-3, -2, -1, 0, 1, 2, 3])               == 3
    assert find_max([0, 0, 2, 2, 2, 12, 12])                == 12 
    assert find_max([30, 22, 12, 2, 3, -1])                 == 30 
    assert find_max([0, 0, 0, 0, 0, 0, 0])                  == 0 
    assert find_max([-3, 52, 0, 12, 0, 2, 3, -1])           == 52 
    assert find_max([-3.2, 5.2, 0.341, -2, 3.32, -1.22])    == 5.2
    assert find_max([-67, 5, 32.5, -322, 123.33, 434.1])    == 434.1


def test_min():
    assert find_min([0]) == 0
    assert find_min([-3, -2, -1, 0, 1, 2, 3])               == -3
    assert find_min([0, 0, 2, 2, 2, 12, 12])                == 0 
    assert find_min([30, 22, 12, 2, 3, -1])                 == -1 
    assert find_min([0, 0, 0, 0, 0, 0, 0])                  == 0 
    assert find_min([-3, 52, 0, 12, 0, 2, 3, -1])           == -3 
    assert find_min([-3.2, 5.2, 0.341, -2, 3.32, -1.22])    == -3.2
    assert find_min([-67, 5, 32.5, -322, 123.33, 434.1])    == -322


def test_sum():
    assert math.isclose(find_sum([0]), 0)
    assert math.isclose(find_sum([-3, -2, -1, 0, 1, 2, 3]), 0)
    assert math.isclose(find_sum([0, 0, 2, 2, 2, 12, 12]), 30)
    assert math.isclose(find_sum([30, 22, 12, 2, 3, -1]), 68)
    assert math.isclose(find_sum([0, 0, 0, 0, 0, 0, 0]), 0)
    assert math.isclose(find_sum([-3, 52, 0, 12, 0, 2, 3, -1]), 65)
    assert math.isclose(find_sum([-3.2, 5.2, 0.341, -2, 3.32, -1.22]), 2.441)
    assert math.isclose(find_sum([-67, 5, 32.5, -322, 123.33, 434.1]), 205.93)

def test_average():
    assert math.isclose(find_average([0]), 0.0)
    assert math.isclose(find_average([-3, -2, -1, 0, 1, 2, 3]), 0.0)
    assert math.isclose(find_average([0, 0, 2, 2, 2, 12, 12]), 4.285714285714286)
    assert math.isclose(find_average([30, 22, 12, 2, 3, -1]), 11.333333333333334)
    assert math.isclose(find_average([0, 0, 0, 0, 0, 0, 0]), 0.0)
    assert math.isclose(find_average([-3, 52, 0, 12, 0, 2, 3, -1]), 8.125)
    assert math.isclose(find_average([-3.2, 5.2, 0.341, -2, 3.32, -1.22]), 0.4068333333333333)
    assert math.isclose(find_average([-67, 5, 32.5, -322, 123.33, 434.1]), 34.321666666666665)

def test_descending():
    assert find_descending([0]) == [0]
    assert find_descending([-3, -2, -1, 0, 1, 2, 3]) == [3, 2, 1, 0, -1, -2, -3]
    assert find_descending([0, 0, 2, 2, 2, 12, 12]) == [12, 12, 2, 2, 2, 0, 0]
    assert find_descending([30, 22, 12, 2, 3, -1]) == [30, 22, 12, 3, 2, -1]
    assert find_descending([0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0]
    assert find_descending([-3, 52, 0, 12, 0, 2, 3, -1]) == [52, 12, 3, 2, 0, 0, -1, -3]
    assert find_descending([-3.2, 5.2, 0.341, -2, 3.32, -1.22]) == [5.2, 3.32, 0.341, -1.22, -2, -3.2]
    assert find_descending([-67, 5, 32.5, -322, 123.33, 434.1]) == [434.1, 123.33, 32.5, 5, -67, -322]


def test_second_smallest():
    assert second_smallest([-3, -2, -1, 0, 1, 2, 3]) == -2
    assert second_smallest([0, 0, 2, 2, 2, 12, 12]) == 2
    assert second_smallest([30, 22, 12, 2, 3, -1]) == 2
    assert second_smallest([2, 4, -23, 2, 95, 21]) == 2
    assert second_smallest([-1, -1, -1, 5, -1, -2, 3, 2]) == -1
    assert second_smallest([-1, -2, -1, 5, -1, -2, 3, 2]) == -1
    assert second_smallest([-3, 52, 0, 12, 0, 2, 3, -1]) == -1
    assert second_smallest([-3.2, 5.2, 0.341, -2, 3.32, -1.22]) == -2
    assert second_smallest([-67, 5, 32.5, -322, 123.33, 434.1]) == -67



def test_kth_smallest():
    assert kth_smallest([0], 1) == 0
    assert kth_smallest([-3, -2, -1, 0, 1, 2, 3], 1) == -3
    assert kth_smallest([-3, -2, -1, 0, 1, 2, 3], 2) == -2
    assert kth_smallest([-3, -2, -1, 0, 1, 2, 3], 3) == -1
    assert kth_smallest([-3, -2, -1, 0, 1, 2, 3], 4) == 0
    assert kth_smallest([-3, -2, -1, 0, 1, 2, 3], 5) == 1
    assert kth_smallest([-3, -2, -1, 0, 1, 2, 3], 6) == 2
    assert kth_smallest([-3, -2, -1, 0, 1, 2, 3], 7) == 3
    assert kth_smallest([0, 0, 2, 2, 2, 12, 12], 1) == 0
    assert kth_smallest([0, 0, 2, 2, 2, 12, 12], 2) == 2
    assert kth_smallest([0, 0, 2, 2, 2, 12, 12], 3) == 12
    assert kth_smallest([30, 22, 12, 2, 3, -1], 1) == -1
    assert kth_smallest([30, 22, 12, 2, 3, -1], 2) == 2
    assert kth_smallest([30, 22, 12, 2, 3, -1], 3) == 3
    assert kth_smallest([30, 22, 12, 2, 3, -1], 4) == 12
    assert kth_smallest([30, 22, 12, 2, 3, -1], 5) == 22
    assert kth_smallest([30, 22, 12, 2, 3, -1], 6) == 30
    assert kth_smallest([0, 0, 0, 0, 0, 0, 0], 1) == 0
    assert kth_smallest([2, 4, -23, 2, 95, 21], 1) == -23
    assert kth_smallest([2, 4, -23, 2, 95, 21], 2) == 2
    assert kth_smallest([2, 4, -23, 2, 95, 21], 3) == 4
    assert kth_smallest([2, 4, -23, 2, 95, 21], 4) == 21
    assert kth_smallest([2, 4, -23, 2, 95, 21], 5) == 95
    assert kth_smallest([-1, -1, -1, 5, -1, -2, 3, 2], 1) == -2
    assert kth_smallest([-1, -1, -1, 5, -1, -2, 3, 2], 2) == -1
    assert kth_smallest([-1, -1, -1, 5, -1, -2, 3, 2], 3) == 2
    assert kth_smallest([-1, -1, -1, 5, -1, -2, 3, 2], 4) == 3
    assert kth_smallest([-1, -1, -1, 5, -1, -2, 3, 2], 5) == 5
    assert kth_smallest([-1, -2, -1, 5, -1, -2, 3, 2], 1) == -2
    assert kth_smallest([-1, -2, -1, 5, -1, -2, 3, 2], 2) == -1
    assert kth_smallest([-1, -2, -1, 5, -1, -2, 3, 2], 3) == 2
    assert kth_smallest([-1, -2, -1, 5, -1, -2, 3, 2], 4) == 3
    assert kth_smallest([-1, -2, -1, 5, -1, -2, 3, 2], 5) == 5
    assert kth_smallest([-3, 52, 0, 12, 0, 2, 3, -1], 1) == -3
    assert kth_smallest([-3, 52, 0, 12, 0, 2, 3, -1], 2) == -1
    assert kth_smallest([-3, 52, 0, 12, 0, 2, 3, -1], 3) == 0
    assert kth_smallest([-3, 52, 0, 12, 0, 2, 3, -1], 4) == 2
    assert kth_smallest([-3, 52, 0, 12, 0, 2, 3, -1], 5) == 3
    assert kth_smallest([-3, 52, 0, 12, 0, 2, 3, -1], 6) == 12
    assert kth_smallest([-3, 52, 0, 12, 0, 2, 3, -1], 7) == 52
    assert kth_smallest([-3.2, 5.2, 0.341, -2, 3.32, -1.22], 1) == -3.2
    assert kth_smallest([-3.2, 5.2, 0.341, -2, 3.32, -1.22], 2) == -2
    assert kth_smallest([-3.2, 5.2, 0.341, -2, 3.32, -1.22], 3) == -1.22
    assert kth_smallest([-3.2, 5.2, 0.341, -2, 3.32, -1.22], 4) == 0.341
    assert kth_smallest([-3.2, 5.2, 0.341, -2, 3.32, -1.22], 5) == 3.32
    assert kth_smallest([-3.2, 5.2, 0.341, -2, 3.32, -1.22], 6) == 5.2
    assert kth_smallest([-67, 5, 32.5, -322, 123.33, 434.1], 1) == -322
    assert kth_smallest([-67, 5, 32.5, -322, 123.33, 434.1], 2) == -67
    assert kth_smallest([-67, 5, 32.5, -322, 123.33, 434.1], 3) == 5
    assert kth_smallest([-67, 5, 32.5, -322, 123.33, 434.1], 4) == 32.5
    assert kth_smallest([-67, 5, 32.5, -322, 123.33, 434.1], 5) == 123.33
    assert kth_smallest([-67, 5, 32.5, -322, 123.33, 434.1], 6) == 434.1