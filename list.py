friends=["ross","joey","chandler","monica","pheobe","rachel"]

print("Friends : ",friends)

# length of list
print("Length of friends : ",len(friends))

print("Type of Friends : ",type(friends))

# list constructor
mylist2=list(("Abhishek",21))
print(mylist2)

print("last element : ",friends[-1])

# range
print("friends from 2 to 4 : ",friends[2:4])
print("friends from -3 to last : ",friends[-3:])

# check for item in list
if "russ" in friends:
    print("yes")
else:
    print("no")

# change values
friends[4]="ursula"
print("ursula in place of pheobe : ",friends)

# insert values
friends.insert(1,"emily")
print("Emily inserted : ",friends)

# append on list
friends.append("Ben")
print("After ben appended : ",friends)

sitcom=["sheldon","ted","robin","leonard"]
sitcom.extend(friends)
print("Sitcom : ",sitcom)

# remove item
friends.remove("ursula")
print("After removing ursula : ",friends)

# friends.remove("ursula")
# print(friends)                    # throws error

friends.pop(1)       # if index not passsed then by default last index
print("After removing index 1 : ",friends)

# del friends[0] use to remove element
# del friends         deletes whole list

# cleares the list
# friends.clear()
# print(friends)



# looping through the list
for x in friends:
    print(x)

# looping through index
for i in range(len(friends)):
    print(i,friends[i])

# sorting the list
friends.sort()
print("Sorted list : ",friends)

friends.sort(reverse=True)
print("Descending list : ",friends)

# reversing the list
friends.reverse()
print("Reversed list : ",friends)

# copy the list
newFriends=friends.copy()  #or newFriends=list(friends)
print("New friends : ",newFriends)

# join 2 list
# by loop and append
# by extend
# by +
newFriends=mylist2+friends
print("joined list : ",newFriends)