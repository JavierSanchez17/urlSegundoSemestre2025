from baseConverter import Converter

c = Converter()

'''
while True:
    print("Conversiones")
    print("1. Binario a Decimal")
    print("2. Decimal a Binario")
    print("3. Decimal a Base")
    print("4. Base a Decimal")
    print("5. Base a Base")
    print("6. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        binario 
    
'''
result = c.bin_dec("1010")  # Binario a decimal
print(f"Binario a Decimal: {result}")

resultbin = c.dec_bin(10)  # Decimal a binario
print(f"Decimal a Binario: {resultbin}")

resultdec_base = c.dec_base(10, 16)  # Decimal a base 16
print(f"Decimal a Base 16: {resultdec_base}")

resultbase_dec = c.base_dec("A", 16)  # Base 16 a decimal
print(f"Base 16 a Decimal: {resultbase_dec}")

resultbase_base = c.base_base("A", 16, 2)  # Base 16 a base 2
print(f"Base 16 a Base 2: {resultbase_base}")
