
fruits = ["apple", "banana", "pear","naartjie", "pineapple", "orange", "naartjie"]
print(fruits)

print(fruits[2]) #showing a specific item in the list

fruits[1] = "litchi" #changing an item at a certain position in the list

print(fruits) 

fruits.append("lemon") #adding an item at the end of the list
print(fruits)

fruits.insert(3, "lemon") #inserting an item into a certain position in the list
print(fruits)

fruits.remove("naartjie") #removes an item from the list and only removes the first instance if there are multiples of that item
print(fruits)

fruits.sort() #sorts items in ascending order
print(fruits)

fruits.sort(reverse=True) #sorts items in descending order
print(fruits)

