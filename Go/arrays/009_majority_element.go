// 009 — Majority Element

// Given array of size n, return element appearing more than n/2 times.

// Assume majority always exists.

// Example

// Input: [3,2,3]
// Output: 3

package arrays

func majorityElement(nums []int) int {
	count := 0
	var candidate int
	for _, num := range nums {
		if count == 0 {
			candidate = num
		}
		if num == candidate {
			count++
		} else {
			count--
		}
	}
	return candidate
}
