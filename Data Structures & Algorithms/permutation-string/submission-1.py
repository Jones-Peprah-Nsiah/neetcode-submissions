class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count_s1 = {}
        window_s2 = {}

        for i in range(len(s1)):
            count_s1[s1[i]] = count_s1.get(s1[i], 0) + 1
            window_s2[s2[i]] = window_s2.get(s2[i], 0) + 1

        if count_s1 == window_s2:
            return True

        l = 0

        for r in range(len(s1), len(s2)):
            window_s2[s2[r]] = window_s2.get(s2[r], 0) + 1

            window_s2[s2[l]] -= 1
            if window_s2[s2[l]] == 0:
                del window_s2[s2[l]]

            l += 1

            if window_s2 == count_s1:
                return True

        return False