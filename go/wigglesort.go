// wigglesort.go - interview problems written in go
// Given an unsorted array nums, reorder it in-place such that
//nums[0] <= nums[1] >= nums[2] <= nums[3]....

// For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].

package main

import (
  "fmt"
)

func wigglesort(array []int) []int {
  n := len(array)
  for i := 1; i < n; i++ {
    if (i%2 == 1) == (array[i-1] > array[i]) {
      array[i], array[i-1] = array[i-1], array[i]
    }
  }
  return array
}

func main () {
  a := []int {3, 5, 2, 1, 6, 4}
  fmt.Println(a)
  fmt.Println(wigglesort(a))
}
