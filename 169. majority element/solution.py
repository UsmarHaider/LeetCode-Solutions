class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts={}
        for i in nums:
            if i in counts:
                counts[i]+=1
            else:
                counts[i]=1
        
        max_count=0
        maj_element=None

        for num , count in counts.items():
            if count>max_count:
                max_count=count
                maj_element=num

        return maj_element

        return max

        
        
