class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Approach: Use a hash map where the keys are anagram signatures and values
        # are the anagrams themselves

        # To get the signatures, we can map the character count to an index in
        # an array of size 26 

        # Time: O(n * m), where n is the number of strings and m is the
        # length of longest string

        # Space: O(m), m is the number of strings meaning the number of keys we
        # could have. Worst case, every string is not an anagram of another

        anagrams = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            count = tuple(count)
            
            if count not in anagrams:
                anagrams[count] = [s]
            else:
                anagrams[count].append(s)
        return list(anagrams.values())

