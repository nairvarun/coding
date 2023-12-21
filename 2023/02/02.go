package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)


func p1(file string) {
	f, _ := os.Open(file)
	defer f.Close()
	res := 0
	id := 0
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		id++
		game := strings.ReplaceAll(strings.Split(scanner.Text(), ":")[1], ";", ",")

		for _, move := range strings.Split(game, ",") {
			parts := strings.Fields(move)
			num, _ := strconv.Atoi(parts[0])
			col := parts[1]

			if (col == "red" && num > 12) ||
			   (col == "green" && num > 13) ||
			   (col == "blue" && num > 14) {
				goto NextGame
			}
		}
		res += id
		NextGame:
	}
	fmt.Println(res)
}

func p2(file string) {
	f, _ := os.Open(file)
	defer f.Close()
	res := 0
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		game := strings.Split(strings.ReplaceAll(strings.Split(scanner.Text(), ":")[1], ";", ","), ",")
		min_red, min_green, min_blue := 0, 0, 0
		for _, move := range game {
			parts := strings.Fields(move)
			num, _ := strconv.Atoi(parts[0])
			col := parts[1]

			switch col {
				case "red":
					min_red = max(min_red, num)
				case "green":
					min_green = max(min_green, num)
				case "blue":
					min_blue = max(min_blue, num)
			}
		}
		res += min_red * min_green * min_blue
	}
	fmt.Println(res)
}

func main() {
	// input := "example.txt"
	input := "input.txt"
	p1(input)
	p2(input)
}
