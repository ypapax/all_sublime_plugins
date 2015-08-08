package my

import (
	"testing"
)

func Test_FromJson0(t *testing.T) {
	type person struct {
		Name string
		Age  int
	}
	json := `{"Name": "Maksim", "Age": 27}`
	var actual person
	err := FromJson(json, actual)
	if err != nil {
		panic("fail here. Hello")
	}

	expected := person{Name: "Maksim", Age: 27}
	Test(actual, expected, t)
}
