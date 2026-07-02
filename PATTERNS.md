# DSA Patterns

## Arrays & Hashing

### 242. Valid Anagram
Given: two strings s and t

Goal: return `True` if they are anagrams, otherwise `False`

Pattern: hash map frequency count

Approach: 
- If lengths differ, return `False`
- Use hash map where **key** is the character and the **value** is the character count
- Count characters in s
- Loop through `t` and subtract from those counts
- If `t` needs a character with count `0`, return `False` meaning that character is unavailable
  so the two are not anagrams
- If the loop finishes, return `True`
  
Time: O(n) since we have to loop through each string once

Space: O(n) worst case we have to store each character form string s in hash map

Mistakes to avoid:
- Remember that `dict.get(char, 0)` handles characters that are not already in the hash map and
  stores the default value to `0`



### 217. Contains Duplicate
Given: array of numbers `nums`

Goal: return `True` if duplicates, else return `False`

Pattern: hash set since it stores unique values

Approach: 
- Use set() on given array since it will remove any duplicates
- Compare the length of the set to length of `nums`
- If lengths differ, return `True` else return `False`

Time: O(n), creating set requires scanning nums

Space: O(n), worst casea all values are unique and stored in set

Key idea:
- `set(nums)` removes any duplicates



### 1. Two Sum
Given: array of integers `nums` and an integer `target`

Goal: return indices of the two integers that add up to `target`

Pattern: hash map lookup

Map: `num -> index`

Approach:
- Loop through `nums` with `enumerate` so we have both index and value
- For each num, calculate `complement = target - num`
- If `complement` is already in hash map, return its stored index and current index
- Otherwise store current `num -> current index`

Time: O(n), loop through the array once

Space: O(n), worst case we store up to every number in the hash map

Key idea:
'num + complement = target`

Mistake to avoid:
- Check for the complement before storing current number so we dont store the same index twice

  

## Two Pointers
### 125. Valid Palindrome
Given: a string `s`

Goal: return `True` if `s` is a palindrome after ignoring non-alphanumeric characters and case

Approach:
- Set left pointer at start and right pointer at end
- While `left < right`, skip non-alphanumeric characters using `.isalnum()` method
- Compare lowercase versions of both characters using `.lower()` method
- If they differ, return `False`
- If they match, move both pointers inward i.e. increment the left and decrement the right

Time: O(n), each pointer moves through string at most once

Space: O(1), only using a fixed number of extra variables

Key idea: Compare valid characters from both ends of string moving inward

Mistake to avoid:
Use `continue` after skipping a non-alphanumeric character so the loop restarts and re-checks the new pointer position before comparing. Why? because say we have two non-alphanumeric characters back-to-back, without `continue` we will move say the left pointer inward from one bad character to another not checking the next bad character so we will end up comparing a bad character to a possible good character at the right pointer.



## Sliding Window
### 121. Best Time to Buy and Sell Stock

