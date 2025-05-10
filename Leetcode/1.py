"""
Problem: Two Sum

You're given an array of integers `nums` and a number `target`.
Your job is to find two distinct indices `i` and `j` such that:
    nums[i] + nums[j] == target

Each input has exactly one solution, and you can’t use the same element twice.

---

Why this matters:
This is one of the most classic interview questions. 
It checks your ability to use loops, think in pairs, and solve problems using brute-force and optimized logic.
A great first step into the world of algorithmic thinking.

---

🧠 Intuition:
Okay, so we want to find two numbers that add up to a specific target.
What’s the first idea that pops into your head?
Check every possible pair and see if they match — that's the most direct way to do it.

It’s not the most efficient, but it's easy to understand — and a perfect way to start.

---

🚶‍♂️ Approach:
- Loop through each element using index `i`
- For each `i`, loop through the elements that come after it using index `j`
- For every (i, j) pair, check if `nums[i] + nums[j] == target`
- If yes, return `[i, j]` immediately
- If we finish the loops and find nothing (shouldn’t happen based on constraints), return an empty list

This is called a brute-force solution, but it’s great for clarity.

---

⏱️ Complexity:
- Time: O(n²)  
  Two nested loops — we check all pairs.

- Space: O(1)  
  No extra data structures used except the return list.

---

🧾 Code:
"""

class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []