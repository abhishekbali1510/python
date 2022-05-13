from email.quoprimime import body_length


bigbang={"sheldon","leonard","penny","sheldon"}
print("bigbang :",bigbang )

# type
print("type : ",type(bigbang))

# length
print(len(bigbang))

testset=set(("a","b",5))
print("test set : ",testset)

# loop
for x in bigbang:
    print(x)

# add items
bigbang.add("raj")
print("after adding raj : ",bigbang)

even={"2","4","6"}
numbers={"1","3","5"}
numbers.update(even)
print("numbers : ",numbers)

# remove items
bigbang.remove("sheldon")               #if element is not in set will raise an error
print("after removing sheldon : ",bigbang)

bigbang.discard("sheldon")      #if element is not in set will not raise an error
print("not error set : ",bigbang)  

numbers.pop()
print("numbers : ",numbers)

numbers.clear()     #removes all elements
print(numbers)

# del numbers will delete the set

# join 2 sets using update and union
set1={"apple","banana","cherry","kiwi"}
set2={"apple","kiwi","mango"}

print("union : ",set1.union(set2))

print("intersection : ",set1.intersection(set2))

print("symmetric difference : ",set1.symmetric_difference(set2))


