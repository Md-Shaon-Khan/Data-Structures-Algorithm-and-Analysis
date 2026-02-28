# Input
n = int(input("Enter length of log: "))
prices = [0] + list(map(int, input("Enter prices for length 1 to n: ").split()))

# DP table
dp = [0]*(n+1) # Create a table to store maximum profit for each length from 0 to n & table size is n+1 because we want to include length n

for i in range(1, n+1):
    max_val = 0
    for j in range(1, i+1):
        max_val = max(max_val, prices[j] + dp[i-j])
    dp[i] = max_val

print("Maximum profit:", dp[n])