import HANGMAN

temp = ""
def strConversion(finalList):
    for i in finalList:
        temp +=i
    print("finalName :"+temp)
    if(len(temp)==len(finalList)):
        gameOver = True    
    

