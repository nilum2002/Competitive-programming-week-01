
# You are given a list of N integers stock_prices, where stock_prices[i] represents the stock price on the i-th day.

# For each day, determine how many days you have to wait until a higher stock price appears in the future. If no such day exists, return 0 for that day.

# Return the result as a space-separated string of integers.

# Input Format

# The first line contains an integer N (1 ≤ N ≤ 10⁷) — the number of days.

# The second line contains N space-separated integers prices[i] (1 ≤ prices[i] ≤ 10⁵) — the stock prices on each day.

# Constraints

# 1 ≤ N ≤ 10⁷

# 1 ≤ stock_prices[i] ≤ 10⁵

# Output Format

# Print a single line containing N space-separated integers, where the i-th integer represents the number of days you have to wait after the i-th day to get a higher stock price. If no future day has a higher price, print 0 for that day.

# Sample Input 0

# 8
# 100 101 102 98 95 99 105 100
# Sample Output 0

# 1 1 4 2 1 1 0 0
# Sample Input 1

# 4
# 20 30 25 35
# Sample Output 1

# 1 2 1 0

def days_to_stock_price(stock_prices):
    res = [0]*len(stock_prices)
    stack = []


    for i in range(len(stock_prices)):
        while len(stack) != 0 and stock_prices[i] > stock_prices[stack[-1]]:
            index = stack.pop()
            #stack.append(stock_prices[i])
            res[index] = i - index

        stack.append(i)
    print(res)
stock_prices = [20, 30, 25, 35]


days_to_stock_price(stock_prices)





