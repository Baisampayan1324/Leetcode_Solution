# 🧾 Code:
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_map = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            if s[right] in char_map:
                left = max(left, char_map[s[right]] + 1)
            
            char_map[s[right]] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length


"""
Problem: Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

---

Why this matters:
This is one of the most popular string-based interview questions. It teaches you how to:
- Handle dynamic windows of data
- Use hash maps for fast lookup
- Avoid brute-force and optimize using the sliding window technique

---

🧠 Intuition:
We want to keep checking parts of the string (substrings) that have all **unique** characters.
As soon as we find a repeat, we should move the start of our window forward to exclude the repeating character.
By keeping track of characters and their last seen positions using a map, we can slide the window efficiently.

---

🚶‍♂️ Approach:
1. Use a dictionary `char_map` to store the last seen index of each character.
2. Use two pointers:
   - `left` marks the start of our current substring window.
   - `right` moves through each character.
3. If a character is already in `char_map` and its last seen index is within our current window:
   - Move `left` forward to one position after that index.
4. Update the character's latest index in `char_map`.
5. Calculate the current window length as `right - left + 1`, and update `max_length` accordingly.
6. Return `max_length` after processing the whole string.

---

⏱️ Complexity:
- Time: O(n)
  Each character is processed at most twice (once by `right`, once by `left`).
- Space: O(k)
  Where `k` is the number of unique characters in the input string (e.g. 128 for ASCII).

---
"""
