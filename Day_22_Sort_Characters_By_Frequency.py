class Solution:
    def frequencySort(self, s: str) -> str:
        words = collections.Counter(s)
       # print (words)
        
        ans=[]
        for l in sorted(words.keys(),key=words.get,reverse=True):
            ans.append((words[l])*l)
       #     print (ans)
        return "".join(ans)
