'''
----------slicling--------
start:stop:step
--->Access the elements from one position to the another position
--->range

a="pleasebe"
 #  0 1 2 3 4 5 6 7
 # -8-7-6-5-4-3-2-1
 print(a[2:7])
 print(a[1:6])
  
  
  '''
a="please be"
  #012345678--->positive indexing
  #-9-8-7-6-5-4-3-2-1---->negative indexing

print(a[2:7])
print(a[1:6])
print(a[:6])
# if there is no starting position then you need to starts from indexing point.
print(a[3:])
# if there is no ending position then you can end the entiree string upto to the deadline.
print(a[-1])
print(a[:-1])
#it will read all the elements from the starting exceptlast element
#in this last element will be removed
print(a[::1])
#it will reverse the string
c="welcome"
print(c[2:7])
print(c[2:7:2])
#start:stop:step
d="welcome to the moon"
print(d[1:10:3])
#starts at indexing 1 ends at the indexing 10 but every third element

a="apple is a fruit"
print(a[::2])
#retrive the  every second element
print(a[::3])
#retrive the every third element
'''
------------string methods------

'''
a=" elon musk "
print(a)
print(len(a))
#len()will retrive the length of the string

print(a.strip())
#strip method will remove the spaces on the both sides of the string
print(a)
print(len(a))
print(a.strip())
# it will remove the white spaces on the right side
print(a.upper())
#it will convert all the characters into upper class
print(a.lower())
#it will convert all the characters into the lower class
print(a.isupper())
#it will check whether the given string is in upper case or not
print(a.islower())
#it will check whether the given string is in lower case or not
print(a.title())
#it will makes the every first characters in everyword into the uppercase
b="welcome123"
print(b.isalnum())
print(b.isdigit())
print(b.isalpha())
print(b.isascii())
c="university"
print(len(c))

d="university123"
print(d.find("v"))
#retrive the indexing position of the particular element
print(d.rfind("v"))
#retrive the indexing position of the particular element from last/reversed
print(d.index("t"))
#retrive the indexing position of the element ---> positive indexing
print(d.rindex("t"))
#retrive the indexing position of the element from right side
print(d.count("a"))
#retrive how many times the element is there in the string
z="python class is very boring"
print(z.startswith("z"))
print(z.endswith("g"))
print(z.swapcase())
#it will swap the upper case letter to lower case letters to the upper case 
print(z.casefold())
# it will convert all the characters into lower case
