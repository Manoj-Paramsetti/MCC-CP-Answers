n  = int(input())
#Splitting input into number to make it as list
number = [int(x) for x in input().split()]
#Getting position to check where the element is moved 
position = int(input())-1
#Getting element to proctor
num = number[position]
#Sorting using built-in function
number.sort()
#Checking where is the element after sorting
#Linear Search is used
for i in range(0,n):
    if(number[i]==num):
        print(i+1)