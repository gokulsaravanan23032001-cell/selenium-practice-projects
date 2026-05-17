"""
greeting="Welcome to python programming"
print(greeting)
InstructorName="Rahul!"
print(greeting+InstructorName)
"""
"""
age,height,favourite_color=25,5.9,"blue"
print(type(age))
print(type(height))
print(type(favourite_color))"""

# list[]
"""
values=[3,4.5,"gokul",25]
print(values[-1])
print(values[1:3])
values.insert(1,10)
print(values)
values.append(100)
print(values)
del values[2]
print(values)
values[3]="Gokul"
print(values)
"""
"""
#tuple its same as list but immutable cannot be edited ()
val=(2,"gokul",2.3,20)
print(val[1])
"""
"""
#dictionary{key:value,key:value...}
coco={2:2,"dodo":"dodo",21:"dodo","dod":2}
print(coco["dodo"])
print(coco[21])
#adding values in dictionary
doco={}
doco["loco"]=1
print(doco)
doco[4]=5
print(doco)
"""
"""
#if else
a="hello babu"
if a=="hello":
    print("correct")
else:
    print("Not correct")

b=25
if b<25:
    print("small")
else:
    print("big")
"""
"""
# for loop
gojo=[2,4,5,6]
for suku in gojo:
    print(suku*2)
print("***********")
#sum of natural numbers
summ=0
for i in range(1,7):
    summ= summ+i
print(summ)

print("***********")

for j in range(1,10,2):
    print(j)
    
"""
"""
# while loop
t=5
while t>1:
    print(t)
    t=t-1
print("******")
m = 4
while m>1:
    if  m!=2:
        print(m)
    m=m-1
print("******")
#break in while loop
l=9
while l>1:
    if l==3:
        break
    print(l)
    l=l-1
print("******")

#continue in while loop
g=15
while g>4:
    if g==11:
        g=g-1
        continue
    if g==5:
        break
    print(g)
    g=g-1
"""
def gojo():
    print("hello gojo")

gojo()
