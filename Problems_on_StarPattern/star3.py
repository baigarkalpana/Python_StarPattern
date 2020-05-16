'''
Author:Kalpan Baigar
program to print following pattern

*****
****
***
**
*

    
'''

print("enter number")
num=int(input())


def display(no):
    for i in range(no,0,-1):
        for j in range(i,0,-1):
            print("*",end=' ')
           
        print()    



display(num)
