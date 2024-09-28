from blind_75.two_sum import two_sum

def test_basic_case():
    nums = [2, 7, 11, 15]
    target = 9
    assert two_sum(nums, target) == [0, 1]

def test_no_solution():
    nums = [2, 7, 11, 15]
    target = 100
    assert two_sum(nums, target) == []