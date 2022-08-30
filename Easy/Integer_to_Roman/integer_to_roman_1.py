class Solution():
    def __init__(self,):
        self.roman_symbols_dict = {
            1000: 'M',  900: 'CM',
            500: 'D', 400: 'CD',
            100: 'C', 90: 'XC',
            50: 'L', 40: 'XL',
            10: 'X', 9: 'IX',
            5: 'V', 4: 'IV', 1: 'I',
        }

    def intToRoman(self, num: int) -> str:
        """
        run through each entry in test_dict
        check if num is dividable by current key in dict
        if it is it returns a 1 and adds the current val to a string
        then the mathed key is substractred from the current num
        the same continues until gone through the whole dict
        """
        res = ""
        for key, val in self.roman_symbols_dict.items():
            res += val * (num // key)
            num -= key * (num // key)
        print(res)
        return res


if __name__ == '__main__':

    sol = Solution()
    sol.intToRoman(199)
