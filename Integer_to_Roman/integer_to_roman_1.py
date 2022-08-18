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

    def intToRoman(self, num: int) -> str:
        return 'NONE'


if __name__ == '__main__':

    solution = Solution()

    test_dict = {
    }

    def _check_solution(solution, should):
        if solution == should:
            result = True
        else:
            result = False
        return result

    # for index, s in enumerate(test_list):
    for index, num in enumerate(test_dict.keys()):
        print("\n")
        print(f"case: {index}")
        print(f"input: {num}")
        result = solution.intToRoman(num)
        print(f"solution: {result}")
        print(f"should: {test_dict[num]}")
        print(f"check: {_check_solution(result, test_dict[num])}")
