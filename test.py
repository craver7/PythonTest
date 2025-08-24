# -*- coding: utf-8 -*-
var = 1 + 2 * 3
print(var)
for i in range(10):
    if i % 2 == 0:
        print(i)
for j in range(100):
    if j % 3 == 0:
        print("Fizz")
        continue
    if j % 5 == 0:
        print("Buzz")
        continue
    if j % 15 == 0:
        print("FizzBuzz")
        continue
    else:
        print(j)

x=3

def calc(x):
    x += 4
    return x
print(x)
print(calc(x))
print(x)

a=[3]

def calc(a):
    a[0] += 4
    return a

print(a)
print(calc(a))
print(a)

b=[3]

def calc(b):
    b=[4]
    return b

print(b)
print(calc(b))
print(b)

def solution(arr):
    answer = []
    for num in arr:
        answer.extend([num] * num)
    return answer

def solution2(arr):
    answer = []
    for num in arr:
        answer.append([num] * num)
    return answer

print(solution([5,1,4]))
print(solution2([5,1,4]))

my_list = [1, 2]
num = 3
my_list.extend([num] * num)
print(my_list)

import random

count = 0    #부채꼴에 들어가는 점의 개수
totalNum = 100000  #전체 점의 개수

for i in range(totalNum):
    x = random.uniform(0,1) #랜덤 x좌표
    y = random.uniform(0,1) #랜덤 y좌표
    if x**2 + y**2 <= 1:  #x**2 + y**2이 1보다 작거나 같으면
        count += 1        #count를 증가시킴

print(count / totalNum * 4)   # 부채꼴 안의 점의 개수 / 전체 점의 개수 * 4

import math

def distance_function(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(distance_function(2,3,4,5))

import math

def my_abs(num):
    if num < 0:
        return -num
    return num

def manhatten_distance(x1, y1, x2, y2):
    return my_abs((x2-x1) + (y2-y1))

print(manhatten_distance(2,3,4,5))

#예제7. 위 코드가 아래와 같이 출력될 수 있도록 하려면 최종적으로 만들어지는 리스트가 [1, 0, 4]여야 함

num = int(input('거슬러줄 돈을 입력: '))
coin = [10, 7, 1]
c = []

coin = [10, 7, 1]

for i in range(len(coin)):
    temp = num//coin[i]
    num = num % coin[i]

    c.append(temp)

print(c)

a = 'france'
b = 'french'

#a랑 b를 이렇게 바꿔줘야 함
#['FR', 'RA', 'AN', 'NC', 'CE']
#['FR', 'RE', 'EN', 'NC', 'CH']

result1 = []

for i in range(len(a) - 1):
    result1.append(a[i:i+2].upper())

print(result1)

# pip install pandas
import pandas as pd

s = pd.Series(["Ab","Cd","Ef", 123])

print(s)

# df = pd.DataFrame({'Name': ['A', 'B', 'C', 'D', 'E'],})

df = pd.read_csv('/mnt/chromeos/MyFiles/Downloads/test.csv')
df.info()