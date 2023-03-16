mi_set = set([1,2,3,4,5])

print(type(mi_set))
print(mi_set)

otro_set = {1,2,3}

print(type(otro_set))
print(otro_set)

set_repetido = {1,1,1,2,2,3,3,4,4,5,5}
print(set_repetido)

#No se pueden poner listas ni diciconarios dentro de un set

set_con_tuple = {1,2,3,(4,5,6,7),8,9}
print(set_con_tuple)
print(len(set_con_tuple))

print(2 in set_con_tuple)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)

print(s3)

s1.add(4)
print(s1)
s1.remove(3)
print(s1)
s1.discard(6)

s1.pop()
print(s1)

s1.clear()
print(s1)