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
		fileTest = """package db

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
}

func getClipByYoutubeId(ds *mon.DataStore, youtubeId string) *Clip {
	var clip Clip
	err := clipCollection(ds).Find(bson.M{"YoutubeId": youtubeId}).One(&clip)
	if mon.PanicIfBadErrAndReturnTrueIfOk(err) {
		return &clip
	} else {
		return nil
	}
}

var foundClipsFromYoutube []*YoutubeSearchResult

func insertFromYoutubeApiToMongo(ds *mon.DataStore, youtubeId string) (clip *Clip) {
	// module.exports = (db, youtubeId, autocb)->
	// 	await getClipByYoutubeId_mongo db, youtubeId, defer result
	// 	[err, clip] = result
	// 	th.err err
	clip = getClipByYoutubeId(ds, youtubeId)
	if clip == nil {

		foundClipsFromYoutube := searchYoutubeByYoutubeId(youtubeId)
		if foundClipsFromYoutube == nil {
			return nil
		} else {
			// 			# createVideo (insert)
			// 			clip =
			// 				Title: clipInfo.title
			// 				YoutubeId: youtubeId
			// first := foundClipsFromYoutube()
			clip = insertClip(ds, foundClipsFromYoutube.Title, foundClipsFromYoutube.YoutubeId)
			return clip
			// 			# await insertMongo db, clip, "clip", defer result
			// 			await insertClip_mongo db, clip, defer result

		}
	}
	return clip

	// 	unless clip
	// 		await videoExists youtubeId, defer result
	// 		[err, exists, clipInfo] = result
	// 		unless exists
	// 			return ['no such clip', null]
	// 		else
	// 			# createVideo (insert)
	// 			clip =
	// 				Title: clipInfo.title
	// 				YoutubeId: youtubeId

	// 			# await insertMongo db, clip, "clip", defer result
	// 			await insertClip_mongo db, clip, defer result

	// 	return [null, clip]

}

func (clip *Clip) localsByClip(ds *mon.DataStore) (locals *YoutubeIdLocals) {
	my.P("clip in localsByClip")
	my.P(clip)
	// unless clip
	// 	return [404, "no clip with id #{clipId}"]
	if clip == nil {
		return nil
	}

	// else
	// 	redirectTo = clip.redirectTo
	// 	if redirectTo
	// 		return [301, redirectTo]
	if len(clip.RedirectTo) > 0 {
		return &YoutubeIdLocals{RedirectTo: clip.RedirectTo}
	} else {
		// 	else
		// 		clipTitle = clip.Title

		// 		await getLastTextByYoutubeId db, youtubeId, defer result
		// 		[err, lastText] = result
		// 		th.err err
		youtubeId := clip.YoutubeId
		lastText := getLastTextByYoutubeId(ds, youtubeId)
		clipTitle := clip.Title
		// 		title = "#{clipTitle} - перевод текста песни"
		// 		h1 = clipTitle
		title := fmt.Sprintf("%s - перевод текста песни", clipTitle)
		h1 := clipTitle
		my.P(title)
		my.P(h1)
		// 		await text2descr lastText, defer result
		// 		[err, descr] = result
		// 		th.err err
		descr := lastText.toDescr()
		var rows []*Row
		if lastText != nil {
			rows = prepareRows(lastText.Rows)
		}

		my.P("rows in youtubeIdLocals.go")
		my.P(rows)
		return &YoutubeIdLocals{
			Title:     title,
			H1:        h1,
			Descr:     descr,
			YoutubeId: youtubeId,
			Rows:      rows,
			ClipTitle: clipTitle,
		}
	}

	// 		rows = if lastText then lastText.rows else []

	// 		locals =
	// 			title: title
	// 			h1: h1
	// 			descr: descr
	// 			youtubeId: youtubeId
	// 			rows: rows
	// 			clipTitle: clipTitle

	// 		return [err, locals]
	return
}
"""
		cursorPosition = 304
		result = generateTestFileNameForGoTest.getLineNumberByTextAndCursorPosition(fileTest, cursorPosition)
		expected = 19
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()