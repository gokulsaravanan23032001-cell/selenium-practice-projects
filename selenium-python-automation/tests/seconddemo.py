#variables in python and data types

gokul=5        #integer
goku="a"       #character
gok="tester"   #string
zogo=20.5      #float
print(gokul)
print(type(gokul))
print(goku)
print(type(goku))
print(gok)
print(type(gok))
print(zogo)
print(type(zogo))

#multiple values to multiple variables
a,b,c=1,2,3
print(a)
print(b)
print(c)
#one vlue to multiple variables
x=y=z="gojo"
print(x)
print(y)
print(z)

print("******************")

#list ,it can be altered inside square brackets(mutable)
mylist=["apple","banana","grapes",1,0.3,20.5]
print(mylist)
mylist[2]="orange"  #change values
mylist.insert(2,"kiwi")
mylist.append("mango")
veggies=["tomato",2,"onion",10.8,8]
mylist.extend(veggies)
print(mylist)
print(mylist[1])   #access item in list
print(mylist[-3:1])
print(len(mylist))
print(type(mylist))


print("*********")

#tuples its unchangeable inside normal brackets(immutable)
tupe1=("abc",1,0.5,True,40,"male")
print(tupe1)
print(type(tupe1))
print(tupe1[-1])  #access tupel through imdex
#tuples can be altered by changing them to list and made changes and then reconvert to tuple


#set come in curly brackets

set1={"apple","rope",34,50.45}
print(set1)
print(len(set1))
print(type(set1))
set1.add("chennai")
print(set1)
set2={"goa","thai"}
set1.update(set2)
print(set1)


print("***********************")

#dictionary ordered and changeable comes in square brackets
cars={
    "brand":"benz",
    "model":"fourseats",
    "year":1999
}
print(cars)
print(len(cars))
print(type(cars))

print("******************")

#if,elif,else
k=500
l=500
if k>l:
    print("k is greater than l")
elif k<l:
    print("k is less than l")
else :
    print("k is equal to l")

print("*********************")


#while loop
i=1
while i<10:
    print(i)
    i+=1

print("*********************")


#for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
