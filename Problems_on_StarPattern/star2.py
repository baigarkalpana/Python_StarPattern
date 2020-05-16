'''
Author:Kalpan Baigar
program to print following pattern

****
*  *
*  *  
****

'''


print("enter number")
num=int(input())


def display(no):
    for i in range(0,no+1):
        for j in range(0,no+1):
            if((i==0) or (i==no) or (j==0) or (j==no)):
               print("*",end=' ')
            else:
               print(" ",end=' ') 
        print()    



display(num)
