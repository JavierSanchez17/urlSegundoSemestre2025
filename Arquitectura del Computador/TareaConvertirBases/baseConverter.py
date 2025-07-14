class Converter:
    def verify_base(self, base:int) -> bool:  # Función para verificar que la base sea mayor a 2 y menor a 16 (solamente llega a hexadecimal)
        if base < 2 or base > 16:
            raise ValueError("La base debe estar entre 2 y 16")  # Verifica si la base es binaria hasta hexadecimal
    
    def bin_dec(self, binary: str) -> int:
        return int(binary, 2)  # Converte la cadena binaria a entero binario ("cadena", base del numero respresentado en la cadena)

    def dec_bin(self, decimal: int) -> str:
        return bin(decimal).replace("0b", "")  # Con la funcion bin() se converte el decimal a binario y se reemplaza "0b" por una cadena vacia para que no aparezca en el resultado
    
    def dec_base(self, dcimal, base: int) -> str:
        self.verify_base(base)
        if dcimal == 0:  # Si el decimal es 0, retorna "0"
            return "0"
        digitos = []  # Lista para colocar los residuos o valores respectivos según la base
        while dcimal > 0:
            value = dcimal % base  # Es el residuo de la división del decimal entre la base
            if value >= 10:
                digitos.append(chr(value - 10 + ord('A')))  # Si el resultado es mayor o igual a 10  se convierte a letra (A-F)
            else:
                digitos.append(str(value))  # Si el resultado es menor a 10 se coloca así nada más
            dcimal //= base  # Se divide el decimal entre la base y se descarta el residuo
        digitos.reverse()  # Se invierte la lista
        return ''.join(digitos)  # Se convierte a texto str
    
    def base_dec(self, base_value: str, base: int) -> int:
        self.verify_base(base)
        decimal = 0  # Variable para almacenar el valor decimal
        for i, digito in enumerate(reversed(base_value)):
            if '0' <= digito <= '9':
                valor = int(digito)  # si el valor esta entre 0 y 9 se convierte a entero y se coloca en valor
            else:
                valor = ord(digito.upper()) - ord('A') + 10  # Si el valor es mayor a 9 se convierte a letra (A-F)
            decimal += valor * (base ** i)  # Se multiplica el valor por la base elevada a la posición del dígito según la formula (decimal = Σ (dígito * base^posición))
        return decimal  # Retorna el valor decimal
    
    def base_base(self, base_value: str, from_base: int, to_base: int) -> str:
        decimal_value = self.base_dec(base_value, from_base)  # Primer paso, se convierte el valor a decimal
        self.verify_base(to_base)  # Verifica que la base de destino sea válida
        return self.dec_base(decimal_value, to_base)  # Retorna el valor convertido a decimal a la base que se solicito
    