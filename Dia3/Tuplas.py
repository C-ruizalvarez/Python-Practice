mi_tuple = (1,2,3,4)

print(type(mi_tuple))

t = (5,3.21,"ff")

print(mi_tuple[0])
print(mi_tuple[-2])

mi_tuple_anidado = (1,2,(10,20),4)

print(mi_tuple_anidado[2][0])

mi_tuple = list(mi_tuple)

print(type(mi_tuple))

mi_tuple = tuple(mi_tuple)

print(type(mi_tuple))

t2 = (1,2,3)

x,y,z = t2

print(x,y,z)

t3 = (1,2,3,1)

print(len(t3))
print(t3.count(1))
print(t3.index(2))