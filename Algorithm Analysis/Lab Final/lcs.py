# Input
X = input("Enter first string: ")
Y = input("Enter second string: ")

m = len(X)
n = len(Y)

# DP table
dp = [[0]*(n+1) for _ in range(m+1)] # Create a (m+1) x (n+1) table initialized with 0s

# Fill DP table
for i in range(1, m+1):
    for j in range(1, n+1):
        if X[i-1] == Y[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print("Length of LCS:", dp[m][n])

# Optional: print actual LCS
i, j = m, n         # start from bottom-right corner of the DP table
lcs = []             

while i > 0 and j > 0:      # until we reach the top-left corner
    if X[i-1] == Y[j-1]:    # If characters match, they are part of LCS
        lcs.append(X[i-1]) 
        i -= 1               # Diagonally move up-left
        j -= 1               # Diagonally move up-left
    elif dp[i-1][j] > dp[i][j-1]:  # If the value above is greater than the value to the left, move up
        i -= 1               # Move up
    else:
        j -= 1               # Move left
print("LCS string:", "".join(reversed(lcs)))