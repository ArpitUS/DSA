// 005 — Move Zeroes

// Move all 0s to end while maintaining relative order of non-zero elements.

// Do it in-place.

// Example

// Input: [0,1,0,3,12]
// Output: [1,3,12,0,0]

package arrays

func moveZeroes(nums []int) {
	nonZeroIndex := 0
	for _, num := range nums {
		if num != 0 {
			nums[nonZeroIndex] = num
			nonZeroIndex++
		}
	}
	for i := nonZeroIndex; i < len(nums); i++ {
		nums[i] = 0
	}
}
