// 006 — Product of Array Except Self

// Return array answer where answer[i] equals product of all elements except nums[i].

// Do not use division.

// Example

// Input: [1,2,3,4]
// Output: [24,12,8,6]

package arrays

func productExceptSelf(nums []int) []int {
	n := len(nums)
	answer := make([]int, n)
	prefix := 1
	for i := 0; i < n; i++ {
		answer[i] = prefix
		prefix *= nums[i]
	}
	suffix := 1
	for i := n - 1; i >= 0; i-- {
		answer[i] *= suffix
		suffix *= nums[i]
	}
	return answer
}
