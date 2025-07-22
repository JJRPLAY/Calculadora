import os
import time

def calculadora(num1: float, num2: float, operador: str) -> float:
    result = float("nan")
  
    if operador not in ['+', '-', '*', '/']:
        print("Operador inválido. Use +, -, * ou /.\n")
        return ("nan")
    
    elif operador == '-':
        result = num1 - num2
        return result
    
    elif operador == '*':
        result = num1 * num2
        return result
    
    elif operador == '/':
        result = num1 / num2
        return result
    
    elif operador == '+':
        result = num1 + num2
        return result



if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print('Calculadora')
            print('----------------------------------\n')
            
            
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
            operando = input('Digite o operador (+, -, *, /): ')
            
            if operando not in ['+', '-', '*', '/']:
                raise ValueError('NaN Operador inválido!')
            
            else:
                if operando == '+':
                    calculadora (num1, num2, operador = '+')
                    print(f"resultado e ")
                elif operando == '-':
                    calculadora (num1, num2, operando = '-')
                elif operando == '*':
                    calculadora (num1, num2, operando = '*')
                elif operando == '/':
                    calculadora (num1, num2, operando = '/')
                    
        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)

        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2) 
            
        continuar = input("Deseja usar a calculadora novamente? (s/n): ").lower()
        if continuar != 's':
            print("Obrigado por Testar!")
            print('\nVolte sempre!\n')
            break