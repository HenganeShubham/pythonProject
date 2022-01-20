List2 = [[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]
for i in List2:
    print(i)

list3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
newlist = list(filter(lambda x: x % 2 == 0, list3))
print(newlist)
