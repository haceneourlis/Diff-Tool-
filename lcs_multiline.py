from lcs import lcs

def lcs_multiline(X, Y):
    m = len(X)
    n = len(Y)
    
    # Step 1: Create a 2D DP table to store lengths of longest common subsequence.
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Step 2: Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Step 3: Backtrack to find the LCS string
    lcs_list = []  # Create a list to store the LCS strings
    
    # Start from the bottom-right corner and backtrack
    i, j = m, n
    while i > 0 and j > 0:
        # If current strings in X and Y are the same, they are part of LCS
        if X[i - 1] == Y[j - 1]:
            lcs_list.insert(0, X[i - 1])  # Insert at the beginning of the list
            i -= 1
            j -= 1
        # If not, move in the direction of the larger value
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return lcs_list
