import calculadora

if __name__ == "__main__":
    num1 = float(input("ingrese un numero: "))
    num2 = float(input("ingrese otro numero: "))
    
    print(f"suma: {calculadora.suma(num1,num2)}") 
    print(f"resta: {calculadora.resta(num1,num2)}")
    print(f"multiplicacion: {calculadora.multiplicacion(num1,num2)}")
    print(f"division: {calculadora.division(num1,num2)}")

    