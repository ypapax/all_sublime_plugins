package elit
import (
	"my"
	"testing"
)

func Test_(t *testing.T) {
    actual := ()
    var expected interface{}
    expectedJson := ``
    my.FromJson(expectedJson, &expected)
    my.Test(actual, expected, t)
}