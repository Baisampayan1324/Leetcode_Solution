# 🧾 Code:
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        return x == x[::-1]


"""
Problem: Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same forward and backward.

For example:
- 121 is a palindrome.
- -121 is not (because of the negative sign).
- 10 is not (because 01 ≠ 10).

---

🧠 Intuition:
We’re checking if a number looks the same from both directions — that is, reversing it gives the same number.
The easiest way is to convert it to a string and check if it equals its reverse.

---

🚶‍♂️ Approach:
1. Convert the integer to a string using `str(x)`.
2. Reverse the string using Python slicing (`[::-1]`).
3. Compare the original string to its reversed version.
   - If equal → it's a palindrome.
   - Otherwise → it's not.

This one-liner approach works great for positive integers.
Note: Negative numbers are not palindromes because of the '-' sign.

---

⏱️ Complexity:
- Time: O(n), where `n` is the number of digits in `x`.
- Space: O(n), due to string conversion and reversal.

---
"""