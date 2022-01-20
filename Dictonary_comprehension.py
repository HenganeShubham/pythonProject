from functools import reduce

'''a = {1: "one", 2: 'two'}
print(a)
a[3] = 'Three'
print(a)


a[2] = 'Twooooo'
print(a)'''

a = {x:x*x for x in range(1, 10)}
print(a)


b = {'names': ['sanket', 'pallavi', 'python']}
print(b)



#-------------------TUPLE------------------------

tuple1 = (10, 'name', 10.4)
print(tuple1)



a = {10, 20, 30, 10, 20} #duplicate elements will get automatically removed..
print(type(a))
print(a)

b = {10, 20}
b.update([30, 40, 50])
print(b)

c = {10, 20}
c.update((30, 40, 21, 50))
print(c)

list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newlist = reduce((lambda x, y: x + y), list4)
print(newlist)
