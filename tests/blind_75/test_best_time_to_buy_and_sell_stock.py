import pytest
from blind_75.best_time_to_buy_and_sell_stock import max_profit
"""Best Time to Buy and Sell Stock". Here's the problem statement:
# Problem: Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
def test_basic_case():
    prices = [7,1,5,3,6,4]
    assert max_profit(prices) == 5

def test_no_profit():
    prices = [7,6,4,3,1]
    assert max_profit(prices) == 0

def test_single_price():
    prices = [1]
    assert max_profit(prices) == 0

def test_two_prices_increasing():
    prices = [1,2]
    assert max_profit(prices) == 1

def test_two_prices_decreasing():
    prices = [2,1]
    assert max_profit(prices) == 0

@pytest.mark.parametrize("prices, expected", [
    ([7,1,5,3,6,4], 5),
    ([7,6,4,3,1], 0),
    ([1], 0),
    ([1,2], 1),
    ([2,1], 0),
    ([3,2,6,5,0,3], 4),
])
def test_multiple_cases(prices, expected):
    assert max_profit(prices) == expected