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
Given: array of prices where `prices[i]` is the stock price day `i`

Goal: return the maximum profit from buying once and selling once later

Pattern: sliding window / one-pass tracking

Approach: 
- Use two pointers: `left` for the best buy day so far and `right` for the current sell day
- If `prices[right] < prices[left]`, move `left` to `right` becasue we found a cheaper buy day
- Calculate profit with `prices[right] - prices[left]
- Keep updating the max profit as `right` moves through the array using `max()` function

Time: O(n), because `right` scans through the array once

Space: O(1), because we only use pointers and a max profit variable

## Stack
### 20. Valid Parentheses
Given: a string `s` containing only `(`, `)`, `{`, `}`, `[` and `[`

Goal: return `True` if every opening bracket is closed by the same type in the correct order

Pattern: Stack, LIFO (last in, first out)

Map: `closing bracket -> matching opening bracket`

Approach:
- Push opening brackets onto the stack
- When a closing bracket appears, check if the stack is empty, if so return `False`
- If top of stack does not match the expected opening bracket, return `False`
- Othersise pop the stack
- At the end, return `True` only if the stack is empty

Time: O(n), one pass through the string

Space: O(n), worst case the stack could hold every character in the string

## Binary Search
### 704. Binary Search
Given: sorted array `nums` and an integer `target`

Goal: return index of `target`, or `-1` if it is not found

Pattern: binary search

Approach: 
- Set `left` at the start of the array and `right` at the end
- While `left <= right`, calculate middle index
- If `nums[mid] == target`, return `mid`
- If `nums[mid] > target`, search the left half by moving `right`
- If `nums[mid] < target`, search the right half by moving `left`
- If loop ends, return `-1`

Time: O(log n), because the search space is cut in half each loop

Space: O(1), because we only use pointers/variables

Key idea: 
Each step cuts the search space in half

Middle formula:
`mid = left + (right - left) // 2`

Mistake to avoid:
- Use `left <= right` so you still check the final remaining element
- Calculate mid inside the loop using the current `left` and `right`
- Remember `mid = left + (right - left) // 2`, not just `(right - left) // 2`
