import pytest
from blind_75.search_in_rotated_sorted_array import search

@pytest.mark.parametrize("nums, target, expected", [
    ([4,5,6,7,0,1,2], 0, 4),
    ([4,5,6,7,0,1,2], 3, -1),
    ([1], 0, -1),
    ([1], 1, 0),
    ([3,1], 1, 1),
    ([5,1,3], 3, 2),
])
def test_search(nums, target, expected):
    assert search(nums, target) == expected

def test_empty_array():
    assert search([], 5) == -1