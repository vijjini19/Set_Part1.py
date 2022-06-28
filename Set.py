'''set data type
set is represented by { } with elements inside it but we cannot represented an empty set.
if we keep an empty set {} then it will be called as dictionary.
it contain several datatypes inside it but it cannot contain a set or list  in it.
set is mutable,modifications can be made.
i.e we can add or remove elements from it.
but frozen set is immutable , we cannot add or remove elements in it.
set is unordered.
'''
# m={}
# print(m,type(m))    #{} <class 'dict'>

# n={23,45,67}
# print(n[1])   #TypeError: 'set' object is not subsciptable


# a={2,3.4,"hey",(3,6)}
# print(a,type(a))  #{2, 3.4, 'hey', (3, 6)} <class 'set'>

# n={5,3.6,"hi",(6,7),[3,6]}
# print(n)    #TypeError: unhashable type: 'list'

# a={2,3.4,"hey",(3,6),{3,5}}
# print(a)   #TypeError: unhashable type: 'set'

# print(dir(set))

'''add'''
# n={2,4.5,'hi',(3,8)}
# m=4,78,9.8,'hi'
# n.add(99)
# print(n)     #{2,99,'hi',4.5,(3,8)}
# n.add(m)
# print(n)    #{'hi',2,(4,78,9.8,'hi),4.5,(3,8)}


'''clear'''
# m={67,8.9,"hey"}
# m.clear()
# print(m)     #set()

'''discard'''
# z={23,66,87,98,65}
# z.discard(87)
# print(z)  #{65,66,98,23}
# z.discard(22)
# print(z)   #{65,66,98,87,23}

'''intersection'''
# a={1,2,3,4}; b={5,6,7,8}; c={4,5,6,1}
# print(a.intersection(b))  #set()
# print(a.intersection(c))   #{1,4}
# print(b.intersection(c))  #{5,6}

'''union'''
# a={23,56,78}; b={56,67,32}; c={23,78}
# print(a.union(b))  #{32,67,23,56,78}
# print(a.union(c))  #{23,56,78}

'''update'''
# a={2,6,8}; b={7,9,0}; c={2,6}
# a.update(c)
# print(a)  #{2,6,8}
# b.update(c)
# print(b)  #{0,2,6,7,9}

'''difference'''
# a={2,3,4,5,6}
# b={2,3,8,9}
# print(a-b)  #{4,5,6}
# print(b-a)  #{8,9}

'''pop'''
# m={2,3,4,5,6,7}
# m.pop()
# print(m)  #{3,4,5,6,7}

'''disjoint'''
# A = {2,3,4,5,6}
# B = {9,0}
# C={2,3,4}
# print('Are A and B disjoint?', A.isdisjoint(B))  #Are A and B disjoint? True
# print(A.isdisjoint(C))  #False

'''subset'''
# A={2,3,4,}
# B={9,0}
# C={2,3,4,5}
# print(A.issubset(B))  #False
# print(A.issubset(C))  #True