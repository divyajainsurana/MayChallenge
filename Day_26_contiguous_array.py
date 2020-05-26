class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff, max_len = 0, 0
        dic = {0:-1}
        for i in range(len(nums)):
            diff = diff + 1 if nums[i] else diff - 1
            if diff not in dic:
                dic[diff] = i
            else:
                max_len = max(max_len, i - dic[diff])
        #    print (dic)
        return max_len
