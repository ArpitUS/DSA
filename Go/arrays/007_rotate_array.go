// 007 — Rotate Array

// Rotate array to right by k steps.

// Example

// Input: nums=[1,2,3,4,5,6,7], k=3
// Output: [5,6,7,1,2,3,4]

package arrays

func rotate(nums []int, k int) {
	n := len(nums)
	k = k % n
	reverse(nums, 0, n-1)
	reverse(nums, 0, k-1)
	reverse(nums, k, n-1)
}

func reverse(nums []int, start, end int) {
	for start < end {
		nums[start], nums[end] = nums[end], nums[start]
		start++
		end--
	}
}
