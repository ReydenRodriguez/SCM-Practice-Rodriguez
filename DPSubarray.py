import time
import random

startTime = time.perf_counter()
def max_subarray_sum(arr):
    """
    Calculate the maximum subarray sum using dynamic programming.
    """
    # Initialize the dynamic programming table
    dp = [0] * len(arr)
    dp[0] = arr[0]

    # Calculate the maximum subarray sum ending at each position
    for i in range(1, len(arr)):
        dp[i] = max(arr[i], dp[i - 1] + arr[i])

    # Calculate the maximum subarray sum
    max_sum = max(dp)

    return max_sum


# Example usage
days = [0] * 200 # Create a list of 100 elements

# Generate random values between 50 and 150 for the list to simluate daily prices
for i in range(200):
    days[i] = random.randint(100, 150)

priceChange = [0] * 100 # Create a list of 100 elements for price changes
for i in range(1, 200):
    priceChange[i] = days[i] - days[i - 1]

print("Daily prices:", days)
print("Price changes:", priceChange)
max_sum = max_subarray_sum(priceChange)
print("Maximum subarray sum:", max_sum)
endTime = time.perf_counter()
print("Execution time: ", (endTime - startTime) * 1000, "ms")
