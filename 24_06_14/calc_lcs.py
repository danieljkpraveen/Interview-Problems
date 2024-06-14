"""
Program to calculate the Longest Common Subsequence (LCS) b/w
2 strings

Ex:
s1 = "abcdef"
s2 = "ace"
Output = 3
"""

def calc_lcs(inp_s1: str, inp_s2: str) -> int:
    m: int = len(s1)
    n: int = len(s2)
    dp = [
        [0 for _ in range(n+1)] for _ in range(m+1)
    ]
    ##
    for i in range(1, m+1):
        for j in range(1, n+1):
            if inp_s1[i-1] == inp_s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]


if __name__ == '__main__':
    s1: str = "abcdef"
    s2: str = "ace"
    ##
    result: int = calc_lcs(inp_s1=s1, inp_s2=s2)
    print(f"Longest common subsequence between {s1} and {s2} is {result}")
