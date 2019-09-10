'changing a list items'
mylist = ['john','orton','greezemann','mbappe','marcos rojo','roben vanpersie']
print(mylist)
mylist[1]= 'kaka'
print(mylist)
'we need to change the last item of a list'
mylist[-1]='snider'
print(mylist)

# string is mutable so if we want to assign a new value to a exist string
# we may encounter a error
mystring = 'roben'
'now we need to access '
print(mystring[2])
'if we want to chnage a value it will encounter a error'
# mystring[2] = 'v'
# # print(mystring)

'deleting a item in mylist by del command'
del mylist[-1]
print(mylist)
# Modifying multiple list values at a time
'we can modify multiple continious list value through slicing'
mylist1 = ['ramos','ak','bk','mk','sk','demario','zlatan','fernando torres',]
print(mylist1[1:5])
print(mylist1)
mylist1[1:5] = ['isco','nacho','costa','assencio']
print(mylist1)
mylist1[1:6] = 'nachho'
print(mylist1)
'we can store list inside one more list object'
a = ['super', mylist1]
print(a)
# one trick to remember
a1 = [1,2,3,4]
print(a1)
a1[0:3]=[5,6,7,8,9]
print(a1)
'It neednot be required to pass the equal number of elemnt in slicing'
'we can pass as many element we want python just  grows and shrinks the list as much it need'
'you can pass multiple element in place of single element'

# we can also add a list inside a list through slicing
a2 = [1,2,3,4]
print(a2)
a2[2]=[3,4,5,6]
print(a2)
# it is coming as a list inside another list called nested
'it doesnt make sense we want a list not nested list'
print(a2)
a2[2:3]=[3,4,5,6]
print(a2)

# Trick to delete multiple items in list
a3 = ['jason',1,2,2.5,True,45]
print(a3)
print(len(a3))
'Tricks to delete '
print(a3[0:6])
a3[0:6] = []
print(a3)
# we dnt want to delete whole list we need delete some portion of a list
print(a3)
print(a3[1:5])
a3[1:5] = []
print(a3)

'now try to using del methods'
print(a3)
del a3[1:4]
print(a3)
