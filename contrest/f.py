from math import sqrt
def distance(x,y,x1,y1):
    ans = sqrt((x1-x)**2+(y1-y)**2)
    return ans

x,y = int(input()),int(input())
x1,y1 = int(input()),int(input())
print(distance(x,y,x1,y1))