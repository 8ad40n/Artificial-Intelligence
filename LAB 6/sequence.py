def find_lcs(P, Q):
    m, n = len(P), len(Q)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if P[i - 1] == Q[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if P[i - 1] == Q[j - 1]:
            lcs.insert(0, P[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(lcs)


P = "AGTCTTCCAGCGAT"
Q = "GACATCGATAATGC"
common_sequence = find_lcs(P, Q)
print("Common Sequence:", common_sequence)
