// 003 — Contains Duplicate

// Given an integer array nums, return true if any value appears at least twice, else return false.

// Example

// Input: [1,2,3,1]
// Output: true

package arrays

func containsDuplicate(nums []int) bool {
	seen := make(map[int]bool)
	for _, num := range nums {
		if seen[num] {
			return true
		}
		seen[num] = true
	}
	return false
}
