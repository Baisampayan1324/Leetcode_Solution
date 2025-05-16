# 🧾 Code:
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [''] * numRows
        current_row = 0
        going_down = False

        for c in s:
            rows[current_row] += c
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1

        return ''.join(rows)


"""
Problem: Zigzag Conversion

The string `s` is written in a zigzag pattern on a given number of rows (`numRows`) and then read row by row.
Convert the given string to this zigzag format and return the final string.

Example:
Input: s = "PAYPALISHIRING", numRows = 3  
Zigzag Pattern:
P   A   H   N  
A P L S I I G  
Y   I   R  

Output: "PAHNAPLSIIGYIR"

---

Why this matters:
This problem is popular because it tests your ability to simulate a pattern in memory and build an intuitive mapping from 2D to 1D structure.
It also helps build a mindset for handling string manipulation in unconventional formats.

---

🧠 Intuition:
When we write characters in a zigzag fashion, they essentially move "down" the rows and then "up" diagonally.
This zigzag pattern repeats, and we can track it row-by-row using a direction flag (`going_down`).

---

🚶‍♂️ Approach:
1. If only one row or the string is shorter than the row count, return the original string (no zigzag needed).
2. Create a list of empty strings for each row.
3. Initialize the starting row and a direction flag (`going_down`) to track whether to move up or down.
4. Iterate through the characters:
   - Append each character to its current row.
   - Flip direction when hitting the top or bottom row.
   - Move to the next row based on the direction.
5. Join all rows into a single string and return.

---

⏱️ Complexity:
- Time: O(n)  
  We traverse the input string once and do constant time operations for each character.

- Space: O(n)  
  We use extra space to store characters row by row before joining them.

---
"""