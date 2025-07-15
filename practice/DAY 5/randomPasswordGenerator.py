import random


letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbol = ['!','@','#','$','%','^','&','*','/',',']
number = ['1','2','3','4','5','6','7','8','9','0']

#concatenate of number and letter list
letter += number



#input from the user
sizeOfPassword = int(input("What will be size of your password: "))#12
numberOfSymbols = int(input("How many symbol do you want in your password: "))#11

if(numberOfSymbols>sizeOfPassword):
    print("Number of symbol must be smaller than size of password")
    exit()
if(numberOfSymbols>len(symbol)):
   print(f"Your symbol is invalid please enter between {0} and {len(symbol)}")
   exit()

    
#password generator
sizeOfPassword -= numberOfSymbols

#listOfCroppedSymbol

#return list of symbol used in randomPassword from symbol list.
sym = list(random.sample(symbol, k= numberOfSymbols))

#return list of letter used in randomPassword from letter list.
newLetter = list(random.sample(letter, k=sizeOfPassword))

password = list(sym+newLetter)
random.shuffle(password)
randomPassword = ""

for i in password:
    randomPassword = randomPassword+i

print("Your password is: "+randomPassword)
