package strutils

import "slices"

func Reversed(s string) string {
	runes := []rune(s)
	slices.Reverse(runes)
	return string(runes)
}
