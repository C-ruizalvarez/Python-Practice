dic = {'clave1':100, 'clave2':500}

deleted = dic.popitem()

print(deleted)
print(dic)

string = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

test = string.lstrip(",:%_#")
test2 = test.lstrip(",")

print(test2)

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)

print(conjuntos_aislados)