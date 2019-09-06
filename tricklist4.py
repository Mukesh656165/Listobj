#nested list
a_list =  ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
# to access single item which is in this case[a,g,j]
print(a_list[0],a_list[2],a_list[4])
#to access [bb,[ccc,ddd],ee,ff]
print(a_list[1])
#to access [hh,jj]
print(a_list[3])
#to access bb
print(a_list[1][0])
#to access [ccc,ddd]
print(a_list[1][1])
#to access ccc
print(a_list[1][1][0])
#to access ddd
print(a_list[1][1][1])
a_list =  ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
#to access ee
print(a_list[1][2])
#to access ff
print(a_list[1][3])
#to print [hh,ii]
print(a_list[3])
#to access hh
print(a_list[3][0])
#to access ii
print(a_list[3][1])
#to print only last item
print(a_list[4])
# access in diffrent way
x =  ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
# to access ddd
print(x[1])
#then access [ccc,ddd]
print(x[1][1])
# now access ddd
print(x[1][1][-1])
# now some more tricks slicing
print(x[1])
#to access [ccc,ddd]
print(x[1][1:2])

# to reverse [hh,ii]
#to print [hh,ii]
print(x[3])
#then reverse the list
print(x[3][::-1])# Great techniqui to handson slicing and indexing
x =  ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
print(len(x))
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])
print('ddd' in x)
print('ddd' in x[1])
print('ddd' in x[1][1])# not it achives the target




