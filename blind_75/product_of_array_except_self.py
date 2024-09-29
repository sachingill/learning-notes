def product_except_self(series: list[int]) -> list[int]:
    if not series:
        return []
    if len(series) < 2:
        return [1] * len(series)
    n = len(series)
    prod_array = [1] * n
    prod_before = 1
    for index, num in enumerate(series):
        prod_array[index] *= prod_before
        prod_before *= num
    prod_after =1
    for i in range(n -1, -1, -1):
        prod_array[i] *= prod_after
        prod_after *= series[i]
    return prod_array