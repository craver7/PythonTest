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