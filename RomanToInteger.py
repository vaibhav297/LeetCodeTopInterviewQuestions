class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
        "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        total_sum = 0

        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in ["IV", "IX", "XL", "XC", "CD", "CM"]:
                total_sum += romanDict[s[i:i+2]]
                i += 2
            else:
                total_sum += romanDict[s[i]]
                i += 1

        return total_sum
