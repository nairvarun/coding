package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type coordinate struct{
	row int
	col int
}

func p1(filename string) {
	f, err := os.ReadFile(filename)
	if err != nil { panic(err) }

	inp := strings.Split(strings.Trim(string(f), "\n"), "\n")

	dir := map[string]coordinate {
		"U": {-1, 0},
		"D": {1, 0},
		"L": {0, -1},
		"R": {0, 1},
	}

	vertex := []coordinate { {0, 0} }

	var boundryPoints int
	for _, line := range inp {
		instruction := strings.Split(line, " ")
		d := dir[instruction[0]]
		n, _ := strconv.Atoi(instruction[1])

		boundryPoints += n

		curr := vertex[len(vertex)-1]
		vertex = append(vertex, coordinate{curr.row + d.row * n, curr.col + d.col * n})
	}

	N := len(vertex)
	// shoelace theorem:
	// https://artofproblemsolving.com/wiki/index.php/Shoelace_Theorem#:~:text=This%20can%20also%20be%20written%20in%20form%20of%20a%20summation
	var shoeLace int
	for i := 0; i < N-1; i++ {
		shoeLace += (vertex[i+1].col + vertex[i].col) * (vertex[i+1].row - vertex[i].row)
	}
	shoeLace = int(math.Abs(float64(shoeLace)))/2

	// pick's theorem
	// https://handwiki.org/wiki/Pick%27s_theorem#:~:text=External%20links-,Formula,-i%20%3D%207%2C
	interiorPoints := shoeLace - boundryPoints / 2 + 1
	fmt.Println(interiorPoints +  boundryPoints)
}

func p2(filename string)  {
	f, err := os.ReadFile(filename)
	if err != nil { panic(err) }

	inp := strings.Split(strings.Trim(string(f), "\n"), "\n")

	dir := map[byte]coordinate {
		'0': {0, 1},
		'1': {1, 0},
		'2': {0, -1},
		'3': {-1, 0},
	}

	vertex := []coordinate{{0, 0}}

	var boundryPoints int
	for _, line := range inp {
		instruction := strings.Split(line, " ")[2]
		d := dir[instruction[7]]
		n, _ := strconv.ParseInt(instruction[2:7], 16, 0)

		boundryPoints += int(n)

		curr := vertex[len(vertex)-1]
		vertex = append(vertex, coordinate{curr.row + d.row * int(n), curr.col + d.col * int(n)})
	}

	N := len(vertex)
	// shoelace theorem:
	// https://artofproblemsolving.com/wiki/index.php/Shoelace_Theorem#:~:text=This%20can%20also%20be%20written%20in%20form%20of%20a%20summation
	var shoeLace int
	for i := 0; i < N-1; i++ {
		shoeLace += (vertex[i+1].col + vertex[i].col) * (vertex[i+1].row - vertex[i].row)
	}
	shoeLace = int(math.Abs(float64(shoeLace)))/2

	// pick's theorem
	// https://handwiki.org/wiki/Pick%27s_theorem#:~:text=External%20links-,Formula,-i%20%3D%207%2C
	interiorPoints := shoeLace - boundryPoints / 2 + 1
	fmt.Println(interiorPoints +  boundryPoints)
}

func main() {
	input := "../example.txt"
	input = "../input.txt"
	p1(input)
	p2(input)
}
