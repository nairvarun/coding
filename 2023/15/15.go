package main

import (
	"fmt"
	"log"
	"os"
	"slices"
	"strconv"
	"strings"
	"unicode"
)


func p1(filename string) {
	f, err := os.ReadFile(filename)
	if err != nil {
		log.Fatal(err)
	}

	inputs := strings.Split(string(f), ",")

	curr_sum := 0
	for _, step := range inputs {
		curr := 0
		step = strings.Trim(step, "\n")
		for _, ch := range step {
			curr = ((curr + int(ch)) * 17) % 256
		}
		curr_sum += curr
	}
	fmt.Println(curr_sum)
}


type lens struct {
	label 		string
	focalLength int
}

func p2(filename string) {
	f, err :=  os.ReadFile(filename)
	if err != nil {
		log.Fatal(err)
	}

	inputs := strings.Split(string(f), ",")

	hashmap := make(map[int][]lens)

	for _, step := range inputs {
		step = strings.Trim(step, "\n")
		curr := 0
		for idx, ch := range step {
			if unicode.IsLetter(ch) {
				curr = ((curr + int(ch)) * 17) % 256
			}

			if ch == '-' {
				pos := slices.IndexFunc(hashmap[curr], func(l lens) bool { return l.label == string(step[:idx]) })
				if pos != -1 {
					hashmap[curr] = slices.Delete(hashmap[curr], pos, pos+1)
				}
			}

			if ch == '=' {
				l := strings.Split(step, "=")
				label := l[0]
				fl, err := strconv.Atoi(l[1])
				if err != nil {
					log.Fatal(err)
				}

				pos := slices.IndexFunc(hashmap[curr], func(l lens) bool { return l.label == label })
				if pos == -1 {
					hashmap[curr] = append(hashmap[curr], lens {
						label: label,
						focalLength: fl,
					})
				} else {
					hashmap[curr][pos].focalLength = fl
				}
				break
			}
		}
	}
	
	ans := 0
	var res int
	for box, lenses := range hashmap {
		for slot, l := range lenses {
			res = (box+1) * (slot+1) * l.focalLength
			ans += res
		}
	}

	fmt.Println(ans)
}

func main() {
	input := "../input.txt"
	// input := "../example.txt"
	// p1(input)
	p2(input)
}
