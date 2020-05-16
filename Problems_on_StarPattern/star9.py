
'''
Author:Kalpana Baigar

print the following star pattern

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
        for j in range(1,i):
            print(" ",end=' ')
        for j in range(1,no+1) :   
            print("*",end=' ')
        print()





display(num)
