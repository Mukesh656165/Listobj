# appending Item in list
'we can add item in a list in start of list or end of a list through +concatenation'
'or += augmented oprator'
a = ['jason','bond']
print(a)
a += ['root','pietersen']
print(a)

'now we need to add it in 1st of the list'
print(a)
a = ['cook','anderson'] + a
print(a)

'Note--> list must be concatenated with another list ,so if you want to add one element'
# you need to make it as list
a1 = ['eman','avesh']

# a1 += 20
# print(a1) # type error
a1 +=[20]
print(a1)

# some more experiment

a2 = [20,30]
a3 = ('ak',20)# we can concatenate with tuple also(list must be concatenated with iterbale)
a2 += a3
print(a2)

'Technically it is not quite correct to say list can be concatenated with a list'
"more precisely we can say list is concatenated with a iterable object"

# note
'strings are also iterable  so if we concatenate a string with list then the resilt comes in diffrent'
a2 = [20,30,40]
#a2 += 'raj'
print(a2)
#op---[20, 30, 40, 'r', 'a', 'j']
'if we want to make it as a list then make it singleton list'
a2 += ['raj']
print(a2)