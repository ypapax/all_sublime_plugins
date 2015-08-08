package elit
import (
	"my"
	"testing"
)

func Test_doAllForMiByUrl(t *testing.T) {
	actual := doAllForMiByUrl()
	var expected interface{}
	expectedJson := ``
	my.FromJson(expectedJson, &expected)
	my.Test(actual, expected, t)
}