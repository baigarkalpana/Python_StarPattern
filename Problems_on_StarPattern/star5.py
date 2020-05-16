'''
Author:Kalpan Baigar
program to print following pattern


   *
  **
 ***
****

space=no-1;


'''


print("enter number")
num=int(input())


def display(no):
    space=no-1
    for i in range(0,no+1):
        for j in range(0,no+1):

            for k in range (0,space):
                print("$",end=' ')
               
            
        print()    



display(num)
