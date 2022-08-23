from typing import List


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_t_dict = {}
        t_s_dict = {}

        for c1, c2 in zip(s, t):

            print(c1)
            print(c2)

            # only write each character only once
            if c1 not in s_t_dict and c2 not in t_s_dict:
                s_t_dict[c1] = c2
                t_s_dict[c2] = c1

                print(s_t_dict)
                print(t_s_dict)

            #
            elif s_t_dict[c1] != c2 or t_s_dict[c2] != c1:

                print(s_t_dict)
                print(t_s_dict)

                return False

        return True

        # return False


if __name__ == '__main__':
    sol = Solution()

    #  s = "egg"
    #  t = "add"

    s = "foo"
    t = "bar"

    print(sol.isIsomorphic(s, t))
