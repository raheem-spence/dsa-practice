class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # given: two strings s and t
        # goal: return true if anagrams, else false
        # pattern: hashmap
        # approach: create two separate hashmaps char -> frequency, then compare the hashmaps
        # time: O(n)
        # space O()

        count_t = Counter(t)
        count_s = Counter(s)

        return count_t == count_s