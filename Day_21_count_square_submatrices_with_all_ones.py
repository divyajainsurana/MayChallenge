class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        s_num=0
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        print (dp)
        result =0
        
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if i==0  or j==0:
                    dp[i][j]=matrix[i][j]
                elif matrix[i][j]==1:
                    dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
                result +=dp[i][j]
        return result
