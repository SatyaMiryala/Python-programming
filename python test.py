#1. Collect a string from the user and reverse it like below
"""
input1 = input("Please enter the string")

c = str()
word = input1[::-1]
#print(word)
for i in word.split():
    a = len(i)
    b = i+str(a)
    c =c +" " + b
print(c)

#2. Collect an integer from the user, convert it into binary number without using an inbuilt function (Don't use inbuilt function bin)
def bin_fun(input_2):
    if int(input_2) >= 1:
        bin_fun(int(input_2) // 2)
    print(int(input_2) %2, end = "")
    #res1 = bin(int(input_2))
    #res1 = int(input_2) % 2
    #return res1
    
input_2 = input("Please enter a number")
print(bin_fun(input_2))
"""

#3. Collect two strings from the user and identify whether both are anagrams or not

input_1 = input("Please enter the first string")
input_2 = input("please enter the second string")

len1 = int(len(input_1))
len2 = int(len(input_2))
if len1 == len2:
    sort1 = sorted(input_1.lower())
    sort2 = sorted(input_2.lower())
    if sort1 == sort2:
        print("given two inter are anagrams")
    else:
        print("Given two strings are not anagrms")
else:
    print("Given two strings are not anagrms")
'''
#4. Collect two list from user. Identify number of common elements between them
def com_ele(li1, li2):
    a = set(li1)
    b = set(li2)
    if (a & b):
        return a&b
    else:
        return ("no common elements")
        
li1 = list(input("Please enter the elements")) 
li2 = list(input("plese enter the elements"))

print(com_ele(li1, li2))

#5. Collect a string from user and identify number of pairs of vowels in it.

def vowel_count(str1):
    a = 0
    vowels =set("aeiou")
    for i in str:
        if i in vowels:
            a += 1
        else:
            print("no vowels")
    print("no of vowels:", a)
str1 = input("Please enter the string")
print(vowel_count(str1))
'''
