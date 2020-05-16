'''
Author:Kalpan Baigar
program to print following pattern

Rhombus Pattern:

Enter rows: 5
    *****
   *****
  *****
 *****
*****

'''


print("enter number")
num=int(input())


def display(no):
    for i in range(1,no+1):
        for j in range(no-i,0,-1):
            print(" ",end=" ")
        for k in range(no):
            print("*",end="")
            
        print()    





display(num)
