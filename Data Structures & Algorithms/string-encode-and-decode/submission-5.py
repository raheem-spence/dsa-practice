class Solution:

    def encode(self, strs: List[str]) -> str:
        # given: a list of strings
        # goal: design an algorithm to encode the list to a single string
        # pattern: ??
        # cue: ??
        # approach: can use a delimiter like "#" and right before it place the number of characters in the string so you know how many characters after the delimiter is in the string
        # time: O(n)
        # space: O(n)?

        encoded_str = ""

        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        # given: an encoded string
        # goal: return the decoded list of strings
        # pattern: ??
        # cue: ??
        # approach: use two pointers to loop through the string. one pointer to find the delimiter and once found the distance between the two pointers should give the length of the string to count
        # time: O(n)
        # space: ??

        decoded_strs = []
        l = 0

        while l < len(s):
            j = l

            while s[j] != "#":
                j += 1
            
            length = int(s[l:j])
            string = ""

            l = j + 1
            
            while length > 0:
                string += s[l]
                length -= 1
                l += 1
            
            decoded_strs.append(string)
        
        return decoded_strs











