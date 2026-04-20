# 007 — Rotate Array

# Rotate array to right by k steps.

# Example

# Input: nums=[1,2,3,4,5,6,7], k=3
# Output: [5,6,7,1,2,3,4]

input_nums = [1, 2, 3, 4, 5, 6, 7]
k = 3       
def rotate_array(nums, k):
    n = len(nums)
    k = k % n  # Handle cases where k > n
    
    # Reverse the entire array
    nums.reverse()
    
    # Reverse the first k elements
    nums[:k] = reversed(nums[:k])
    
    # Reverse the remaining n-k elements
    nums[k:] = reversed(nums[k:])
    
    return nums

print(rotate_array(input_nums, k))  # Output: [5,6,7,1,2,3,4]