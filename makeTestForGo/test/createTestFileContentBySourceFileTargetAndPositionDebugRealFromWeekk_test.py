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
		targetFileContent = """package model

import (
	"fmt"
	"github.com/go-shadow/moment"
	"html/template"
	"my"
	// "time"
)

type YearLocals struct {
	Weeks        []template.HTML
	Title, Descr string
	H1           template.HTML
}

func WrapBigBold(str string) string {
	return fmt.Sprintf("<b><big>%s</big></b>", str)
}

// 1)29.12-04.01, 2)05.01-11.01, 3)12.01-18.01, 4)19.01-25.01, 5)26.01-01.02, 6)02.02-08.02, 7)09.02-15.02, 8)16.02-22.02, 9)23.02-01.03, 10)02.03-08.03, 11)09.03-15.03, 12)16.03-22.03, 13)23.03-29.03, 14)30.03-05.04, 15)06.04-12.04, 16)13.04-19.04, 17)20.04-26.04, 18)27.04-03.05, 19)04.05-10.05, 20)11.05-17.05, 21)18.05-24.05, 22)25.05-31.05, 23)01.06-07.06, 24)08.06-14.06, 25)15.06-21.06, 26)22.06-28.06, 27)29.06-05.07, 28)06.07-12.07, 29)13.07-19.07, 30)20.07-26.07, 31)27.07-02.08, 32)03.08-09.08, 33)10.08-16.08, 34)17.08-23.08, 35)24.08-30.08, 36)31.08-06.09, 37)07.09-13.09, 38)14.09-20.09, 39)21.09-27.09, 40)28.09-04.10, 41)05.10-11.10, 42)12.10-18.10, 43)19.10-25.10, 44)26.10-01.11, 45)02.11-08.11, 46)09.11-15.11, 47)16.11-22.11, 48)23.11-29.11, 49)30.11-06.12, 50)07.12-13.12, 51)14.12-20.12, 52)21.12-27.12, 53)28.12-03.01,
func GetYearLocals(yearStr string) (yearLocals *YearLocals, currentWeekAnchor template.HTML) {
	year := my.StrToInt(yearStr)
	from, to := firstWeekOfYear(year)
	// first week of next year
	fromNext, _ := firstWeekOfYear(year + 1)
	var weeks []template.HTML
	weekCounter := 1
	var descr string
	for {
		// current week:
		strWeek := weekToStr(toRuString(from), toRuString(to))
		title := titleByYearAndWeekNumber(year, weekCounter)
		linkUrl := yearWeekLinkUrl(year, weekCounter)
		a := weekAnchorByYearWeekNumberAndTextInsideAnchor(year, weekCounter, strWeek)
		if WeekIsCurrent(from, to) {
			a = WrapBigBold(a)
			currentWeekAnchor = template.HTML(weekAnchorByYearWeekNumberAndTextInsideAnchor(year, weekCounter, fmt.Sprintf("%d-я", weekCounter)))
		}
		weeks = append(weeks, template.HTML(a))
		fromShort := toStringForVeryShortDescr(from)
		toShort := toStringForVeryShortDescr(to)
		descrItem := fmt.Sprintf("%d)%s-%s, ", weekCounter, fromShort, toShort)
		descr += descrItem
		my.P(a)
		// next week
		weekCounter++
		from.AddDays(daysInWeek)
		to.AddDays(daysInWeek)
		// if we archived next year - enough
		if from.Diff(fromNext, "seconds") == 0 {
			break
		}
	}
	title := fmt.Sprintf(`недели %d года`, year)
	yearLocals = &YearLocals{
		Weeks: weeks,
		Title: title,
		H1:    template.HTML(title),
		Descr: my.Trim(descr),
	}
	return
}

func yearWeekLinkUrl(year, week int) string {
	return fmt.Sprintf("/%d/%d", year, week)
}

// func descriptionYear(year)

func OneTwoFiftyTwoAnchors() (html template.HTML) {
	today := moment.New()
	yearNow := today.Year()

	const lastWeek = 52
	targetFirstWeeks = []int{1, 2}
	totalHtmlStr = ""
	for _, weekNumber := range targetFirstWeeks {
		strAnchor := generateWeekAnchorForSiteHead(weekNumber)
	}
	totalHtmlStr += "..."
	totalHtmlStr += generateWeekAnchorForSiteHead(lastWeek)
	return totalHtmlStr
}
"""
		position = 2618
		result = generateTestFileNameForGoTest.createTestFileContentBySourceFileTargetAndPosition(targetFileContent, position)
		expected = """package model
import (
    "my"
	"testing"
)

func Test_OneTwoFiftyTwoAnchors(t *testing.T) {
    var (
	


	html template.HTML

	html_expected template.HTML
        )
    html = OneTwoFiftyTwoAnchors()
    
	expectedJson_html := ``
	my.FromJson(expectedJson_html, &html_expected)
	my.Test(html, html_expected, t)
}"""
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()