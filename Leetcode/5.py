# 🧾 Code:
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand_around_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest_palindrome = ""
        for i in range(len(s)):
            # Odd-length palindrome
            palindrome1 = expand_around_center(s, i, i)
            # Even-length palindrome
            palindrome2 = expand_around_center(s, i, i + 1)

            if len(palindrome1) > len(longest_palindrome):
                longest_palindrome = palindrome1
            if len(palindrome2) > len(longest_palindrome):
                longest_palindrome = palindrome2

        return longest_palindrome


"""
Problem: Longest Palindromic Substring

Given a string `s`, return the longest palindromic substring in `s`.

---

Why this matters:
Palindrome problems are common in interviews because they require solid string manipulation, edge case handling, and sometimes dynamic programming.
This specific problem is a great test of your ability to explore patterns within strings efficiently.

---

🧠 Intuition:
A palindrome is a string that reads the same forward and backward.
To find the **longest** one, we can check around each character in the string and expand outwards to see how far we can go while it remains a palindrome.

We repeat this for every character – treating it as the **center** of a potential palindrome.

---

🚶‍♂️ Approach:
1. Define a helper function `expand_around_center` to grow around matching characters.
2. For each character in the string:
   - Check for **odd-length palindromes** (centered on one character).
   - Check for **even-length palindromes** (centered between two characters).
3. Use the helper to get the longest palindrome for each center and update the result if it's longer than the current best.
4. Return the longest found palindrome.

This avoids checking every substring and instead focuses only on valid centers.

---

⏱️ Complexity:
- Time: O(n²)  
  For each character, we expand out to check palindromes.
- Space: O(1)  
  We're not using any extra space apart from a few variables.

📝 Note:
This approach is very elegant and efficient enough for most input sizes. For even more performance, dynamic programming or Manacher's Algorithm could be explored.

---
"""
