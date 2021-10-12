#给你一个字符串 s，找到 s 中最长的回文子串。
#示例 1：
#输入：s = "babad"
#输出："bab"
#解释："aba" 同样是符合题意的答案。
#示例 2：
#输入：s = "cbbd"
#输出："bb"
#示例 3：
#输入：s = "a"
#输出："a"
#示例 4：
#输入：s = "ac"
#输出："a"
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        max_len = 1
        begin = 0
        dp = [ [False] * n for _ in range(n) ]
        for i in range(n):
            dp[i][i] = True
        
        for k in range(2, n + 1):
            for i in range(n):
                j = k + i - 1
                if j >= n:
                    break
   
                if s[i] != s[j]:
                    dp[i][j] = False 
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]
