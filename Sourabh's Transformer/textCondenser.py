import PySimpleGUI as sg
import tkinter
from tkinter import messagebox
from threading import Timer
from tkinter import * 
from time import sleep


def loadingScreen(userInput):
    layout = [[sg.Text("Fetching Data...")],[sg.Text(''),sg.Submit('Continue')]]
    window = sg.Window('Window Title', layout, margins=(200, 100))

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Continue":
            sleep(1)
            window.close()
            beforeText = 'this is a test paragraph'
            newText = findAndReplace(beforeText,userInput)
            numCut = wordsCut(beforeText,userInput)
            displayTexts(beforeText,newText,numCut,userInput)




def helpScreen():
    layout = [[sg.Text("This Software Goes Through text given by a Wikipedia Scrapper and condenses it so that words less than your inputted value are shown")],
    [sg.Text("Instructions")],[sg.Text('____________________')],[sg.Text('1. Input A Number(represents the min value of letters in a word)')],
    [sg.Text('2. Click Continue Once Data Has Been Fetched')],[sg.Text('3. View The Number Of Words Cut, The Text Before, and The Text After')],
    [sg.Submit('Back')]]
    window = sg.Window('Window Title', layout, margins=(200, 100))

    while True:
        event, values = window.Read()
        if event in (None, 'Exit'):
            break
        elif event == 'Back':
            window.close()
            homePage()

    

def wordsCut(beforeText,numLength):
    newText = beforeText.split(' ')
    count = 0

    for x in newText:
        if len(x) > int(numLength):
            count = count + 1

    return count
        
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
    return finalArray

def displayTexts(beforeText,afterText,numCut,userInput):
    numCut = str(numCut)
    userInput = str(userInput)
    newAfterText = " "
    newAfterText = newAfterText.join(afterText)
    layout = [[sg.Text('Cutting Words Greater Than = ' + userInput + ' letters')],[sg.Text('Words Cut = ' + numCut)], [sg.Text('Before')],[sg.Text("____________________")],
     [sg.Text(beforeText)],[sg.Text('')], [sg.Text('After')], [sg.Text("____________________")], [sg.Text(newAfterText)], ]

    window = sg.Window('Window Title', layout, margins=(200, 100))
    
    while True:
        event, values = window.Read()
        if event in (None, 'Exit'):
            break
        if event == 'Submit':
            window.close()
            #loadScreen(True)
        elif event == 'Cancel':
            func('Pressed button Cancel222')

    event, values = window.Read()
            


def homePage():
    layout = [[sg.Text('Transformer App')],[sg.Text('_________________')], 
    [sg.Text('This service searches scraped wiki text and transforms it into')], 
    [sg.Text('text containing words less than or equal to your inputted value')], [sg.Text('Word Length')], [sg.InputText()], 
    [sg.Submit('Submit'), sg.Cancel('Cancel')],[sg.Text('')],[sg.Text('')],[sg.Button('Help') ]]

    window = sg.Window('Window Title', layout, margins=(50, 100))

    while True:
        event, values = window.Read()
        if event in (None, 'Exit'):
            break
        if event == 'Submit':
            window.close()
            #beforeText = 'this is a test paragraph'
            #newText = findAndReplace(beforeText,values[0])
            #numCut = wordsCut(beforeText,values[0])
            #displayTexts(beforeText,newText,numCut,values[0])
            loadingScreen(values[0])
        elif event == 'Cancel':
            func('Pressed button Cancel222')
        elif event == 'Help':
            window.close()
            helpScreen()

    event, values = window.Read()




homePage()
