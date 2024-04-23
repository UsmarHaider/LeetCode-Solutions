# Intuition
To find the length of the last word in a string, we split the string by whitespace and return the length of the last element.

# Approach
We use the `split()` method to split the string `s` into a list of words based on whitespace. Then, we access the last element of the list using index `-1` and return its length.

# Complexity
- Time complexity: $$O(n)$$, where $$n$$ is the length of the input string `s`. The `split()` method takes linear time to split the string.
- Space complexity: $$O(n)$$, where $$n$$ is the length of the input string `s`. This is the space required to store the list of words after splitting the string.

# Code
```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        last_word = s.split()[-1]
        return len(last_word)
```