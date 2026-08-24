def lcs(X, Y):
    m = len(X)
    n = len(Y)

    table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    i = m
    j = n
    result = ""

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            result = X[i - 1] + result
            i -= 1
            j -= 1
        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return result


X = "AGGTAB"
Y = "GXTXAYB"

print("Longest Common Subsequence:", lcs(X, Y))
