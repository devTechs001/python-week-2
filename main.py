
#create an empty list
my_list = []

#appent items to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert the value 15 at the second position index (2)
my_list.insert(2, 15)

#extend the list with another list
another_list = [50, 60, 70]

#remove the last element from the list for the list
my_list.pop()

#sort the list in ascending order
my_list.sort()

#find and print the value at the index 30
index_of_30 = my_list.index(30)

print(f"the index of 30 in my list is: {index_of_30}")
