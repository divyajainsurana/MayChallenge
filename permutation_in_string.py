class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        abc='abcdefghijklmnopqrstuvwxyz'
        a=[s1.count(i) for i in abc]        #create hashmap for s1 
        #print (a)
        b=[0]*26                            # array of size 26  
        for i in range(len(s2)):
            if i>=len(s1):
                if a==b:   # check if a and b are same 
                    return True
                b[ord(s2[i-len(s1)])-ord('a')]-=1
                b[ord(s2[i])-ord('a')]+=1
            else:
                b[ord(s2[i])-ord('a')]+=1   # if i < len(s2), amend hashmap b for the characters seen in s2
                
            if b==a:
                return True
        return False
