def subtract(a, b):
    return a -b

def add(a,b):
    return a+b
import math

def square_root(a):
    return math.sqrt(a)

a, b = map(int, input().split())
print(subtract(a, b))