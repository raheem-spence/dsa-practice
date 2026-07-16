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
- Remember that `dict.get(char, 0)` handles characters that are not already in the hash map and stores the default value to `0`
- When using `dict.get(char)`, remember it can return `None` if character is missing from map so don't only chck `if count == 0` because that misses the `None` case
- Use `if not count` to catch both:
    - `None` = character does not exist in the map
    - `0` = character exists but has already been used up



### 217. Contains Duplicate
Given: array of numbers `nums`

Goal: return `True` if duplicates, else return `False`

Pattern: hash set since it stores unique values

Approach: 
- Use set() on given array since it will remove any duplicates
- Compare the length of the set to length of `nums`
- If lengths differ, return `True` else return `False`

Time: O(n), creating set requires scanning nums

Space: O(n), worst case all values are unique and stored in set

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



### 387. First Unique Character in a String
Given: a string `s`

Goal: return the index of the first non-repeating character, or `-1` if none exists

Pattern: hash map frequency count + second pass

Map: `char -> count`

Approach: 
- Count each character using hash map
- Loop through the string again with `enumerate` cause we want both index and character
- Return the first index where `char_count[char] == 1`
- If no unique character exists, return `-1`

Time: O(n), we loop through string twice but O(2n) simplifies to O(n)

Space: O(n), worst case we store all unique characters

Key idea:
First pass gets the counts; second pass preserves original order



### 169. Majority Element
Given: array `nums` of size `n`

Goal: return the element that appears more than `n / 2` times

Pattern: hash map frequency count 

Map: `num -> count`

Approach:
- Use a hash map to count each number
- Set threshold as `len(nums) // 2`
- As each count is updated, check if it is greater than the threshold
- Return the number once its count passes the threshold

Time: O(n)

Space: O(n)

Key idea:
The majority element appears more than half the array length

Alternative approach:
Boyer-Moore Voting Algorithm can solve this in O(1) space, but the hash map version is clearer for now


## Arrays & Math
### 268. Missing Number
Given: array `nums` containing `n` distinct numbers from `0` to `n`

Goal: return missing number from the range `0` to `n`

Pattern: arrays / math

Approach: 
- Since the numbers should be from `0` to `n`, calculate the expected sum
- Calculate the actual sum of `nums`
- The missing number is `expected_sum - actual_sum`

Formula:
`expected_sum = n * (n + 1) // 2`

Time: O(n), we loop through `nums` once to find sum

Space: O(1), we only use a few variables

Mistake to avoid:
- The full range is based on `len(nums)`, not the last value in the array because the array is not gauranteed to be sorted



## Arrays / Counting / Combinatorics
### Pattern: Middle-Anchor Counting

Use this pattern when:
- You are counting triplets/subsequences of length 3
- Index order matters: `i < j < k`
- The elements do **not** need to be contiguous
- You can think of each valid answer as:
```text
left element + middle element + right element
```

### Key Concept
For an increasing subsequence of length 3:
```text
nums[left] < nums[middle] < nums[right]
left < middle < right
```

Instead of building every subsequence manually, fix each possible element as the **middle**.

Then count:
```text
left_smaller = number of values before middle that are smaller
right_greater = number of values after middle that are greater
```

For the middle:
```text
valid subsequences = left_smaller * right_greater
```

Why multiply?
Because of the multiplication rule:
```text
Each valid left choice can pair with each valid right choice.
```
Since the middle is already fixed, every combination forms:
```text
one left choice + fixed middle + one right choice
```
So the subsequence is automatically length 3

### Mistake to Avoid
Do **not** treat this like a sliding window.
```text
Subarray = contiguous
Subsequence = order preserved, but can skip elements
```

Example:
```python
nums = [2, 1, 3, 4, 5]

[2, 3, 5] is a subsequence
It skips 1 and 4, but the order is preserved
```

### Solution
```python
def countIncreasingSubsequences(nums):
    MOD = 10**9 + 7
    subsequences = 0

    for i in range(1, len(nums) - 1):
        small_count = 0
        big_count = 0

        for j in range(i):
            if nums[j] < nums[i]:
                small_count += 1

        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                big_count += 1

        subsequences += small_count * big_count
        subsequences %= MOD

    return subsequences
```
## Complexity
Time: O(n<sup>2</sup>), nested for loops

Space: O(1)

## Core Mental Model
```text
For each possible middle:
  count valid left choices
  count valid right choices
  multiply them
  add to answer
```

