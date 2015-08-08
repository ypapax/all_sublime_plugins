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
		targetFileContent = """package elit

import (
	"my"
	"testing"
)

func doAllForMiByUrl(url string, expected menuItem, t *testing.T) (res1 int, res2 int) {
	actual := MiByUrl(url)
	my.Test(actual, expected, t)
}

func doAllForAddAlt(mi menuItem, expectedAlt string, t *testing.T) {
	miAddAlt(&mi)
	actual := mi.alt

	my.Test(actual, expectedAlt, t)
}

func doAllFor_fullHtmlUrl(mi *menuItem, expectedFullHtmlUrl string, t *testing.T) {
	actual := fullHtmlUrl(mi)
	my.Test(actual, expectedFullHtmlUrl, t)
}

func TestMiByUrl(t *testing.T) {
	SetMenu()
	url := "Glavnaja"
	expected := menu[0]
	doAllForMiByUrl(url, expected, t)
}

func TestMiByUrlSubMenu(t *testing.T) {
	SetMenu()
	url := "KozyrkiNavesy"
	expected := menu[1].subMenu[1]
	doAllForMiByUrl(url, expected, t)
}

func TestAddAlt(t *testing.T) {
	SetMenu()
	mi := menu[0]

	doAllForAddAlt(mi, "Главная - ТСК 'ЭЛИТСТРОЙ' Тверь", t)
}

func TestFullHtmlUrl(t *testing.T) {
	SetMenu()
	mi := menu[0]

	doAllFor_fullHtmlUrl(&mi, "/Content/fotos2/Glavnaja", t)
}

// func TestHtmlFileUrl(t *testing.T) {

// }

func TestFullGalleryUrl(t *testing.T) {
	SetMenu()
	mi := MiByUrl("PerilaOograzhdenijaIzNerzhavejuwejStali")
	my.Test(galleryUrl(&mi), "/Kovka/Gallereja/PerilaOograzhdenijaIzNerzhavejuwejStali", t)

}

func Test_photosRelPath(t *testing.T) {
	SetMenu()
	mi := MiByUrl("PerilaOograzhdenijaIzNerzhavejuwejStali")
	my.Test(mi.photosRelPath(), "./Content/fotos2/PerilaOograzhdenijaIzNerzhavejuwejStali", t)

}

func Test_photoHtmlPath(t *testing.T) {
	SetMenu()
	mi := MiByUrl("PerilaOograzhdenijaIzNerzhavejuwejStali")

	my.Test(mi.photoHtmlPath("1.jpg"), "/Content/fotos2/PerilaOograzhdenijaIzNerzhavejuwejStali/1.jpg", t)
}

func Test_isThumb(t *testing.T) {

	my.Test(isThumb("10_resize.jpg"), true, t)
}

func Test_isThumbFalse(t *testing.T) {

	my.Test(isThumb("10.jpg"), false, t)
}

func Test_thumbFileNameToBigFileName(t *testing.T) {

	my.Test(thumbFileNameToBigFileName("10_resize.jpg"), "10.jpg", t)
}

func Test_fotoListByMenuItemUrl(t *testing.T) {
	my.Test(fotoListByMenuItemUrl("PerilaOograzhdenijaIzNerzhavejuwejStali"), "./Content/fotos2/PerilaOograzhdenijaIzNerzhavejuwejStali", t)

}

func Test_fileNameListToFotoList(t *testing.T) {
	my.Test(fileNameListToFotoList([]string{"10_resize.jpg", "10.jpg"}), FotoList{foto{Thumb: "10_resize.jpg", BigFoto: "10.jpg"}}, t)

}

func Test_sortFileNames(t *testing.T) {
	fileNames := []string{"10_resize.jpg", "10.jpg", "1_resize.jpg", "1.jpg"}
	expected := []string{"1_resize.jpg", "1.jpg", "10_resize.jpg", "10.jpg"}
	my.Test(sortFileNames(fileNames), expected, t)

}
"""
		position = 56
		result = generateTestFileNameForGoTest.createTestFileContentBySourceFileTargetAndPosition(targetFileContent, position)
		expected = """package elit
import (
    "my"
	"testing"
)

func Test_doAllForMiByUrl(t *testing.T) {
    var (
	

	url string
	expected menuItem
	t *testing.T

	res1 int
	res2 int

	res1_expected int
	res2_expected int
        )
    res1,res2 = doAllForMiByUrl(url,expected,t)
    
	expectedJson_res1 := ``
	my.FromJson(expectedJson_res1, &res1_expected)
	my.Test(res1, res1_expected, t)
	expectedJson_res2 := ``
	my.FromJson(expectedJson_res2, &res2_expected)
	my.Test(res2, res2_expected, t)
}"""
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()