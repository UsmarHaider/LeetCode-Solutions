class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp=[]
        temp.append(nums[0])
        i=1
        while i<len(nums):
            if nums[i]!=nums[i-1]:
                temp.append(nums[i])
                i=i+1
            else:
                i=i+1

        for i in range(len(temp)):
            nums[i]=temp[i]

        return len(temp)