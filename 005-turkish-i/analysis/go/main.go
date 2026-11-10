// Turkey test, Go: strings.ToLower / strings.ToUpper / strings.EqualFold.
package main

import (
	"fmt"
	"os"
	"runtime"
	"strings"
)

func main() {
	fmt.Printf("{\"lang\":\"Go\",\"version\":\"%s\",\"locale\":\"%s\",\"api\":\"strings.ToLower / strings.ToUpper / strings.EqualFold\",\"lower_TITLE\":\"%s\",\"upper_title\":\"%s\",\"FILE_equals_file\":%t}\n",
		runtime.Version(), os.Getenv("LANG"), strings.ToLower("TITLE"), strings.ToUpper("title"), strings.EqualFold("FILE", "file"))
}
