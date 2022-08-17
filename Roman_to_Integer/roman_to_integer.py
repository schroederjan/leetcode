
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

        # eg. IV = 4 != 6
        def _small_before_big(s) -> int:
            int(s)
            pass

            # only single character input
        if s in self.roman_symbols_dict.keys():
            return _get_base_int(s)

        # multi character input
        elif len(s) > 1:
            string_list = list(s)
            int_list = []
            for string in string_list:
                int_list.append(_get_base_int(string))

            if 
            return sum(int_list)

        else:
            raise NotImplementedError


if __name__ == '__main__':

    solution = Solution()

    test_dict = {
        'I': 1,
        'II': 2,
        'III': 3,
        'IV': 4,
        'V': 5,
        'VI': 6,
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
