class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1 = {}
        for char in s1:
            map1[char] = map1.get(char, 0) + 1

        l = 0
        r = 0
        map2 = {}

        for r, char in enumerate(s2):
            map2[char] = map2.get(char, 0) + 1
            while map2.get(char, 0) > map1.get(char, 0) and l < len(s2)-1:
                map2[s2[l]] = map2.get(s2[l], 0)-1
                if map2.get(s2[l]) == 0:
                    map2.pop(s2[l])
                l = l+1

            if map1 == map2:
                return True

        return False


        