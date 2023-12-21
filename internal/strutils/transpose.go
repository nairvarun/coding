package strutils

import (
	"slices"
	"strings"
)

func Transpose(slice []string) []string {
	NUM_ROWS := len(slice[0])
	NUM_COLS := len(slice)
	transposed_slice := make([]string, NUM_ROWS)

	for r := 0; r < NUM_ROWS; r++ {
		temp := make([]string, NUM_COLS)
		for c :=  0; c < NUM_COLS; c++ {
			temp[c] = string(slice[c][r])
		}
		transposed_slice[r] = strings.Join(temp, "")
	}

	return transposed_slice
}

func Rotate(slice []string) []string {
	slices.Reverse(slice)
	return Transpose(slice)
}
