# 1. Write a Python script to create a list of first N natural numbers.
n = int(input('Enter a number : '))

li = [x for x in range(1, n+1)]

print(li)

# 2. Write a Python script to create a list of first N odd natural numbers.

n = int(input('Enter a number : '))

li = [x*2-1 for x in range(1, n+1)]

print(li)

# 3. Write a Python script to create a list of first N even natural numbers.

n = int(input('Enter a number : '))

li = [x*2 for x in range(1, n+1)]

print(li)

# 4. Write a Python script to find the greatest number in a given list of numbers.

li = [2, 9, 11, 8, 1]

print(max(li))

# 5. Write a Python script to find the smallest number in a given list of numbers.
li = [2, 9, 11, 8, 1]

print(min(li))

# 6. Write a Python script to calculate the sum of elements in a given list of numbers.
li = [2, 9, 11, 8, 1]

print(sum(li))

# 7. Write a Python script to remove all non int values from a list.

li = ["Aniket", 9, 3+11j, 8, 1, 5.6]

length = len(li)

i = 0

while i < length:
    if type(li[i]) != int:
        li.pop(i)
        length -= 1
        continue
    i += 1

print(li)

# 8. Write a Python script to print distinct elements along with their frequencies of occurrence in the list.
li = [10, 20, 10, 20, 30, 30, 30, 40]

# print(li.count(10))
# print()

l2 = []
a = 0

for i in li:
    if i not in l2:
        l2.append(i)
        print(i, li.count(i))

# 9. Write a Python script to print indices of all occurrences of a given element in a given list.

li = [10, 20, 10, 30, 20, 40, 30, 20]
l2 = []

for i in li:
    if i not in l2:
        l2.append(i)


for j in l2:
    i = 0
    print(j, end=' : ')
    while i < len(li):
        if j == li[i]:
            print(i, end=' ')
        i += 1
    print()

# 10. Write a python script to sort a list.
li = [60, 20, 10, 20, 30, 30, 30, 40]

print(end='\n\n')


print(li,end='\n\n')
li.sort()

print(li)