from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp = 0
        result = []
        for num in nums:
            temp += num
            result.append(temp)
        return result


if __name__ == '__main__':
    sol = Solution()

    nums = [1, 2, 3, 4]
    print(sol.runningSum(nums))

    nums = [3, 1, 2, 10, 1]
    print(sol.runningSum(nums))
