intercept, slope_cost, slope_profit = map(int, input().split())

if slope_cost >= slope_profit:
    print("-1")
else:
    print(intercept // (slope_profit - slope_cost) + 1)


