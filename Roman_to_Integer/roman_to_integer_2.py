
class Solution():
    def __init__(self,):
        self.roman_symbols_dict = {
            'I': 1,
            'V': 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

    def romanToInt(self, s: str) -> int:
        # large before smaller +
        # smaller before larger -
        result = 0
        for i in range(len(s)):
            if i+1 < len(s) and self.roman_symbols_dict[s[i]] < self.roman_symbols_dict[s[i+1]]:
                result -= self.roman_symbols_dict[s[i]]
            else:
                result += self.roman_symbols_dict[s[i]]
        return result


if __name__ == '__main__':

    solution = Solution()

    test_dict = {
        'IV': 4,
        'VI': 6,
        'XI': 11,
        'IX': 9,
        'XL': 40,
        'LX': 60,
        'XC': 90,
        'CX': 110,
        'CM': 900,
        'MC': 1100,
        'LVIII': 58,
        'MCMXCIV': 1994,
    }

    def _check_solution(solution, should):
        if solution == should:
            result = True
        else:
            result = False
        return result

    # for index, s in enumerate(test_list):
    for index, s in enumerate(test_dict.keys()):
        try:
            print("\n")
            print(f"case: {index}")
            print(f"input: {s}")
            result = solution.romanToInt(s)
            print(f"solution: {result}")
            print(f"should: {test_dict[s]}")
            print(f"check: {_check_solution(result, test_dict[s])}")

        except NotImplementedError:
            print("solution: NOT IMPLEMENTED")
