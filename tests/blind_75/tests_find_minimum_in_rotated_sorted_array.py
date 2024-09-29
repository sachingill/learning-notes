import pytest
from blind_75.find_minimum_in_rotated_sorted_array import find_min

@pytest.mark.parametrize("nums, expected", [
    ([3,4,5,1,2], 1),
    ([4,5,6,7,0,1,2], 0),
    ([11,13,15,17], 11),
    ([2,1], 1),
    ([1], 1),
])
def test_find_min(nums, expected):
    assert find_min(nums) == expected

def test_empty_array():
    with pytest.raises(ValueError):
        find_min([])