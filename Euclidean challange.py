#Euclidean distance code

x1 = input("enter x1: ")
x2 = input("enter x2 : ")
y1 = input("enter y1 : ")
y2 = input("enter y2 : ")
A= [ x1, x2]
B = [y1, y2]
from math import sqrt
C =pow((( int(A[1]))-( int(A[0]))),2)
D =pow((( int(B[1]))-( int(B[0]))),2)
E= sqrt( C + D)
print(f"The Euclidean distance for coordinates({x1},{y1}) and ({x2},{y2}) is {E}")





