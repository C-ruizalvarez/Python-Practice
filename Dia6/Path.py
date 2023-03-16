from pathlib import Path

base = Path.home()
guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_Familia.txt"))
guia2 = guia.with_name("La_Pedrera.txt")

print(base)
print(guia)
print(guia2)

print(guia.parent)
print(guia.parent.parent)
print(guia.parent.parent.parent)

guia3 = Path(Path.home(), "Europa")

for txt in Path(guia3).glob("**/*.txt"):
    print(txt)

guia4 = Path("Europa", "España", "Barcelona", "Sagrada_Familia.txt")
en_europa = guia4.relative_to("Europa")
en_espania = guia4.relative_to("Europa", "España")

print(en_europa)
print(en_espania)