### 1395. Count Number of Teams
Given: integer array `rating` where `rating[i]` represents the rating of the `ith` soldier

Goal: return the number of teams of 3 soldiers `(i, j, k)` such that:
- `i < j < k`
- `rating[i] < rating[j] < rating[k]`
- or `rating[i] > rating[j] > rating[k]`

Pattern: Middle-Anchor Counting

Approach:
- Loop through every possible middle soldier
- Count
    - `left_smaller`
    - `left_bigger`
    - `right_smaller`
    - `right_bigger`
- Compute
    - `increasing_teams = left_smaller * right_bigger`
    - `decreasing_teams = left_bigger * right_smaller`
- Add both values to the total number of teams

Time: O(n<sup>2</sup>), nested for loops

Space: O(1)

Key Idea
- Fix each soldier as the `middle` soldier
- Count the valid left soldiers and the valid right soldiers
- Every valid left soldier can pair with every valid right soldier, so the total number of teams using the current middle soldier is the product of the two counts.
- This is an application of the `Multiplication Rule (Rule of Product)` in combinatorics

Mistakes to avoid
- Do not generate every possible triplet
- Do not use a sliding window (the soldiers do `not` have to be contiguous)
- Remember to count `both`
    - increasing teams
    - decreasing teams
- If the ratings are guaranteed to be uniqe, using `else` works. If duplicates allowed, use explicit comparisions

Related Problems:
- Increasing Subsequences (Middle Anchor)
- Decreasing Subsequences (Middle Anchor)
- Mountain Triplets (Middle Anchor)

### 3583. Count Special Triplets
Given: an integer array `nums`

Goal: return the total number of special triplets such that
- `0 <= i < j < k < n, where n = nums.length`
- `nums[i] == nums[j] * 2`
- `nums[k] == nums[j] * 2`

Pattern: Middle-Anchor Frequency Counting

Approach: Maintain two hash maps: one for the total count of each number and one for the seen count of each number as we iterate through the array. On each iteration we calculate the `target = n * 2` where `n` is the current number were on and the potential middle of a valid special triplet. Then we find the counts of the target that is left of the current number by accessing the seen count map. Next we add the current number to the seen count, we do it at this point because otherwise we'd count the current number as being on the left when its not on either side at this point. Next, we find the counts for the target on the right side by
taking the difference between the total count for the target and the seen count for the target. We do so by accessing both hash maps where the target is the key. Lastly, we update the total number of special triplets by adding the product of the left choices and right choices to find the total number of special triplets for this particular middle number. Here we are using the `Multiplication Rule` aka `Rule of Rroduct`. Then take the modulo `10<sup>9</sup> + 7` of the special triplets value and return it.

Time: O(n)

Space: O(n), worst case every number is unique, so both hash maps store `n` keys

Related Problems:
- Count Number of Bad Pairs
- Number of Good pairs
- Count Nice Pairs in an Array
- Count Good Meals


## Two Pointers
### 125. Valid Palindrome
Given: a string `s`

Goal: return `True` if `s` is a palindrome after ignoring non-alphanumeric characters and case

Pattern: two pointers

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

### 283. Move Zeroes
Given: array `nums`

Goal: move all `0`s to the end while keeping the relative order of non-zero elements 

Pattern: two pointers / in-place array

Approach:
- Use `l` to track where the next non-zero element should go
- Use `r` to scan through the array
- When `nums[r]` is non-zero, swap `nums[r]` with `nums[l]`
- Move `l` forward after placing a non-zero
- Always move `r` forward

Time: O(n), `r` scans array once

Space: O(1), we modify the array in place and only use pointers

Key idea:
- `l = next position for a non-zero`
- `r = scanner looking for non-zero values`

Mistake to avoid:
- Avoid using `pop()` from the middle of the array because it shifts elements and can make the solution O(n<sup>2</sup>)

## Sliding Window
### 121. Best Time to Buy and Sell Stock
Given: array of prices where `prices[i]` is the stock price day `i`

Goal: return the maximum profit from buying once and selling once later

Pattern: sliding window / one-pass tracking

Approach: 
- Use two pointers: `left` for the best buy day so far and `right` for the current sell day
- If `prices[right] < prices[left]`, move `left` to `right` becasue we found a cheaper buy day
- Calculate profit with `prices[right] - prices[left]`
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
