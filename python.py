'''
a = input("Enter first name:")
b = input("Enter last name:")
print((a+"  "+b)[::2])
'''



'''c = (input("enter no"))

print(int(c)+int(c+c)+int(c+c+c))'''

'''a = [1,2,3,4,5]
d = len(a)
for i in range(0,d):
  d=len(a)
  if a[i]%2==0:
    a.remove(a[i])
  
print(a)  '''

'''
a = []
for i in range(0,11):
  a.append(i*i*i)
print(a)
'''

'''
a=[4,5,6,3,4,5,2,1,5,4,3,0,1,2]
mini = min(a)
for i in a:
  if(min(a)==mini):
    a.remove(min(a))
  else:
    break
print("second min is ",min(a))
'''

'''
a = ['b', 'b', 'c', 'd', 'a', 'e', 'a']
b = []
j =0
for i in range(0,len(a)):
  if(b.count(a[i])==0):
    b.append(a[i])
    print("count of",b[len(b)-1],"is ",a.count(b[len(b)-1]))
'''


'''
a = "hello how are you"
b = ""
b = " "*a.count(" ") + (a.replace(" ",""))
print(b)
'''


'''
a = 'xbdcbbhcw'
b = 'dqdkxdjk'
j=0
c=""
for j in a:
  for i in b:
    if i == j:
      c=c+(i)
#c=c.split()
c=sorted(c)
c = "".join(c)
print(c)
'''

'''
a = 'hello'
b = 'world'
c = b.join(a)
print(c)
'''
'''
from collections import Counter
a = "qwertyuiovcfgdfxc vbhjkn"
b = " zxcvbhjuytrewqwertyuiujhgfdsdf"
a = Counter(a)
b = Counter(b)
c = a&b
print(c)
'''

'''
import re
a = "Beautiful, is;!!@#! better*than ugly.   "
a = re.split('[;,*?#!@.$ ]+',a)
a.remove("")
#a=" ".join(a)
print(a)
'''
'''
a = {
  'apples': 'red',
  'oranges': 'orange'
}
print(a)
a['grapes'] = 'purple'
print(a) 
a.pop('grapes')
print(a)
'''
'''
a = {}
l1 = [1,2,3]
l2 = ['a','b','c']
for i in range(0,3):
  a[l1[i]] = l2[i]
print(a)
'''
'''
l1 = ['a','b','c']
d = {}
for i in range(0,len(l1)):
  d[l1[i]]=l1[i]*3
print(d)
'''
'''
import math
l1 = [1,2,3]
d = {}
for i in range(0,len(l1)):
  d[l1[i]] = pow(l1[i],3)
print(d)
'''
'''
s = "bvhvbefhbv"
z = ""
for i in range(0,len(s)):
  if z.count(s[i])==0 :
    z = z+s[i]
print(z)
'''

'''
a = "hello python"
d = {}
for i in range(0,len(a)):
  if (i+2==len(a)):
    break
  d[a[i]] = a[i+2]
print(d)
'''
'''
a = "hellovkgjr"
print("My name is {:.2} {:.2f}".format('raj',12))
'''
'''
a = "its me again"
b = ['a','e','i','o','u','A','E','I','O','U']
count = 0
for i in b:
      count = a.count(i)+count
print(count)
'''
'''
thislist = list(("apple", "banana", "cherry"))
thislist.remove("banana")

print(thislist)
'''
'''
count = 0
string = "ThIsisCoNfUsInG"
sub_string = "is"
for i in range(0,len(string)-2):
  if string[i:i+len(sub_string)] == sub_string:
    count = count + 1
print(count)
'''
'''
a = "kjvfk fkfjwn1324   qwertyrjbhsfdhb"
b = "qkhdbvwkdjbec krkfd tdnfjy"
c=""
for i in b:
  for j in a:
    if j==i:
      c=c+i
      break
c = sorted(c)
c = "".join(c)

print(c)
#print("".join(sorted(c)))
'''
'''
a = '0'
mylist = []
for i in range(0,10):
  a = input()
  mylist.insert(i,a)
mylist=" ".join(mylist)
print(mylist)
'''
'''
a = "1234567890"
print(a[::-1])
'''
'''
l = [[1,2,3],[3,4,5]]
print(l)
'''

'''
A = []
A = input()
A = A.split(" ")
A = " ".join(A)
print(A)'''

'''
A = "vherbbhb"
A=A.find("a")
print(A)
'''

a = "fchk e"
a = a[-1:]+a[0]+a[1:-1]+"."
print(a)
