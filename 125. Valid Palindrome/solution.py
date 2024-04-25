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
