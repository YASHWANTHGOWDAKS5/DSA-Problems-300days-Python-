#day two of 300 days of DSA problems chllenge
#Buying and selling of stocks at right time
#EG:list=[5,1,3,6,8]
#buying=1
#sell at 8
#profit=7
def Sales(prices):
    min = float('inf')
    profit = 0

    for price in prices:
        if price < min:
            min = price
        else:
            profit = max(profit, price - min)

    return profit
prices=[3,1,5,2,7]
res=Sales(prices)
print(res)