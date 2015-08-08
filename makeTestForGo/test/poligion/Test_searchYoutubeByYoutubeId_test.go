package db
import (
    "my"
	"testing"
)

func Test_searchYoutubeByYoutubeId(t *testing.T) {
    var (
	

	youtubeId string

	onlyOne *YoutubeSearchResult

	onlyOne_expected *YoutubeSearchResult
        )
    onlyOne = searchYoutubeByYoutubeId(youtubeId)
    
	expectedJson_onlyOne := ``
	my.FromJson(expectedJson_onlyOne, &onlyOne_expected)
	my.Test(onlyOne, onlyOne_expected, t)
}