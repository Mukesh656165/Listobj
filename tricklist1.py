# starting in list
# list are ordered collection of object
a_list = ['sam','dam','dand','bhed']
b_list = ['dand','bhed','sam','dam']
#
print(a_list==b_list)
print(a_list is b_list)
print(id(a_list))
print(id(b_list))
# list have same element and diffrent order are not same

# list can contain complex object like function ,class
int
print(int)
def mak():
    pass
print(mak)

import math
print(math)

a_list = [int,len,mak,math]
print(a_list)

# list accessed by index
a_list = ['python','javascript','html','django']
print(len(a_list))
print(a_list[0])
print(a_list[3])
print(a_list[1])

# access value through nagative index

# to access django
print(a_list[-1])
print(a_list[-4])
print(a_list[-3])

# slicing techniqui in list
lang = ['java','.net','python','javascript']

# to show ['.net','python','javascript']

print(lang[1:])

# to show [python,'javascript]
print(lang[2:])

lang1 = ['java','pearl','ruby','Ai','iot','python','R']

#to print[ruby,ai,iot,'python'] # start:stop uses

print(lang1[2:6])

# print same thing through nagative index
print(len(lang1))
print(lang1[-5:-1])
print(lang1[-5:-1] == lang1[2:6])

#to print [java,to 'iot']
print(lang1[:5])
# # in nagative
print(lang1[-7:-2])

#to print [ruby to python]
print(lang1[2:6])
print(lang1[-5:-1])

# some more example
a_list = ['smith','starck','hazellwood','pattinson']
# to print [stark to pattionson]
print(a_list[1:])
print(a_list[-3:])
#to print [smith to hazelwood]
print(a_list[0:3])
print(a_list[-4:-1])

print(a_list[1:len(a_list)])
# giving [stark to pattinson]
print(a_list[2:])
print(a_list[:3])
print(a_list[2:]+a_list[:3])


