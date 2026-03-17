prices = [29.99, 45.50, 12.75, 38.20]

for a in range(len(prices)):
    if a == 0:
        prices[0] = prices[0]*0.9
        print(f'Updated price for item {1}: ${prices[0]:.2f}')

    elif a == 1:
        prices[1] = prices[1]*0.8
        print(f'Updated price for item {2}: ${prices[1]:.2f}')

    elif a == 2:
        prices[2] = prices[2]*0.85
        print(f'Updated price for item {3}: ${prices[2]:.2f}')

    elif a == 3:
        prices[3] = prices[3]*0.95
        print(f'Updated price for item {4}: ${prices[3]:.2f}')







