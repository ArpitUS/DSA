# 006 — Product of Array Except Self

# Return array answer where answer[i] equals product of all elements except nums[i].

# Do not use division.

# Example

# Input: [1,2,3,4]
# Output: [24,12,8,6]

input_nums = [1, 2, 3, 4]

def product_except_self(nums):
    n = len(nums)
    answer = [1] * n
    
    left_product = 1
    for i in range(n):
        answer[i] *= left_product
        left_product *= nums[i]
        
    right_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]
        
    return answer   

print(product_except_self(input_nums))  # Output: [24,12,8,6]