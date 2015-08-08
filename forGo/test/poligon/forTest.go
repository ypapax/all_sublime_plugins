package main

import (
	"calldb"
	"html/template"
	"my"
	// "text/template"
)

type MegaLocals struct {
	NextNumbers                            calldb.NextNumberListType
	MainContent, EnRuPart, NextNumbersHtml template.HTML
	UseMap                                 bool
	Current                                string
	FindButtonName                         string
	Desc, Keywords, MainPageUrl, Logo      string
	Title                                  template.HTML
	ShowMapRuEnText                        string
}

func numberChooserHtml(megaLocals *MegaLocals, urlPath string) template.HTML {
	megaLocals.Current = calldb.GetCurrentNumberByUrl(urlPath)
	// html := my.ParseTemplateNoExtMin("numberChooser", megaLocals)
	html := minContentByLayout("numberChooser", megaLocals)

	return html
}

func mainPageMegaLocals(en bool, ds *calldb.DataStore) *MegaLocals {
	locals := ds.GetMainPageLocalsFromCache(en)
	my.P("locals in toMegaLocas.go")
	my.P(locals)
	// html := my.ParseTemplateNoExtMin("mainPageMainContent", locals.MainPageCodes)
	html := minContentByLayout("mainPageMainContent", locals.MainPageCodes)

	return &MegaLocals{

		Title: template.HTML(locals.Title), Desc: locals.Desc, Keywords: locals.Keywords, NextNumbers: locals.NextNumbers,
		MainContent: html,
	}
}

func numbersMegaLocals(firstDigits string, en bool, ds *calldb.DataStore) (locals *MegaLocals) {
	locals := ds.GetNumberLocalsAnyWay(firstDigits, en)
	if locals == nil {
		return nil
	} else {
		if en {
			locals.LoadMoreName = "Load more"
		} else {
			locals.LoadMoreName = "Загрузить еще"
		}
		html := minContentByLayout("numbersMainContent", locals)
		return &MegaLocals{
			Title: template.HTML(locals.Title), Desc: locals.Desc, Keywords: locals.Keywords, NextNumbers: locals.NextNumbers,
			MainContent: html,
		}
	}
}

func regionMegaLocals(regionId string, en bool, ds *calldb.DataStore) *MegaLocals {
	locals := ds.GetRegionLocals(regionId, en)
	if locals == nil {
		return nil
	} else {
		html := locals.Codes
		title := my.PrepareSymbolsForHtml(locals.Title)
		my.Pat("title in regionMegaLocals")
		my.P(title)
		return &MegaLocals{
			Title: template.HTML(my.PrepareSymbolsForHtml(title)), Desc: locals.Desc, Keywords: locals.Keywords, NextNumbers: locals.NextNumbers,
			MainContent: html,
		}
	}
}

func minContentByLayout(templName string, locals interface{}) template.HTML {
	return my.ParseTemplateNoExtMinAnyWayTemplateHTML(templName, locals)
}
