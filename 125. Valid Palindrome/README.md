# Intuition
To solve this problem, we want to determine if a given string is a palindrome after converting it to lowercase and removing all non-alphanumeric characters. Our intuition here is to create a cleaned version of the string that only contains alphanumeric characters, then check if this cleaned string reads the same forwards and backwards.

# Approach
We'll approach this problem by first converting the input string to lowercase to ensure case insensitivity. Then, we'll remove all non-alphanumeric characters from the string. After obtaining the cleaned string, we'll compare it with its reverse to check if it's a palindrome.

# Complexity
- Time complexity: 
  - Converting the string to lowercase takes linear time in the size of the string, so it's O(n), where n is the length of the input string.
  - Removing non-alphanumeric characters also takes linear time, as we iterate through each character once, resulting in O(n) time complexity.
  - Reversing the string and comparing it also takes linear time, O(n).
  - Thus, the overall time complexity is O(n).
  
- Space complexity: 
  - We create a new string to store the cleaned version of the input string, which takes up additional space proportional to the size of the input string. So, the space complexity is O(n).

# Code
```python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Convert the string to lowercase
        s = s.lower()
        
        # Remove non-alphanumeric characters
        alphanumeric_s = ''.join(char for char in s if char.isalnum())
        
        # Check if the alphanumeric string is a palindrome
        return alphanumeric_s == alphanumeric_s[::-1]
```