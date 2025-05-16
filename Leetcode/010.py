# 🧾 Code:
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        # dp[i][j] will be True if s[:i] matches p[:j], else False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # Empty string matches empty pattern

        def isMatch(i: int, j: int) -> bool:
            # Returns True if s[i] matches p[j]
            if i < 0 or j < 0:
                return False
            return p[j] == '.' or s[i] == p[j]

        # Initialize dp for patterns like a*, a*b*, a*b*c* matching empty string
        for j, c in enumerate(p):
            if c == '*' and j > 0:
                dp[0][j + 1] = dp[0][j - 1]

        for i in range(m):
            for j in range(n):
                if p[j] == '*':
                    # '*' can mean zero occurrence or one/more occurrences of the previous char
                    noRepeat = dp[i + 1][j - 1] if j > 0 else False  # zero occurrence
                    doRepeat = isMatch(i, j - 1) and dp[i][j + 1]  # one or more occurrences
                    dp[i + 1][j + 1] = noRepeat or doRepeat
                elif isMatch(i, j):
                    dp[i + 1][j + 1] = dp[i][j]

        return dp[m][n]


"""
Problem: Regular Expression Matching

Implement regular expression matching with support for '.' and '*'.
- '.' Matches any single character.
- '*' Matches zero or more of the preceding element.

Given input strings `s` (text) and `p` (pattern), return True if the pattern matches the entire string.

---

Why this matters:
This problem tests your ability to implement pattern matching and dynamic programming.
It’s a classical problem that touches many key programming concepts like recursion, memoization, and DP.

---

🧠 Intuition:
- Use a 2D DP table where dp[i][j] means if s[:i] matches p[:j].
- Handle '*' carefully since it can represent zero or more occurrences of the previous char.
- '.' is a wildcard matching any single character.

---

🚶‍♂️ Approach:
1. Initialize a DP table with False values and set dp[0][0] = True (empty matches empty).
2. Pre-fill dp for patterns that can match empty strings like 'a*', 'a*b*', etc.
3. Iterate over the string and pattern:
   - If current pattern char is '*':
     - Either ignore the '*' and previous char (zero occurrence).
     - Or if the previous char matches current char in s, move forward (one or more occurrences).
   - Else if current chars match or pattern char is '.', copy dp from previous subproblem.
4. The answer is in dp[len(s)][len(p)].

---

⏱️ Complexity:
- Time: O(m * n), where m = len(s), n = len(p), since we fill a 2D DP table.
- Space: O(m * n), for the DP table.

---
"""