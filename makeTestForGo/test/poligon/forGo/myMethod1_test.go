package myPackage
import (
	"my"
	"testing"
)

func Test_myMethod1(t *testing.T) {
	actual := myMethod()
	expected := ""
	my.Test(actual, expected, t)
}