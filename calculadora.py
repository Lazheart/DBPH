def suma(a, b):
    """Realiza la suma de dos números"""
    return a + b


def resta(a, b):
    """Realiza la resta de dos números"""
    return a - b


def multiplicacion(a, b):
    """Realiza la multiplicación de dos números"""
    return a * b


def main():
    print("Calculadora en línea de comandos")
    print("Presione 'c' para borrar, Enter para calcular")
    print("Presione 'q' para salir")

    while True:
        entrada = input("> ")
        if entrada.lower() == 'q':
            break
        if entrada.lower() == 'c':
            continue

        if '+' in entrada:
            numeros = entrada.split('+')
            try:
                num1 = float(numeros[0].strip())
                num2 = float(numeros[1].strip())
                print(f"Resultado: {suma(num1, num2)}")
            except ValueError:
                print("Error: Ingrese números válidos")

        elif '-' in entrada:
            numeros = entrada.split('-')
            try:
                num1 = float(numeros[0].strip())
                num2 = float(numeros[1].strip())
                print(f"Resultado: {resta(num1, num2)}")
            except ValueError:
                print("Error: Ingrese números válidos")

        elif '*' in entrada:
            numeros = entrada.split('*')
            try:
                num1 = float(numeros[0].strip())
                num2 = float(numeros[1].strip())
                print(f"Resultado: {multiplicacion(num1, num2)}")
            except ValueError:
                print("Error: Ingrese números válidos")


if __name__ == '__main__':
    main()