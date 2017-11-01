// Write a function that takes a string as input and reverse only the vowels of a string.

// Example 1:
// Given s = "hello", return "holle".


package main

import "fmt"
import "strings"

func reverseVowel(v string) string {
  if len(v) == 0 {return v}

  input := []rune(v)
  vowelkey := "aeiouAEIOU"
  start := 0
  end := len(input)-1

  for start < end {
    for start < end && !(strings.ContainsAny(vowelkey, string(input[start]))){
      start ++
    }
    for start < end && !(strings.ContainsAny(vowelkey, string(input[end]))){
      end --
    }

    temp := input[start]
    input[start] = input[end]
    input[end] = temp
    start++
    end--
  }
  s := string(input)
  return s
}

func main() {
    s := "Hello"
    fmt.Println(reverseVowel(s))
}
