# best_time_stock_python
class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price 
                max_profit = max(max_profit, profit)

        return max_profit

if __name__ == "__main__":
    prices = {20, 30, 30.5, 50, 100}
    sol = Solution()
    result = sol.maxProfit(prices)
    print("Maximum Profit is ", result)