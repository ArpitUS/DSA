// 010 — Missing Number
// Given array containing n distinct numbers in range [0,n], return missing one.
// Example
// Input: [3,0,1]
// Output: 2

package arrays

func missingNumber(nums []int) int {
	n := len(nums)
	expectedSum := n * (n + 1) / 2
	actualSum := 0
	for _, num := range nums {
		actualSum += num
	}
	return expectedSum - actualSum
}
