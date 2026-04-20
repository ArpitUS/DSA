# 008 — Merge Sorted Arrays

# You are given two sorted arrays nums1 and nums2.

# Merge nums2 into nums1 as one sorted array.

# nums1 has enough space.

# Example

# Input:
# nums1=[1,2,3,0,0,0], m=3
# nums2=[2,5,6], n=3

# Output:
# [1,2,2,3,5,6]

input_nums1 = [1, 2, 3, 0, 0, 0]
m = 3
input_nums2 = [2, 5, 6]
n = 3

def merge_sorted_arrays(nums1, m, nums2, n):
    i = m - 1  # Pointer for nums1
    j = n - 1  # Pointer for nums2
    k = m + n - 1  # Pointer for merged array
    
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    # If there are remaining elements in nums2, copy them
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    
    return nums1

print(merge_sorted_arrays(input_nums1, m, input_nums2, n))  # Output: [1,2,2,3,5,6]