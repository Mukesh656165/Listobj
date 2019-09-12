even = [2,4,6,8]
print(even)
another_even = even
print(another_even)

print(id(even))
print(id(another_even))

another_even.sort(reverse=True)
print(even)
print(another_even)
print(another_even==even)

print(another_even is even)
even = [2,4,6,8]
odd = [1,3,5,7]

numbers = [even,odd]

for num in numbers:
    print(num)

    for value in num:
        print(value)