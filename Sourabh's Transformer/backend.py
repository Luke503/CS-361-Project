def listToString(s): 
    str1 = "" 
     
    for ele in s: 
        str1 += ele 
        str1 += ' ' 
    
    return str1 


def findAndReplace(beforeText,numLength):
    finalArray = []

    print(beforeText)
    newText = beforeText.split(' ')
    print(newText)

    for x in newText:
        print(x)
        if len(x) <= int(numLength):
            finalArray.append(x)

    print('DONE')
    print(finalArray)
    return listToString(finalArray)