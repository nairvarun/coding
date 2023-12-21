package set

import (
	"fmt"
	"strings"
)

type Set[T comparable] map[T]struct{}

func (s Set[T]) Add(elem T) {
	s[elem] = struct{}{}
}

func (s Set[T]) Contains(elem T) bool {
	_, ok := s[elem]
	return ok
}

func (s Set[T]) Remove(elem T) {
	delete(s, elem)
}

func (s Set[T]) String() string {
	elems := make([]string, 0, len(s))
	for e := range s {
		elems = append(elems, fmt.Sprintf("%v", e))
	}
	return fmt.Sprintf("{%s}", strings.Join(elems, ", "))
}
