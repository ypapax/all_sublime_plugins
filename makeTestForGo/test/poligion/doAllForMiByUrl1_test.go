package elit
import (
	"my"
	"testing"
)

func doAllForMiByUrl1(t *testing.T) {
	actual := doAllForMiByUrl()
	var expected interface{}
	expectedJson := ``
	my.FromJson(expectedJson, &expected)
	my.Test(actual, expected, t)
}