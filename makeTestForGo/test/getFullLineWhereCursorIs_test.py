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
		fileText = """package db

import (
	"fmt"
	"gopkg.in/mgo.v2/bson"
	"my"
	"my/mon"
)

func GetYoutubeIdLocals(ds *mon.DataStore, youtubeId string) {

}

type YoutubeIdLocals struct {
	Title, Descr, RedirectTo, H1, YoutubeId, ClipTitle string
	Rows                                               []*Row
}

func LocalsByYoutubeId(ds *mon.DataStore, youtubeId string) *YoutubeIdLocals {
	clip := getClipByYoutubeId(ds, youtubeId)

	// 	unless clip
	if clip == nil {
		//			# check if such youtubeId exist:
		// 		await insertFromYoutubeApiToMongo db, youtubeId, defer result
		// 		[err, clip] = result
		clip = insertFromYoutubeApiToMongo(ds, youtubeId)
	}
	if clip == nil {
		return nil
	} else {
		return clip.localsByClip(ds)
	}
	//
	// 	unless clip
	// 		return ["no such video in youtube and local with id #{youtubeId}", null]
	// 	else
	// 		await localsByYoutubeId db, youtubeId, defer result
	// 		[err, locals] = result
	// 		return [err, locals]
}"""
		cursorPosition = 305
		result = generateTestFileNameForGoTest.getFullLineWhereCursorIs(fileText, cursorPosition)
		expected = "func LocalsByYoutubeId(ds *mon.DataStore, youtubeId string) *YoutubeIdLocals {"
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()