
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
import pyFind
import navigateToModel

import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
import color

inputText = """require 'colors'
th = require 'throw'
t2 = require 'myAssert/t2'
rf = require './grab/redisFunc'
_ = require 'underscore'
client = rf.client
exports.startsLikeShortCode = (code, number, autocb)->
    firstChar = code[0]
    globalName = "codes:9"
    switch firstChar
        when "4" then globalName = "4x"
        when "8" then globalName = "8x"
        when "3" then globalName = "3x"

    await rf.sgetSorted globalName, defer codes
    codesLike = codes.filter (c)->
        index = c.indexOf code  
        index is 0
    # 903 905 906
    fromToArr = {}
    await 
        for codeI in codesLike
            @startsLikeCodeNumber codeI, number, defer(fromToArr[codeI])
    fromToArr
    result = []
    for code of fromToArr
        fromTos = fromToArr[code] 
        for fromTo in fromTos
            result.push "#{code}:#{fromTo}" 

    
    result

exports.startsLikeCodeNumber = (code, number, autocb)->
    # if code.length is 3
    await @startsLike code, defer fromTo
    if number.length
        ok = fromTo.filter (i)->
            index = i.indexOf number
            index is 0
    else
        fromTo
exports.startsLike = (code, autocb)->
    await rf.sgetSorted code, defer fromTo
    fromTo
findFullNumber = (fullNumber, autocb)->
    t1 = process.hrtime()
    await (require './toCodeAndEnd') fullNumber, defer code, tail
    t2 t1, "findFullNumber.1 #{fullNumber}"

    t111 = process.hrtime()
    await rf.sgetSorted code, defer fromTo
    th.log fromTo.length
    th.log "up fromTo.length"
    t2 t111, "findFullNumber.111 #{fullNumber}"
    t112 = process.hrtime()
    type = typeof fromTo
    found = null
    for item in fromTo
        parts = item.split ":"
        from = parts[0]
        end = parts[1]

        fromInt = parseInt from, 10
        endInt = parseInt end, 10
        tailInt = parseInt tail, 10
        if fromInt <= tailInt <= endInt
            found = "#{code}:#{item}"
    t2 t112, "findFullNumber.112 #{fullNumber}"     
    return found
exports.find = (number, cb)->   
    whatAfuck = ""
    
    result = []
    initialNumber = number
    th.log number
    th.log " initial number"
    await (require './toCodeAndEnd') number, defer code, tail
    if number.length < "7903".length
        #number like 79 or like 790
        await @allCodes defer allCodes
        codeLen = number.length-1
        # fullCodeLen = 3
        # deltaLen = fullCodeLen - codeLen
        codesObjList = allCodes.map (c)->
            code: c
            short: c.substr 0, codeLen
        codesObjList = codesObjList.filter (co) ->
            co.short is code
        th.log  codesObjList
        th.log "actualCode"
        th.log code
        result = codesObjList.map (co)->
            co.code


    else if number.length is "7903".length
        
        await @isBigCode code, defer isBigCode
        th.log "isBigCode"
        th.log isBigCode
        if isBigCode
            # getCard
            whatAfuck = "bigCode"
            await @opersOfBigCode code, defer opers
            result = opers
        else
            await rf.sgetSorted code, defer result
            result = result.map (i)->
                "#{code}:#{i}"
    else if (number.length > "7903".length) and (number.length <= "7903805".length)     
        await @isBigNumber number, defer isBigNumber
        th.log "isBigNumber"
        th.log isBigNumber

        if isBigNumber
            key = "opersAndRegionOfBigNumber:#{number}"

            await rf.sgetSorted "opersOfBigNumber:#{number}", defer opers
            # await rf.saddIfNotExists "regionsOfBigNumber:#{bigNumber}", regionIdList, defer()
            result = opers

        else
            
            await (require './find/7903MoreNotBigNumber') number, defer result
    else
        await (require './find/7903MoreNotBigNumber') number, defer result      
    cb result, whatAfuck
exports.findOld = (number, cb)->
    t1 = process.hrtime() 
    th.log "start search #{number}"
    await (require './toCodeAndEnd') number, defer code, tail
    if number.length is "79038053525".length
        await findFullNumber number, defer codes
    else if code.length < "903".length
        await @startsLikeShortCode code, "", defer codes
    else
        t01 = process.hrtime()
        await @startsLikeCodeNumber code, tail, defer like
        like = like.map (l)->
            "#{code}:#{l}"

        tfn = require './toFullNumbers' 
        t2 t01, "to1 #{number}"
        t02 = process.hrtime()
        await tfn number, defer from, to
        t2 t02, "to2 #{number}"
        t03 = process.hrtime()
        await 
            findFullNumber from, defer codesFrom
            findFullNumber to, defer codesTo
        codes = _.union codesFrom, codesTo, like
        codes = _.unique codes
        codes = codes.filter (c)->
            c   
        t2 t03, "to3  #{number}"    
            
    t2 t1, "find #{number}"
    cb codes, code, tail    

exports.sqlRegions = (autocb)->
    await rf.matrix "sqlRegions", defer(sqlMatrix)  
    sqlMatrix

exports.eachCodeFromToKey = (globalName, autocb)->
    keys = []
    await rf.sgetSorted globalName, defer(codes9)
    for code in codes9
        await rf.sgetSorted code, defer(fromToSet)
        for fromTo in fromToSet
            keys.push "#{code}:#{fromTo}"
    return keys     
exports.eachOperRegionMass = (globalName, autocb)->
    objects = []
    
    
    await @eachCodeFromToKey globalName, defer (keys)
        # await rf.client.saddIfNotExists 'regions', key.region, defer()
    
    for key in keys
        await rf.hgetall key, defer obj

        obj.key = key
        
        
        objects.push obj
    
    return objects


exports.addRegionFullIfNotExist = (regions, autocb)->
    for reg in regions
        await rf.saddIfNotExists "regionFull", reg, defer()
exports.regionFull = exports.fullRegions = (autocb)->
    await rf.sgetSorted "regionFull", defer(regions)
    return regions
exports.fin = rf.fin
exports.rf = rf

# exports.findInFullRegion = (regionName, fullId, cb)->
#   await rf.sgetSorted "regionFull", defer fullRegion
#   

#   
#   

#   nameParts = regionName.split "-"
#   contains = fullRegion.filter (fr)->
#       target = (nameParts[0]).replace /ия$/, '' #Удмурт ия
#       (~fr.indexOf target) or ( fullId? and (fr is fullId))
#   # rf.fin()  
#   cb contains, rf 
exports.AllRegionsWithCoords = (autocb)->
    await rf.matrix "sqlRegions", defer regions
    regions = regions.map (r)->
        r = r.hash
        obj =
            Name : r.Name
            FullName : r.FullName
            Id: r.Id
            Lat: r.Lat
            Long: r.Long
    regions = regions.filter (r)->
        r.Lat and r.Long        
    regions
exports.x9 = (autocb)->
    await @codes "9x", defer(candidates)
    candidates
exports.x4 = (autocb)->
    await @codes "4x", defer(candidates)
    candidates
exports.x3 = (autocb)->
    await @codes "3x", defer(candidates)
    candidates  
exports.x8 = (autocb)->
    await @codes "8x", defer(candidates)
    candidates      
exports.codes = (name, autocb)->
    await rf.sgetSorted name, defer(candidates)
    candidates
exports.codesByRegion = (regionId, autocb)->
    await rf.sgetSorted "codeFromToBySqlRegionId:#{regionId}", defer codes
    codes
exports.shortCodesByRegion  = (regionId, autocb)->
    await @codesByRegion regionId, defer codes
    shortCodes = @codesToShort codes
exports.codesToShort = (codes)->
    debugger;
    shortCodes = codes.map (code)->
        # 
        # 

        parts = code.split ":"
        parts[0]

    shortCodes = _.unique shortCodes        
    shortCodes

exports.codesOfEveryRegion = (autocb)->
    await rf.client.get "shortCodesBySqlRegionIdAsOneObject", defer err, stringifiedOut
    JSON.parse stringifiedOut
exports.bigBoss = (boss, autocb)->
    await rf.client.hget "oldBigBossByBoss",  boss, defer(err, bigBoss)
    throw err if err    
    bigBoss
exports.codesBySqlRegion = (regionId, autocb)->
    await rf.sgetSorted "codeFromToBySqlRegionId:#{regionId}", defer values
    values

exports.isBigCode = (code, autocb)->
    await rf.client.sismember "moreThan1000Codes", code, defer(err, result)
    result
exports.isBigNumber = (fullNumber, autocb)->
    await rf.client.sismember "allBigNumbers", fullNumber, defer(err, result)
    result  
exports.opersOfBigCode = (code, autocb) ->
    await rf.sgetSorted "moreThan1000Codes:#{code}", defer opers
    opers
exports.allCodes = (autocb) ->
    await rf.sgetSorted "allCodes", defer allCodes
    allCodes
exports.regionsOfBigCode = (code, autocb)->
    await rf.sgetSorted "bigCodesSqlRegions:#{code}", defer regionIdList
    regionList = []
    for regionId in regionIdList
        th.log regionId
        await rf.hgetall "sqlRegions:#{regionId}", defer values
        th.log values
        regionList.push values  
    regionList = regionList.map (i)   ->
        fullName = if i.FullName? then i.FullName else i.Name
        i.FullName = fullName
        i
    regionList    """

positionForBigTest = len("""require 'colors'
th = require 'throw'
t2 = require 'myAssert/t2'
rf = require './grab/redisFunc'
_ = require 'underscore'
client = rf.client
exports.startsLikeShortCode = (code, number, autocb)->
    firstChar = code[0]
    globalName = "codes:9"
    switch firstChar
        when "4" then globalName = "4x"
        when "8" then globalName = "8x"
        when "3" then globalName = "3x"

    await rf.sgetSorted globalName, defer codes
    codesLike = codes.filter (c)->
        index = c.indexOf code  
        index is 0
    # 903 905 906
    fromToArr = {}
    await 
        for codeI in codesLike
            @startsLikeCod""")

class Test(unittest.TestCase):
    
    def test_bigFile(self):
        color.blue("test here baby")
        

        expected = ['', 'startsLikeCodeNumber']
        


        result = navigateToModel.getObject(inputText, positionForBigTest)

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()     
