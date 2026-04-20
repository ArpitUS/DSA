// 004 — Maximum Subarray

// Given integer array nums, find contiguous subarray with largest sum and return its sum.

// Example

// Input: [-2,1,-3,4,-1,2,1,-5,4]
// Output: 6
// Explanation: [4,-1,2,1]

package arrays

func maxSubArray(nums []int) int {
	maxSum := nums[0]
	currentSum := nums[0]

	for i := 1; i < len(nums); i++ {
		if currentSum < 0 {
			currentSum = nums[i]
		} else {
			currentSum += nums[i]
		}
		if currentSum > maxSum {
			maxSum = currentSum
		}
	}

	return maxSum
}
