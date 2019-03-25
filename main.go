package main

import (
	"os"

	"github.com/elielodeveloper/examplebeat/cmd"

	_ "github.com/elielodeveloper/examplebeat/include"
)

func main() {
	if err := cmd.RootCmd.Execute(); err != nil {
		os.Exit(1)
	}
}
