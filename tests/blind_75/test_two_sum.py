import pytest
from blind_75.two_sum import two_sum


def test_basic_case():
    nums = [2, 7, 11, 15]
    target = 9
    assert sorted(two_sum(nums, target)) == [0, 1]

def test_no_solution():
    nums = [2, 7, 11, 15]
    target = 100
    assert two_sum(nums, target) == []

def test_negative_numbers():
    nums = [-1, -2, -3, -4, -5]
    target = -8
    assert sorted(two_sum(nums, target)) == [2, 4]

def test_duplicate_numbers():
    nums = [3, 3]
    target = 6
    assert sorted(two_sum(nums, target)) == [0, 1]

def test_zero_sum():
    nums = [0, 4, 3, 0]
    target = 0
    result = two_sum(nums, target)
    assert len(result) == 2 and nums[result[0]] + nums[result[1]] == target

def test_larger_numbers():
    nums = [1000000, 1000002, 1000001]
    target = 2000003
    result = two_sum(nums, target)
    assert len(result) == 2 and nums[result[0]] + nums[result[1]] == target

def test_single_number():
    nums = [5]
    target = 5
    assert two_sum(nums, target) == []

@pytest.mark.parametrize("nums, target, expected", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([-1, -2, -3, -4, -5], -8, [2, 4]),
])
def test_multiple_cases(nums, target, expected):
    assert sorted(two_sum(nums, target)) == sorted(expected)