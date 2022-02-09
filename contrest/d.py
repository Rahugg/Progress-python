from math import factorial
n = int(input())

pascal = []

for i in range(n):
    for j in range(i+1):
        pascal.append(factorial(i)//(factorial(j)*factorial(i-j)))
    yo = list(map(int, pascal))
    print(yo)
    pascal.clear()