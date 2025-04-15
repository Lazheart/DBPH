def suma(a, b):
    """Realiza la suma de dos números"""
    return a + b


def resta(a, b):
    """Realiza la resta de dos números"""
    return a - b


def multiplicacion(a, b):
    """Realiza la multiplicación de dos números"""
    return a * b


def division(a, b):
    """Realiza la división de dos números con manejo de error"""
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: División por cero"


def main():
    print("Calculadora en línea de comandos")
    print("Operaciones disponibles: +, -, *, /")
    print("Presione 'c' para borrar, Enter para calcular")
    print("Presione 'q' para salir")

    operacion_actual = ""

    while True:
        entrada = input(operacion_actual or "> ")

        if entrada.lower() == 'q':
            break

        if entrada.lower() == 'c':
            operacion_actual = ""
            continue

        if not entrada and operacion_actual:
            try:
                # Evaluar la operación completa
                if '+' in operacion_actual:
                    numeros = operacion_actual.split('+')
                    num1 = float(numeros[0].strip())
                    num2 = float(numeros[1].strip())
                    print(f"Resultado: {suma(num1, num2)}")

                elif '-' in operacion_actual:
                    numeros = operacion_actual.split('-')
                    num1 = float(numeros[0].strip())
                    num2 = float(numeros[1].strip())
                    print(f"Resultado: {resta(num1, num2)}")

                elif '*' in operacion_actual:
                    numeros = operacion_actual.split('*')
                    num1 = float(numeros[0].strip())
                    num2 = float(numeros[1].strip())
                    print(f"Resultado: {multiplicacion(num1, num2)}")

                elif '/' in operacion_actual:
                    numeros = operacion_actual.split('/')
                    num1 = float(numeros[0].strip())
                    num2 = float(numeros[1].strip())
                    resultado = division(num1, num2)
                    print(f"Resultado: {resultado}")

                operacion_actual = ""

            except ValueError:
                print("Error: Ingrese una operación válida")
                operacion_actual = ""
            except Exception as e:
                print(f"Error inesperado: {str(e)}")
                operacion_actual = ""
        else:
            operacion_actual += entrada


if __name__ == '__main__':
    main()