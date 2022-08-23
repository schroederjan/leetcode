from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        leftsum = 0
        for i, num in enumerate(nums):
            if leftsum == (S - leftsum - num):
                return i
            leftsum += num
        return -1


if __name__ == '__main__':
    sol = Solution()

    nums = [1, 7, 3, 6, 5, 6]
    print(sol.pivotIndex(nums))

    nums = [1, 2, 3]
    print(sol.pivotIndex(nums))

    nums = [2, 1, -1]
    print(sol.pivotIndex(nums))
