import pytest
from blind_75.maximum_product_subarray import max_product

@pytest.mark.parametrize("nums, expected", [
    ([2,3,-2,4], 6),
    ([-2,0,-1], 0),
    ([-2,3,-4], 24),
    ([0,2], 2),
    ([-2,3,4], 12),
    ([-4,-3,-2], 12),
])
def test_max_product(nums, expected):
    assert max_product(nums) == expected

def test_empty_array():
    with pytest.raises(ValueError):
        max_product([])

def test_single_element():
    assert max_product([5]) == 5
    assert max_product([-5]) == -5