# #first line in python
# print("hello bro")
# print (1+1)
# #assigning helloo to variable greetings 
# greetings = "hello bro"
# print(greetings)
# #python is case sensitive and indent sensitive
# sechR = (3600*3600)
# print(sechR)
# x = 2
# y = 2
# print(x)
# print(y)

# phrase = "hello bro"
# type(phrase)
# #the first delimeter quotes the other quotes can bve used inside 
# msg = 'she say,"she flirt with her boyfriend bredin"'
# print(msg)
# #escape the error if you use the same quotes as delimeter using a backlash\
# msg2 = "she say,\"she flirt with her boyfriend bredin\""
# print(msg2)

# alpha = len("abcdefghijklmnopqrstuvwxyz")


# print(alpha)

# #extremely long strings written with backlashes \
# #conctination,slicingand indexing
# #concatination
# msc = "davido"
# act = "released"
# alb = "timeless"
# magix = msc +  " " + act + alb
# print(magix)
# userinput = "google"
# lastel = len(userinput)-1
# ls = userinput[lastel]
# print(ls)
# n = ""
# user = "Tell Me Your Password"


# #kl = int(input())
# #kj = int(input())
# #p = (kl+kj)


# #print(f"the sum of{kl}and{kj}is{p}")
# k = int(20)

# print("adam aint no Ho @" + str(k) ,sep="$")
# a = 3
# a *=3
# print(a)

# k=input([])

# x = 'wet'
# if x is ('wet'):
#     print("its really wet")

# marks = [90, 100, 95, 30, 20, 55, 60] 

# highest = marks[0]
# for i in marks:
#     if i > highest:
#         highest = i
#         print(highest)
#         b = max(marks)

#loops 
#while loop
# i = 0
# while i <= 10 :
#     if i % 2 == 0:
#      print(i ,sep="\n")
    
#     i+= 1
    
# i = 1
# add  =  0
# while i<=10:
#     add +=i
#     i +=1
# print(add)

#range function
# b=range(5)
# print(b)

# b = list(range(5))
# print(b)

# b = list(range(1,5))
# print(b)

# b = list(range(1,10,2))
# print(b)
# #forlloop
# n = int(input())

# for i in range(1,11):
#     b = i * n
#     print(b)   

# for i in range(1,5):
#     for i in range(1,5):
#      print("*",end="" )
#     print('')

# for i in range(1,5):
#     for j in range(i):
#         print("+",end="")
#     print()

#break continue and pass

# n = 'rahul'
# k = len(n)-1
# p = n[k]
# print(p)
 
 #data structures
 #slicing lists
# i = [2,4,6,7,9]
# k = i[::-1]
# # print(k)
# phone = [1,2,3,4,5]

# name = ['letra', 'petty', 'food','gof']
# name.extend(phone)
# name.append(2)
# print(name)
#heterogeneous lists
# i = [1,'goose',1.3]
# for x in i:
# #     print(x)
# k1 = [1,2,3,4]
# k2 = [5,6,7,8]
# k3 = [9,11,23,45]
# k = [k1,k2,k3]

# for i in k:
#  for j in i:
#      print(j)

# l =[]
# for i in range(10):
#     l.append(i)
# print(l)

# pop = int(0)
# l = []
# for i in range(20):
#     l.append(i)

# for k in l:
#     pop +=k
# print(pop)

# t = ([1,2,3], 'bro')
# k = t[0]
# p = t[1]
# print(p)

#dictionaries
fruits = {
    'apples' : 20,
    'mangoes' :10,
    'oranges':5
}

e = '34'
k = [34:{}]

fruits = dict(zip(e,k))
print(fruits)
# name = ['ketra','john','bomu']
# price = [233,445,666]
# stu = dict(zip(name,price))
# print(stu['ketra'])
# print(stu.get('john'))

# stu['ketra'] = {'short':5000,'mediium':10000}
# #updating dictionary with one item
# stu['babra'] = 567
# #updating dictionary with another dictionary or multiple elements
# stu.update(fruits)
# #deleting item  from dictionary
# stu.pop('ketra')
# stu.popitem()
# ('john',445)
# stu.popitem()
# ('babra',567)
# print(stu)

# del fruits
# print(stu)


#acess elements in a dictionary
# for i in fruits:
#     print(i)
    
# for i in fruits:
#     print(i,fruits[i])   

# for key, value in fruits.items():
# #  print(key,value)
# fruits.keys()
# print(fruits.keys())
# name = "samir aktar"

# freq = {}
# for i in name:
#     if i not in freq:
#         freq[i] = 1
#     else:
#         freq[i]+=1
# print(freq)
# freq.pop('s')
# freq.popitem()
# print(freq)

#dictionary challenge
# name = input()
# dk = {}

# for i in name:
#     if i not in dk:
#         dk[i] = 1
#     else:
#         dk[i] += 1
# print(dk)

# #sets
# s = set()
# s =  {1,2,3,1,2,4,5,1,2}
# s.add(8)

# name = 'samir'
# s.update(name) 
# s.remove("a")
# print(s)

#intersetion
# python = {'ironman','hulk','spidy','bro'}
# java = {'ironman','harrypotter','antman'}

# print(python.difference(java))

# sent = 'be the change you see in the world'

# lst = sent.split()
# s = set(lst)
# print(s)

#defining a function
# def greet():
#     print ('Halo bro')
    
# greet()

# def greet(pk):
#     print("halo bro",pk)
    
# greet("avenger")

# def add(x,y):
#     z = x+y
#     print(z)
# add(5,6)

# def pvn(g):
#     if g % 2 == 0:
#         print('even number')
#     else:
#         print('not even')
        
# h = int(input())
# pvn(h)
# list = []
# def pvn(lists):
    
#  for i in range(10):
#     if i % 2 == 0:
#      lists.append(i)
#      print(lists)
       
#     else:
#         print('not even')
        
# pvn(list)

# #using return 
# def add(a,b):
#     c = a + b
#     return c



# k = add(9,10)
# print(k)

#returning multiple values 
def jaja(r,t,g):
    return r,t,g

a,b,c = jaja('adam','katamba','hakeam')
print(a,b,c)
   
