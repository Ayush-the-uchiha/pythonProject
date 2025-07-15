import random


#given
fruit = ["mango","lichi","apple","banana","pineapple","papaya"]
finalList = []
finalName = ""
gameOver = False
TotalLives = 5

#output

#1. Generate a random name
name = random.choice(fruit)
print(name)

#1.2 Assignment of final list
for i in name:
    finalList.append("_ ")
print(f'finallist {finalList}')
#2. Generate as many blanks as name
blankName = ""
for blank in name:
    blankName += "_ "
print("blank: "+blankName)

#3. Ask the user to guess a letter

#while loop yahan se suru hoga
while(gameOver == False):
    print(f'{"_ "*15}Lives: {TotalLives}{"_ "*15}')
    
    guess = input("guess the letter: ")
    print(guess)

    #3.1 Checking if the guessed letter present in the word
    guessInName = False
    for i in range(len(name)):
        if(guess==name[i]):
            guessInName = True
            
    #3.1.1 (if yes) then add guess letter into List        
    if guessInName == True:
        
        for i in range(len(name)):
            if(guess==name[i]):
                finalList[i] = guess
        print(finalList)
        
        #Convertion from list-item to string
        temp = ""
        for i in finalList:
            temp +=i
        print("finalName :"+temp)
        finalName =temp
        if(len(temp)==len(finalList)):
            print("\n You Won!")
            gameOver = True

    #3.1 (if no) then live--
    else:
        TotalLives -= 1
        print("finalName: "+finalName)
        if (TotalLives <=0):
            print("You lost the game")
            gameOver = True
        





    
