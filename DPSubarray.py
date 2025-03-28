import time
import random

# Get user input for number of days
num_days = int(input("Enter the number of days to simulate: "))

startTime = time.perf_counter()

def max_subarray_sum(arr):
    """
    Calculate the maximum subarray sum using dynamic programming.
    """
    if not arr:
        return 0
    
    # Initialize the dynamic programming table
    dp = [0] * len(arr)
    dp[0] = arr[0]

    # Calculate the maximum subarray sum ending at each position
    for i in range(1, len(arr)):
        dp[i] = max(arr[i], dp[i - 1] + arr[i])

    # Calculate the maximum subarray sum
    max_sum = max(dp)

    return max_sum

# Create a list for daily prices
days = [random.randint(100, 150) for _ in range(num_days)]

# Create a list for price changes
priceChange = [0] * num_days
for i in range(1, num_days):
    priceChange[i] = days[i] - days[i - 1]

print("Daily prices:", days)
print("Price changes:", priceChange)
max_sum = max_subarray_sum(priceChange)
print("Maximum subarray sum:", max_sum)

endTime = time.perf_counter()
print("Execution time: ", (endTime - startTime) * 1000, "ms")
