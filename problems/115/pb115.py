import pysnooper

class Solution:
    
    @pysnooper.snoop()
    def numDistinct(self, s: str, t: str) -> int:
        '''
        举例
        输入: S = "ababgbag", T = "bag"
        输出: 5

        这道题不是求两个字符串是匹配，而是判断S有多少种方式可以得到T。
        但其实还是动态规划，我们一个定义二维数组dp，dp[i][j]为字符串s(0,i)变换到t(0,j)的变换方法的个数。

        画出表格，推导: 
        从一个字符的子序列开始推导

        动态转换逻辑
        if s[i] == t[j], dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1],
        这是因为：
        再拼接一个新的字符满足子串相同，可有的case有 dp[i - 1][j - 1] 个； 
        不拼接一个新的字符满足子串相同，可用的case有 dp[i][j - 1] 个
        '''

        s_len = len(s)
        t_len = len(t)

        if s_len < t_len or s_len < 1 or t_len < 1:
            return 0

        s_array = [sc for sc in s]
        t_array = [tc for tc in t]

        dp = [[0 for sc in s_array] for tc in t_array]
        
        for row_index in range(t_len):
            for col_index in range(s_len):
                if s_array[col_index] == t_array[row_index]:
                    if row_index > 0:
                        if col_index > 0:
                             dp[row_index][col_index] =  dp[row_index - 1][col_index - 1] +  dp[row_index][col_index - 1]      
                    else:
                        dp[row_index][col_index] = dp[row_index][col_index - 1] + 1
                else:
                    if col_index > 0:
                        dp[row_index][col_index] = dp[row_index][col_index - 1]

        return dp[-1][-1]