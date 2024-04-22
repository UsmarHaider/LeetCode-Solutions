# Intuition
To convert a Roman numeral to an integer, we iterate through the string. For each character, we look up its corresponding integer value in a dictionary. If the current character's value is less than the value of the next character, we subtract the current value from the total. Otherwise, we add the current value to the total.

# Approach
We use a dictionary `roman_value` to map each Roman numeral character to its corresponding integer value. Then, we iterate through the string `s`. For each character, we calculate its value and determine whether to add or subtract it from the total based on the value of the next character.

# Complexity
- Time complexity: $$O(n)$$, where $$n$$ is the length of the input string `s`.
- Space complexity: $$O(1)$$, since the dictionary `roman_value` and the variables `count` and `value` occupy constant space.

# Code
```python
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        count = 0

        for i in range(len(s)):
            value = roman_value[s[i]]

            if i < len(s) - 1 and roman_value[s[i + 1]] > value:
                count -= value
            else:
                count += value

        return count
```