
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

        def _get_base_int(s) -> int:
            return self.roman_symbols_dict[s]

        def _solve_cases(int_list):
            counter: int = 0
            last: int = 0
            for n in int_list:
                # case IV = I - V (1-5) = 4
                if n == 5 and last == 1:
                    counter += n - last * 2
                    last = n
                # case IX = I - X (1-10) = 9
                elif n == 10 and last == 1:
                    counter += n - last * 2
                    last = n
                # case XL = X - L (10-50) = 40
                elif n == 50 and last == 10:
                    counter += n - last * 2
                    last = n
                # case XC = X - C (10-100) = 90
                elif n == 100 and last == 10:
                    counter += n - last * 2
                    last = n
                # case CD = C - D (100-500) = 400
                elif n == 500 and last == 100:
                    counter += n - last * 2
                    last = n
                # case CM = C - M (100-1000) = 900
                elif n == 1000 and last == 100:
                    counter += n - last * 2
                    last = n
                # case Normal
                else:
                    counter += n
                    last = n
            return counter

            # only single character input
        if s in self.roman_symbols_dict.keys():
            return _get_base_int(s)

        # multi character input
        elif len(s) > 1:
            string_list = list(s)
            int_list = []
            for string in string_list:
                int_list.append(_get_base_int(string))

            return _solve_cases(int_list)

        else:
            raise NotImplementedError


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
