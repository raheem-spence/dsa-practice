class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # given: an array of strs
        # goal: group all anagrams into sublists and return output
        # pattern: canonical representation + 
        # approach: use a signature for each anagram. the signature will be the key for a hashmap and the value will be a list of anagrams with that signature,

        anagrams = defaultdict(list)

        for s in strs:
            # check for signature else build a new one
            signature = [0] * 26
            for c in s:
                index = ord(c) - ord('a');
                signature[index] += 1
            anagrams[tuple(signature)].append(s)
        
        return list(anagrams.values())
      