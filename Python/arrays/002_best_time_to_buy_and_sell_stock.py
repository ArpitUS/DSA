# 002 — Best Time to Buy and Sell Stock

# Given an array prices where prices[i] is the price of a stock on day i, maximize profit by choosing one day to buy and one later day to sell.

# Return maximum profit. If no profit possible, return 0.

# Example

# Input: [7,1,5,3,6,4]
# Output: 5

input_prices = [7, 1, 5, 3, 6, 4]

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
            
    return max_profit

print(max_profit(input_prices))  # Output: 5