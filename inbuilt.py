#absolute value
var = float(input("Enter a number :"))
print('Absolute value of floating point number is:', abs(var))

#all function in lists
l1=[]
print(all(l1))

l2=[1,9,0,-3]
print(all(ele>0 for ele in l2))

l3=[1,2,3,4]
print(all(l3))

#any function

l4=[False,True,False]
print(any(l4))

l5=[1,0,-9,8]
print(any(ele>0 for ele in l5))

#ascii
print(ascii("#"))

s = "S a n j a n a"
print(ascii(s))

string='''Sanjana
Raghunath'''
print(ascii(string))

#bool()
x=bool(1)
print(x)
y=bool()
print(y)
bool(-1)
bool(0.0)
bool("string")

#chr()
num=32
print("Character value of Number is:",chr(num))

#dict()
dictionary=dict(flower="rose",fruit="banana")
print(dictionary)

#divmod()
print("5,10",divmod(5,10))
print("10,3",divmod(10,3))

#enumerate()
list1=["my","name","is"]
for i,name in enumerate(list1):
    print(f"index of {i}",{name})
print(list(enumerate(list1)))

#filter()
def odd(n):
    return n%2!=0
list1=[1,2,3,4]
list2=filter(odd,list1)
print(list(list2))









