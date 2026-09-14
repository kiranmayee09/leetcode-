class Solution:
    def hasSameDigits(self, s: str) -> bool:
        """ while len(s) > 2:
            new_s = ""

            for i in range(len(s) - 1):
                digit = (int(s[i]) + int(s[i+1])) % 10
                new_s += str(digit)

            s = new_s

        return s[0] == s[1] """

        while len(s) > 2:
            new_s = ""

            for i in range(len(s) - 1):
                x = int(s[i])
                y = int(s[i + 1])

                new_s += str((x + y) % 10)

            s = new_s

        return s[0] == s[1]
