package db

import (
	"code.google.com/p/google-api-go-client/googleapi/transport"
	"code.google.com/p/google-api-go-client/youtube/v3"
	"flag"
	"my"
	"net/http"
)

var (
	maxResults = flag.Int64("max-results", 25, "Max YouTube results")
	service    *youtube.Service
	response   *youtube.SearchListResponse
)

const developerKey = "AIzaSyBprNsfwC--UTIOkeqeh2VW51jllNJy9RM"

type YoutubeSearchResult struct {
	Title, YoutubeId string
}

func searchYoutubeByYoutubeId(youtubeId string) (onlyOne *YoutubeSearchResult) {
	results, err := searchYoutubeByKey(youtubeId)
	my.FLI(err)
	if len(results) > 0 {
		for _, youtubeResult := range results {
			if youtubeResult.YoutubeId == youtubeId {
				onlyOne = youtubeResult
				return
			}
		}
	}
	return
}

// it can search by title and by youtubeId
func searchYoutubeByKey(str string) (result []*YoutubeSearchResult, err error) {
	query := flag.String("query", str, "Search term")
	flag.Parse()

	client := &http.Client{
		Transport: &transport.APIKey{Key: developerKey},
	}

	service, err = youtube.New(client)
	if err != nil {
		return
	}

	// Make the API call to YouTube.
	call := service.Search.List("id,snippet").
		Q(*query).
		MaxResults(*maxResults)
	response, err = call.Do()
	if err != nil {
		return
	}

	// Iterate through each item and add it to the correct list.
	for _, item := range response.Items {
		switch item.Id.Kind {
		case "youtube#video":
			result = append(result, &YoutubeSearchResult{Title: item.Snippet.Title, YoutubeId: item.Id.VideoId})
		}
	}
	return
}

var SearchYoutubeByKey = searchYoutubeByKey
