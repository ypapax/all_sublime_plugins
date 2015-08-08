// Sometimes we'll want to sort a collection by something
// other than its natural order. For example, suppose we
// wanted to sort strings by their length instead of
// alphabetically. Here's an example of custom sorts
// in Go.

package elit

import (
	"encoding/json"
)

func Test_toJson(t *testing.T) {

	actual := toJson(FotoList{
		{bigFoto: "1.jpg"},
		{bigFoto: "10.jpg"},
	})
	expected := ""
	my.Test(actual, expected, t)
}
