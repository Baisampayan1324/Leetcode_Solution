# 🧾 Code:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode()
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry, digit = divmod(total, 10)

            current.next = ListNode(digit)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy_head.next

"""
Problem: Add Two Numbers

You’re given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

---

Why this matters:
This is one of the most asked Linked List problems in interviews.
It teaches you how to handle data structures like linked lists while simulating elementary school-style addition (digit by digit, carrying over values).

---

🧠 Intuition:
Imagine how we add numbers manually: we go from right to left, add digits one by one, and carry over if the sum is more than 9.

Here, the numbers are already in reverse order, so we can directly add from head to tail.
We just walk through both lists at the same time, add their values (plus carry), and build the resulting linked list as we go.

---

🚶‍♂️ Approach:
1. Initialize a dummy head node to simplify handling the result list.
2. Set a current pointer starting at the dummy head and a variable `carry = 0`.
3. Loop while either `l1` or `l2` has nodes left (or there's a carry).
4. At each step:
   - Extract values from the current nodes (or use 0 if one list is shorter).
   - Add them together with the carry.
   - Set the new carry (use `divmod` to get digit and carry).
   - Create a new node with the resulting digit and move forward.
5. Return the next node of dummy head (the real result list).

---

⏱️ Complexity:
- Time: O(max(m, n))  
  We traverse each list once, where `m` and `n` are the lengths of the two input lists.

- Space: O(max(m, n))  
  We create a new list to store the result, which could be as long as the longer input.

---
"""