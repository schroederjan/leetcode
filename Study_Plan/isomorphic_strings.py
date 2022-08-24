from typing import List


# first approach
class Solution_1:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_t_dict = {}
        t_s_dict = {}

        for c1, c2 in zip(s, t):
            # only write each character only once
            if c1 not in s_t_dict and c2 not in t_s_dict:
                s_t_dict[c1] = c2
                t_s_dict[c2] = c1

            # if current char is not in each others list
            elif s_t_dict[c1] != c2 or t_s_dict[c2] != c1:
                return False

        return True


# simplified approach using set
class Solution_2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


# simplified approach using set
class Solution_3:
    def transfromString(self, s: str) -> str:
        index_map = {}
        new_str = []

        for i, c in enumerate(s):
            if c not in index_map:
                index_map[c] = i
            new_str.append(str(index_map[c]))

        return " ".join(new_str)

    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.transfromString(s) == self.transfromString(t)


if __name__ == '__main__':
    sol_1 = Solution_1()
    sol_2 = Solution_2()
    sol_3 = Solution_3()

    #  s = "egg"
    #  t = "add"

    s = "egson"
    t = "adsin"

    #  s = "testing"
    #  t = "barteng"

    print(sol_1.isIsomorphic(s, t))
    print(sol_2.isIsomorphic(s, t))
    print(sol_3.isIsomorphic(s, t))
