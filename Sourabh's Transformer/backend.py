def listToString(s): 
    str1 = "" 
     
    for ele in s: 
        str1 += ele 
        str1 += ' ' #this line provides the space between each word in final output
    
    return str1 


def findAndReplace(beforeText,numLength):
    finalArray = []
    newText = beforeText.split(' ')

    for x in newText:
        if len(x) <= int(numLength):
            finalArray.append(x)

    return listToString(finalArray)