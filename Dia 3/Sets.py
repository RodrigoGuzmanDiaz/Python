#mi_set = set([1,2,3,4,5,1,1,2,3,])
#print(type(mi_set))
#print(mi_set)

mi_set = {1,2,(1,5),4,5}
print(len(mi_set))
print(mi_set)

s1 = {1,2,3}
s2 = {4,5,6}
s3 = s1.union(s2)
print(s3)


s1 = {1,2,3}
s1.add(4)
print(s1)

s1 = {1,2,3}
s1.remove(2)
print(s1)

s1 = {1,2,3}
s1.discard(4)
print(s1)

s1 = {1,2,3}
s1.pop()
print(s1)

s1 = {1,2,3}
s1.clear()
print(s1)
