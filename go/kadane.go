// kadane.go - Interview Problems in Go
// Say you have an array for which the ith element is the price of a given stock on day i.
// If you were only permitted to complete at most one transaction (ie, buy one and sell one
//share of the stock), design an algorithm to find the maximum profit.

// Example:
// Input: [7, 1, 5, 3, 6, 4]
// Output: 5

package main

import (
  "fmt"
  "math"
)

func maxProfit(prices []float64) float64 {
    if len(prices) == 0{
      return 0
    } else {
      var max, min float64
      max = 0
      min = prices[0]
      for i := 0; i < len(prices); i++ {
        if (prices[i] > min){
          max = math.Max(max, (prices[i] - min))
        } else {
          min = prices[i]
      }
    }
    return max
  }
}

func main () {
  prices := []float64 {7, 1, 5 , 3, 6, 4}
  fmt.Println(maxProfit(prices))
}
