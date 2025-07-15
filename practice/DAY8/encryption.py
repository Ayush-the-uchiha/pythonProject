import random

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
listLen = len(alphabets)
list1 = []
start = True
plainText = ""
cipherText = ""

#encode and decode method
#encode
def encode():
    print(f'\n{"-"*20} Encryption Process {"-"*20}')
    cipherText =""
    plainText = input("Enter your message: ").lower()#ayush
    temp = plainText
    shifts = int(input("How many shifts you want to perform: "))
    for i in plainText:
        if i not in alphabets:
            list1.append(i)
            #print(f'list: {list1}')
        else:
            #calculate final shift
            indexOfAlpha = alphabets.index(i)
            finalShift = (indexOfAlpha+shifts)%listLen
        if i in alphabets:
            cipherText += alphabets[finalShift]
        else:
            cipherText += list1.pop()         
            
    return cipherText

       
#decode method
def decode():
    print(f'\n{"-"*20} Decryption Process {"-"*20}')
    plainText = ""
    cipherText = input("Enter your encrypted message: ")#ayush
    shifts = int(input("How many shifts you want to perform: "))
    for i in cipherText:
        if i not in alphabets:
            list1.append(i)
            #print(f'list: {list1}')
        else:
            #calculate final shift
            indexOfAlpha = alphabets.index(i)
            finalShift = (indexOfAlpha-shifts)%listLen
        if i in alphabets:
            plainText += alphabets[finalShift]
        else:
            plainText += list1.pop()         
            
    return plainText



#Actual starting point
while (start):
    print(f'\n\n{"-"*60}')
    print("What do you want 'encode' or 'decode': ")
    choice = int(input("1) for 'Encryption' \n2) for 'Decryption':\nChoose:  "))
    if(choice == 1):
        #cipherText = encode()
        print("\nEncrypted message: "+encode())
    elif(choice ==2):
        print("\nDecrypted message: "+decode())
    else:
        start = False
        print("\nProgram is terminated because of invalid choice")
        
    
