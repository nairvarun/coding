package input

import (
	"os"
	"path/filepath"
	"strings"

	"github.com/nairvarun/AdventOfCode/internal/projectroot"
)

func getFileContent(filename string) (string, error) {
	example := filepath.Join(projectroot.Path, filename)

	f, err := os.ReadFile(example)
	if err != nil {
		return "", err
	}

	// trim new line and whitespace
	return strings.Trim(string(f), "\n "), err
}

func Example() (string, error) {
	return getFileContent("example.txt")
}

func MyInput() (string, error) {
	return getFileContent("input.txt")
}
