import pysnooper

class Solution:
    
    @pysnooper.snoop()
    def numDistinct(self, s: str, t: str) -> int:
        '''
        举例
        输入: S = "babgbag", T = "bag"
        输出: 5

        这道题不是求两个字符串是匹配，而是判断S有多少种方式可以得到T。
        但其实还是动态规划，我们一个定义二维数组dp，dp[i][j]为字符串s(0,i)变换到t(0,j)的变换方法的个数。

        如果S[i]==T[j]，那么dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        意思是：如果当前S[i]==T[j]，那么当前这个字符即可以保留也可以抛弃，所以变换方法等于保留这个字符的变换方法加上不用这个字符的变换方法， 
            dp[i-1][j-1]为保留这个字符时的变换方法个数，dp[i-1][j]表示抛弃这个字符时的变换方法个数。

        如果S[i]!=T[i]，那么dp[i][j] = dp[i-1][j]，意思是如果当前字符不等，那么就只能抛弃当前这个字符。
        '''

        s_len = len(s)
        t_len = len(t)

        if s_len < t_len or s_len < 1 or t_len < 1:
            return 0

        check_len = t_len

        s_array = [sc for sc in s]
        t_array = [tc for tc in t]

        return 5