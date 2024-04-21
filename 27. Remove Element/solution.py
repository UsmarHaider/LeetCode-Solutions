class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        temp = []

        for j in range(len(nums)):
            if nums[j] != val:
                temp.append(nums[j])

        for i in range(len(temp)):
            nums[i] = temp[i]

        return len(temp)