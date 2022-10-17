#1 Basic
for numb in range(0,151):
    print(numb)

#2 Multiples of Five
for mult5 in range(5,1001,5):
    print (mult5)

#3 Counting, the Dojo Way
myList =['Coding', 'Dojo']
for CodingDojo in range(0,101):
    if CodingDojo%10 == 0:
        print(myList[0]+myList[1])
    elif CodingDojo%5 == 0:
        print(myList[0])
    else : print(CodingDojo)

#4 Whoa. That Sucker's Huge
sum=1
for numb in range(0,500001):
    sum=sum+numb
print(sum)

#5 Countdown by Fours
for numb in range(2018, 0 , -4):
    print(numb)

#6  Flexible Counter
def counter(lowNumb , highNumb , mult):
    for numb in range(lowNumb , highNumb):
        if numb % mult == 0:
            print(numb)
counter(2,10,3)