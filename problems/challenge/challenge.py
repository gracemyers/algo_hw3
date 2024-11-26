'''
Challenge 1
'''

def find_max_form(strs, m, n): 
    # Initialize a DP table with dimensions (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for s in strs:
        # count num of 0s and 1s 
        zeros = s.count('0')
        ones = s.count('1')

        # Update the DP table
        for i in range(m, zeros - 1, -1):  # Start from m 
            for j in range(n, ones - 1, -1):  # Start from n 
                dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

    return dp[m][n]

