def max_profit(prices: int) -> int:
    #track the macx profit and reset the max_profit if another window increases.
    # start with first element, check difference with next element if grater rest the preserve the max profit value
    if not prices:
        return 0
    
    if len(prices) < 2:
        return 0
    
    max_profit: int = 0
    left = 0
    right  = 1
    while  right < len(prices):
        if(prices[left] < prices[right]):
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        else:
            left = right
        
        right +=1
    return max_profit
       
        



            



 
   


    




    


