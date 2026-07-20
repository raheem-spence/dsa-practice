class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # given: array of strings strs
        # goal: return all anagrams together in sublists where an anagram is a string 
        # that contains the exact same characters as another string, 
        # but the order of characters can be different
        # pattern: arrays & hashing
        # approach: Use a hash map where the key is the anagram signature of character
        # frequency count represented as a list then we check if each string has that exact
        # signature and appended it to a list, else create new list for that string
        # time: O(m * n), where m is the number of characters in the longest string and n is the number of strs
        # space: O(n)

        count_map = {}

        for s in strs:
            signature = 26 * [0]

            for c in s:
                position = ord(c) - ord('a')
                signature[position] += 1

            signature_key = tuple(signature)

            if signature_key in count_map:
                anagrams = count_map.get(signature_key, 0)
                anagrams.append(s)
                count_map[signature_key] = anagrams
            else:
                count_map[signature_key] = [s]


        return list(count_map.values())



        