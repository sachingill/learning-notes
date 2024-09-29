def product_except_self(series: list) -> list[int]:
    if not series:
        return []
    n = len(series)
    if n < 2:
        return [1]
    prod_array = [1] * n
    prod_before = 1
    for num, index  in enumerate(series):
        prod_array[index] *= prod_before
        prod_before *= num
    prod_after =1
    for i in range(n -1, -1, -1):
        prod_array[i] *= prod_after
        prod_after *= series[i]
    return prod_array