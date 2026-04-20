// 002 — Best Time to Buy and Sell Stock

// Given an array prices where prices[i] is the price of a stock on day i, maximize profit by choosing one day to buy and one later day to sell.

// Return maximum profit. If no profit possible, return 0.

// Example

// Input: [7,1,5,3,6,4]
// Output: 5

package arrays

func maxProfit(prices []int) int {
	minPrice := prices[0]
	maxProfit := 0

	for _, price := range prices {
		if price < minPrice {
			minPrice = price
		} else if price-minPrice > maxProfit {
			maxProfit = price - minPrice
		}
	}

	return maxProfit
}
