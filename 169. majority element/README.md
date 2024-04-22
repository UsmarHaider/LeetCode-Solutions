# Intuition
To find the majority element in an array, which is the element that appears more than ⌊n / 2⌋ times, we can use a counting approach. We'll count the occurrences of each element in the array and then find the element with the highest count.

# Approach
1. Initialize an empty dictionary `counts` to store the counts of each element.
2. Iterate through the given `nums` array. For each element `i`, check if it exists in the `counts` dictionary.
   - If it does, increment its count.
   - If it doesn't, add it to the dictionary with a count of `1`.
3. Initialize variables `max_count` and `maj_element` to keep track of the maximum count and the majority element, respectively.
4. Iterate through the key-value pairs in the `counts` dictionary.
   - For each pair, if the count is greater than `max_count`, update `max_count` and `maj_element` accordingly.
5. Return `maj_element`, which is the majority element in the array.

# Complexity
- Time complexity: $$O(n)$$, where \(n\) is the number of elements in the input array. We iterate through the array once to count the occurrences of each element.
- Space complexity: $$O(n)$$, where \(n\) is the number of elements in the input array. We use a dictionary to store the counts of each element, which could potentially store all elements in the worst case.

# Code
```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        max_count = 0
        maj_element = None

        for num, count in counts.items():
            if count > max_count:
                max_count = count
                maj_element = num

        return maj_element
```