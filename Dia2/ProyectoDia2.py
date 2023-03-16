nombre = input("Cual es tu nombre? ")
ventas = float(input("Cuanto dinero hiciste en ventas? "))

comisionDeVentas = 0.13

print(f"OK {nombre}. Este mes ganaste ${round(ventas*comisionDeVentas, 2)}")