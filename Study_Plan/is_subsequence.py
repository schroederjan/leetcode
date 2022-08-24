""" """


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        print(list(s))
        print(list(t))

        if s in list(t):
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()

    s = "abc"
    t = "ahbgdc"

    print(solution.isSubsequence(s, t))
