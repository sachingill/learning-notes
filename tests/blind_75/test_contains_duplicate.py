import pytest
from blind_75.contains_duplicate import contains_duplicate

def test_basic_duplicate():
    assert contains_duplicate([1,2,3,1]) == True

def test_no_duplicate():
    assert contains_duplicate([1,2,3,4]) == False

def test_multiple_duplicates():
    assert contains_duplicate([1,1,1,3,3,4,3,2,4,2]) == True

def test_empty_array():
    assert contains_duplicate([]) == False

def test_single_element():
    assert contains_duplicate([1]) == False

@pytest.mark.parametrize("nums, expected", [
    ([1,2,3,1], True),
    ([1,2,3,4], False),
    ([1,1,1,3,3,4,3,2,4,2], True),
    ([], False),
    ([1], False),
    ([1,2,3,4,5,6,7,8,9,1], True),
])
def test_multiple_cases(nums, expected):
    assert contains_duplicate(nums) == expected