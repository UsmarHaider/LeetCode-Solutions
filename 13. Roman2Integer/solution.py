class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_value = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000 }

        count=0

        for i in range(len(s)):
            value = roman_value[s[i]]

            if i<len(s)-1 and roman_value[s[i+1]]>value:
                count-=value
            else:
                count+=value

        return count


        