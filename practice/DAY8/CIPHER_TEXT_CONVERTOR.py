import random

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
listLen = len(alphabets)
start = True

#encode and decode method
#encode
def encode():
    cipherText =""
    plainText = input("Enter your message: ").lower()#ayush
    shifts = int(input("How many shifts you want to perform: "))
    for i in plainText:
        if(i==" "):
             cipherText += i
        else:
            #calculate alphabet's index in list(alphabets)
            indexOfAlpha = alphabets.index(i)
            finalShift = (indexOfAlpha+shifts)%listLen
            cipherText += alphabets[finalShift]
    return cipherText

       
#decode method
def decode():
    plainText = ""
    cipherText = input("Enter your encrypted message: ").lower()#ayush
    shifts = int(input("How many shifts you want to perform: "))
    for i in cipherText:
        if(i==" "):
             plainText += i
        else:
            indexOfAlpha = alphabets.index(i)
            finalShift = (indexOfAlpha-shifts)%listLen
            plainText += alphabets[finalShift]

    return plainText



#Actual starting point
while (start):
    choice = input("What do you want encode or decode: ")
    if(choice == "encode"):
        #cipherText = encode()
        print("encode method: "+encode())
    elif(choice =="decode"):
        print("decode method: "+decode())
    else:
        print("please choice between encode and decode")
        start = False
        print("Program is terminated because of invalid choice")
        
    
