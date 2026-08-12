class Solution:

    def encode(self, strs: List[str]) -> str:
        # given: a list of strings
        # goal: encode the list to one list and return it
        # pattern: string manipulation?
        # approach: use a delimiter like "&" and the number of characters per string to separate each string in encoded string
        # time: O(n)
        # space: O(n)
        
        encoded_str = ""

        for s in strs:
            encoded_str += str(len(s)) + "&" + s
        return encoded_str 

    def decode(self, s: str) -> List[str]:
        # given: an encoded str
        # goal: return a list of decoded strings
        # pattern: two pointers
        # approach: use two pointers, one of them is used to find the delimiter specifically

        decoded_strs = []

        l = 0

        while l < len(s):
            j = l

            while s[j] != "&":
                j += 1
            
            length = int(s[l:j])
            l = j + 1
            string = ""

            while length > 0:
                string += s[l]
                l += 1
                length -= 1
            
            decoded_strs.append(string)
        return decoded_strs









