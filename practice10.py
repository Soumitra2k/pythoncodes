#set
my_set={1,2,3,4,5}
print(my_set)

#adding/removing elements to set

my_set.add(9)

print(my_set)
my_set.remove(9)
print(my_set)

my_set.add(5)
print(my_set)
my_set1={1,'one'}
print(my_set1)

# set operation

set1={1,2,3,4,5}
set2={4,5,6,7,8}
union_set=set1.union(set2)
print(union_set)

intersect_set=set1.intersection(set2)
print(intersect_set)

diff_set=set1.difference(set2)
print(diff_set)


diff_set=set2.difference(set1)
print(diff_set)

# how to check if an element is present in a set or not

print(2 in set1)  # it will check if 2 is in set1  TRUE/False

print(9 in set1) # this will check 9 in set1   TRUE/False

original_set={1,2,3,4,5}
print("original_set = ",original_set)

