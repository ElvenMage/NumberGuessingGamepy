from random import randint
import os
a = randint(1,100)
while True:
   
    value = input("Enter a Number")
    value=int(value)
    os.system("cls")
    if(a<value):
        print("too high")
    elif(a>value):
        print("too low")
    elif(a==value):
        print("You are awesome")
        a=randint(1,100)
        continue
