class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict_count = {}

        
        for i in range(len(strs)):
            letter_count = [0] * 26
            for j in range(len(strs[i])):
                letter_index = ord(strs[i][j]) - ord('a')
                letter_count[letter_index] += 1

            letter_count = tuple(letter_count)
            
            if letter_count in dict_count:
                dict_count[letter_count].append(strs[i])
            else:
                dict_count[letter_count] = [strs[i]]
            

        anagrams_list = []

        for k, v in dict_count.items():
            anagrams_list.append(v)
        
        return anagrams_list



