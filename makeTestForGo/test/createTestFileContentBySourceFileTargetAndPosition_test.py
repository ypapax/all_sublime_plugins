import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/makeTest')
import color
import assertMy
import generateTestFileNameForGoTest

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		targetFileContent = """package main

import (
	"github.com/go-martini/martini"
	"my"
	"my/mart"
	"net/http"
	"runly/db"
)

// Request URL:http://localhost:3000/ajaxSearchInYoutubeApi?searchInput=Jarren%20Benton%20-%20Go%20Off%20feat.%20SwizZz%20&%20Hopsin%20(Official%20Video)
//
func searchInputParam(r *http.Request) (paramValue string) {
	paramValue = mart.GetQueryParam(r, "searchInput")
	return paramValue
}
func addSearchRoutes(m *martini.ClassicMartini) {
	m.Get("/ajaxSearchInYoutubeApi", func(w http.ResponseWriter, r *http.Request) {
		searchInput := searchInputParam(r)
		my.P("searchInput")
		my.P(searchInput)
		results, err := db.SearchYoutubeByKey(searchInput)
		my.FLI(err)
		my.P("results")
		my.P(results)
		ren.JSON(w, http.StatusOK, results)

	})
	// http://localhost:3000/searchClipsWithClicks_route?searchInput=Jarren%20Benton%20-%20Go%20Off%20feat.%20SwizZz%20&%20Hopsin%20(Official%20Video)

	m.Get("/searchClipsWithClicks_route", func(w http.ResponseWriter, r *http.Request) {
		searchInput := searchInputParam(r)
		my.P("searchInput")
		my.P(searchInput)
	})
}
"""
		position = 275
		result = generateTestFileNameForGoTest.createTestFileContentBySourceFileTargetAndPosition(targetFileContent, position)
		expected = """package main
import (
    "my"
	"testing"
)

func Test_searchInputParam(t *testing.T) {
    var (
	

	r *http.Request

	paramValue string

	paramValue_expected string
        )
    paramValue = searchInputParam(r)
    
	expectedJson_paramValue := ``
	my.FromJson(expectedJson_paramValue, &paramValue_expected)
	my.Test(paramValue, paramValue_expected, t)
}"""
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()