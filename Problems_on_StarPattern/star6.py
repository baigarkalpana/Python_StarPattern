'''
Author:Kalpan Baigar
program to print following pattern

*
* *
*   *
*     *
* * * * *

'''


print("enter number")
num=int(input())


def display(no):
    for i in range(no):
        for j in range(no):
            if(j==0 or i==j or i==no-1):
               print("*",end="")
            else:
                print(end=" ")
        print()    





display(num)
