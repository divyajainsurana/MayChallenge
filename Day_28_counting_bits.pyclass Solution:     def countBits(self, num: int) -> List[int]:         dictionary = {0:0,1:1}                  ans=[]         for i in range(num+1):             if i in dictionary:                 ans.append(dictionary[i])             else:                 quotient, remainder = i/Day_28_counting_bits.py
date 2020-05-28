class Solution:
    def countBits(self, num: int) -> List[int]:
        dictionary = {0:0,1:1}
        
        ans=[]
        for i in range(num+1):
            if i in dictionary:
                ans.append(dictionary[i])
            else:
                quotient, remainder = i//2,i%2
                value = ans[quotient] +ans[remainder]
                ans.append(value)
                
        return ans
