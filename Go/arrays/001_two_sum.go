// 001 — Two Sum

// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// Each input has exactly one solution, and you may not use the same element twice.

// Example:

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]

package arrays

func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	for i, num := range nums {
		if j, ok := m[target-num]; ok {
			return []int{j, i}
		}
		m[num] = i
	}
	return []int{}
}
