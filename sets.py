#Sets

'''
my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set.add(6) #adds item to the set
print(my_set)

my_set.remove(3) #removes item from the set
print(my_set)
'''

set1 = {1, 2, 3}
set2 = {3, 4, 5}

#Union
union_set = set1.union(set2) #combines sets
print(union_set)

#Intersection
inter_set = set1.intersection(set2) #shows items that appear in both the sets
print(inter_set)

#Difference
diff_set = set1.difference(set2) #shows items only appear in set1 
print(diff_set)

diff_set2 = set2.difference(set1)
print(diff_set2)