package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
	"unicode"
)

func p1(filename string) {
	file, err := os.Open(filename)
	if err != nil {
		fmt.Println(err.Error())
		return
	}
	defer file.Close()

	res := 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		var digits[]rune
		for _, ch := range scanner.Text() {
			if unicode.IsDigit(ch) {
				digits = append(digits, ch)
			}
		}
		res += int(digits[0] - '0') * 10 + int(digits[len(digits)-1] - '0')
	}
	fmt.Println(res)
}


func p2(filename string) {
	f, _ := os.Open(filename)
	defer f.Close()

	m := map[string]string{
		"one": "o1e",
		"two": "t2o",
		"three": "t3e",
		"four": "f4r",
		"five": "f5e",
		"six": "s6x",
		"seven": "s7n",
		"eight": "e8t",
		"nine": "n9e",
	}

	res := 0
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		line := scanner.Text()
		for target, new := range m {
			line = strings.Replace(line, target, new, -1)
		}

		digits := regexp.MustCompile(`\d`).FindAllString(line, -1)
		d1, _ := strconv.Atoi(digits[0])
		dn, _ := strconv.Atoi(digits[len(digits)-1])
		res += d1 * 10 + dn
	}
	fmt.Println(res)
}

func main() {
	// input := "example.txt"
	input := "input.txt"
	// p1(input)
	p2(input)
}
