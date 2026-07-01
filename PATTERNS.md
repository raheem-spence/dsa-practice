# DSA Patterns

## Arrays & Hashing

### 242. Valid Anagram
Given: two strings s and t

Goal: return `True` if they are anagrams, otherwise `False`

Pattern: hash map frequency count

Approach: 
- If lengths differ, return `False`
- Count characters in s and store in hash map character as key and count as value
- Loop through `t` and subtract from those counts
- If `t` needs a character with count `0`, return `False` meaning that character is unavailable
  so the two are not anagrams
- If the loop finishes, return `True`
  
Time: O(n) since we have to loop through each string once
Space: O(n) worst case we have to store each character form string s in hash map

Mistakes to avoid:
- Remember that `dict.get(char, 0)` handles characters that are not already in the hash map and
  stores the default value to `0`

