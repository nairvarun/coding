package projectroot

import (
	"path/filepath"
	"runtime"
)

var (
	_, f, _, _ = runtime.Caller(0)

	// root path
	Path = filepath.Join(filepath.Dir(f), "../..")
)
