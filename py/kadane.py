#Kadane Algorithm Python Implementation

def maxProfit(prices):
    if len(prices) == 0:
        return 0
    else:
        _max = 0
        _min = prices[0]
        for price in range(len(prices)):
            if (prices[price] > _min) :
                _max = max(_max, prices[price]-_min)
            else :
                _min = prices[price]
        return _max

L = [7, 1, 5, 3, 6, 4]
print maxProfit(L)
