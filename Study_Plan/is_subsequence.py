""" Solution for Problem """


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_iter = iter(t)
        # loop through letters and check against each letter in t
        for letter in s:
            if letter not in t_iter:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()

    s = "abc"
    t = "ahbgdc"

    print(solution.isSubsequence(s, t))

    s = "x"
    t = "ahbgdc"

    print(solution.isSubsequence(s, t))
