import sys
import color
import util


def do(str1, str2):
    if str1 is None:
        str1 = ""
    len1 = len(str1)
    len2 = len(str2)
    splited1 = list(str1)
    splited2 = list(str2)
    short = splited1 if len1 < len2 else splited2
    if len1 != len2:
        add = range(0,abs(len2-len1))
       
        for i in add:
            
            short += "_"
      
    zipped = zip(splited1, splited2)
    colorStr1 = colorStr2 = ''
    for (i, j) in zipped:
        
        
        
        iRepr = util.goodRepr(i)
        jRepr = util.goodRepr(j)
        if i == j:
            colorStr1 += color.color(iRepr, 'green')    
            colorStr2 += color.color(jRepr, 'green')    
        else:
            colorStr1 += color.color(iRepr, 'red')  
            colorStr2 += color.color(jRepr, 'yellow')   
    color.red('diff:')        
    print(colorStr1)        
    print(colorStr2)