# 🧾 Code:
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        size = len(nums1)
        
        # Even number of elements
        if size % 2 == 0:
            index1 = nums1[size // 2]
            index2 = nums1[(size // 2) - 1]
            return (index1 + index2) / 2.0
        # Odd number of elements
        else:
            return nums1[size // 2]


"""
Problem: Median of Two Sorted Arrays

You are given two sorted arrays `nums1` and `nums2` of size m and n respectively.
You must return the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

---

Why this matters:
This is a **classic interview problem** that tests your understanding of array manipulation, edge case handling, and optimizing for performance.
While a brute-force merge-and-sort method works, the optimal solution involves binary search – but this approach is still very useful for understanding the basics first.

---

🧠 Intuition:
The simplest idea is to:
1. Merge the two arrays.
2. Sort the result.
3. Return the middle value(s) depending on whether the combined array length is odd or even.

This isn't the most optimal solution in terms of time complexity, but it's intuitive and easy to understand for beginners.

---

🚶‍♂️ Approach:
1. Merge the two input arrays using `extend()`.
2. Sort the combined list.
3. Get the length of the combined list:
   - If it's **even**, average the two middle elements.
   - If it's **odd**, return the middle element directly.

This avoids edge case bugs like index errors or incorrect averaging when the number of elements is even.

---

⏱️ Complexity:
- Time: O((m + n) * log(m + n))  
  Because we're sorting the merged array.
- Space: O(m + n)  
  Since we’re storing all elements in one combined array.

📝 Note:
While the optimal approach would use binary search and achieve **O(log(min(m, n)))**, this method works well for smaller inputs and makes the concept of finding medians much easier to grasp.

---
"""
