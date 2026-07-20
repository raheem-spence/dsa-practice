class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # given: array of strings strs
        # goal: return all anagrams together in sublists where an anagram is a string 
        # that contains the exact same characters as another string, 
        # but the order of characters can be different
        # pattern: arrays & hashing
        # approach: Use a hash map where the key is the anagram signature of character
        # frequency count represented as a list. Strings with the same signature
        # are grouped together in the same list.
        # time: O(m * n), where m is the average or maximum length of a string and n is the number of strs
        # space: O(1)

        count_map = {}

        for s in strs:
            signature = 26 * [0]

            for c in s:
                position = ord(c) - ord('a')
                signature[position] += 1

            signature_key = tuple(signature)

            if signature_key in count_map:
                anagrams = count_map.get(signature_key)
                anagrams.append(s)
            else:
                count_map[signature_key] = [s]


        return list(count_map.values())



        