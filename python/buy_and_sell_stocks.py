def max_profit(prices):

    # Assume we buy on the first day itself
    buy_price = prices[0]
    # Initialize max profit to zero
    max_profit = 0

    # Loop through the list of prices starting from the second day
    for i in range(1, len(prices)):
        # If the current price is less than the buy price, update buy price
        if prices[i] < buy_price:
            # Update buy price to the current price
            buy_price = prices[i]
        else:
            # Calculate potential profit if we sell on the current day
            profit = prices[i] - buy_price
            # Update max profit if the calculated profit is greater than the current max profit is found
            if profit > max_profit:
                max_profit = profit
    
    return max_profit

# Example usage
prices = [7,1,5,3,6,4]
result = max_profit(prices)
print(result)