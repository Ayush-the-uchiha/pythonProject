#love Calculator
true = "true"
love = "love"
name1 = input("Enter the name: ").lower()
name2 = input("Enter your partner name: ").lower()


def loveCalculate(name1, name2):
    firstComparision=0
    secondComparision=0
    #firstName check
    for i in name1:
        for j in true:
           if(i==j):
               firstComparision += 1
    for i in name2:
        for j in true:
           if(i==j):
               firstComparision += 1
    print(f'firstComparision: {firstComparision}')
    #secondName check
    for i in name1:
        for j in love:
            if(i==j):
              secondComparision += 1
    for i in name2:
        for j in love:
            if(i==j):
               secondComparision += 1
    print(f'secondComparision: {secondComparision}')
    loveScore = firstComparision*10+secondComparision
    print(f'lovescore: {loveScore}')


loveCalculate(name1,name2)    
