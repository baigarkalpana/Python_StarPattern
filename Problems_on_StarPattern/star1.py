'''
Author:Kalpan Baigar
program to print following pattern

*
* *
* * *
* * * *

'''


print("enter number")
num=int(input())

'''
def display(no):
    for i in range(0,no):
        for j in range(i+1):
            print("* ",end=' ')
        print()    



'''
def display(no):
    for i in range(no):
        for j in range(no):
            print("* ",end=' ')
        print()    


display(num)
