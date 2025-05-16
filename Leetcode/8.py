# 🧾 Code:
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break

        result *= sign

        # Clamp to 32-bit signed integer range
        if result < -2**31:
            return -2**31
        elif result > 2**31 - 1:
            return 2**31 - 1
        else:
            return result


"""
Problem: String to Integer (atoi)

Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer.

This function mimics the behavior of the C/C++ `atoi` function — converting a string to an integer, handling whitespace, signs, invalid characters, and overflow.

---

🧠 Intuition:
We want to parse the number from a string like how a human or a low-level parser would:
- Trim whitespace
- Look for a sign
- Read in digits until a non-digit appears
- Clamp to 32-bit signed integer limits if needed

---

🚶‍♂️ Approach:
1. Strip leading/trailing whitespace using `strip()`.
2. If the string is empty after stripping, return 0.
3. Determine the sign from the first character if it's '+' or '-'.
4. Iterate through each character:
   - If it's a digit, build the result number.
   - Stop parsing when you hit a non-digit character.
5. Multiply the final result with its sign.
6. Clamp the result within the 32-bit signed integer range:
   - Minimum: -2³¹ → -2147483648
   - Maximum: 2³¹ - 1 → 2147483647

---

⏱️ Complexity:
- Time: O(n), where n is the length of the string.
- Space: O(1), only a few variables used.

---
"""