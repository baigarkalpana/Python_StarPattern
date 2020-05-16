'''
Author:Kalpan Baigar
program to print following pattern

Rhombus Pattern:

Enter rows: 5
    *****
   *   *
  *   *
 *   *
*****

'''


print("enter number")
num=int(input())


def display(no):
    for i in range(1,no+1):
        for j in range(no-i,0,-1):   #for space printing
            print(" ",end=" ")
        for k in range(1,no+1):      
            if((i==1)or(i==no)or(j==1)or(j==no)):    #for star printing
                print("*",end=' ')
            else:
                print(" ",end=' ')
        print()    





display(num)
