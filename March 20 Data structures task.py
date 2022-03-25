#List

li1 = list()

print(li1)
print(type(li1))

li2 = []

print(li2)
print(type(li2))


val = [1,5,8,9]

val2 =[5, 6, 7, 8]

print(val + val2)

val3 = [8,9,1,5,6,7,8,1]
val.extend(val3)
print(val)
print(val.count(8))


print(len(val))
print(sum(val))
print(min(val))
print(max(val))

val4 = sum(val) / 2

val.append(90)

val5 = len(val) / 2

print(val4)
print(val5)




#Tuple

tup1 = (1,4,5,6,7,8)
tup2 = (5,6,7,8,9, "python")

tup3 = tup1 + tup2

print(tup3)
print(type(tup3))

print(tup3.index(9))

tup4 = tuple(set(tup3))

print(tup4)
print(type(tup4))

tup5 = tup3 * tup3 * tup3

print(tup5)

#SET

#Create two empty sets

set1 = {3, 5, 7}

set2 = {2, 4, 6}

print(set1)
print(type(set1))
print(set2)
print(type(set2))

#update set1 with 7,8,9,1,2,3,4,5,0

set3 = {7,8,9,1,2,3,4,5,0}
set1.update(set3)

print(set1)


#update set2 with 4,5,6,0

set4 = {4, 5, 6, 0}
set2.update(set4)
print(set2)


#remove 8 from set 1 and set 2 ==> find the inferences

set1.discard(8)
print(set1)

#discard 0 from set1 and set2

set1.discard(0)
print(set1)

set2.discard(0)
print(set2)

#check whether set2 is subset of set1 or no ?

print(set2.issubset(set1))


#check whether both have common elements are no ?

set1.intersection_update(set2)

print(set1)
#remove 8 from set 1 and set 2 ==> find the inferences

set1.discard(8)
print(set1)

#find collection of both sets ===> set1 and set2

set1.update(set2)

print(set1)



#create a dictionary
#{1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}

a = {1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}


#Extract "bobtn" from above dictionary

print(a[3][0][::2])
#Extract "arbeg" from above dictionary
print(a[3][2][-1:-6:-1])

#print all keys in dictionary and convert it into tuple

print(tuple(a.keys()))
#Find the average of all numbers available under key "2"

b = sum(a[2])

print(b)





















