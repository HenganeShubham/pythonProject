# Seperate ODD and EVEN numbers from the list

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #default list
odd_list = []
even_list = []

for i in list1: # i will hold each number in the list.
    if i % 2 == 1: # checking the even or odd
        odd_list.append(i)
    else:
        even_list.append(i)

print('odd_list: ', odd_list) # displaying the list.
print("even_list: ", even_list)

