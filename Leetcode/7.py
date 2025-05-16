# 🧾 Code:
class Solution(object):
    def reverse(self, x):
        """
        :type x: list of int
        :rtype: list of int
        """
        result = []
        for num in x:
            sign = -1 if num < 0 else 1
            num *= sign
            reverse = int(str(num)[::-1])
            if reverse > 2**31 - 1:
                result.append(0)
            else:
                result.append(sign * reverse)
        return result


"""
Problem: Reverse Integer (Extended to a List of Integers)

Given a list of integers, reverse the digits of each integer individually.  
If the reversed number exceeds the 32-bit signed integer range `[-2^31, 2^31 - 1]`, return 0 for that number instead.

This is a modified version of the classic LeetCode Problem 7 that applies to a list of integers.

---

Why this matters:
This problem tests your understanding of integer overflow, string manipulation, and sign handling.
It’s a common question in coding interviews that reveals how carefully you manage edge cases in numerical data.

---

🧠 Intuition:
To reverse an integer:
- Ignore the sign for reversal.
- Convert it to a string, reverse the string, convert it back to an integer.
- Reapply the sign.

Since Python handles big integers gracefully, we manually check for 32-bit overflow using the condition `> 2^31 - 1`.

---

🚶‍♂️ Approach:
1. Initialize an empty result list.
2. For each number in the input list:
   - Determine its sign.
   - Reverse its digits using string slicing.
   - If the reversed value exceeds the 32-bit signed integer limit, add `0` to the result.
   - Else, multiply it with the original sign and append to result.
3. Return the result list.

---

⏱️ Complexity:
- Time: O(n * d)  
  Where `n` is the number of elements in the list, and `d` is the number of digits in each number (string conversion & reversal).

- Space: O(n)  
  A new list is returned containing the reversed values.

---
"""