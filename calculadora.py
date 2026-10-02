try:
  # Coleta de dados sendo eles números e sinal da equação
  numero1 = int(input('Digite o primeiro número: '))
  sinal = input('Escolha o sinal entre: +,-,* ou /: ')
  numero2 = int(input('Digite o segundo número: '))
  # Se a equação for soma
  if sinal == '+':
    total = numero1 + numero2
  # Se a equção for subtração
  elif sinal == '-':
    total = numero1 - numero2
  # Se a equaçãp for multiplicação
  elif sinal == '*':
    total = numero1 * numero2
  # Se a equação for divisão
  elif sinal == '/':
    total = numero1 / numero2
  # Caso o sinal escolhido não seja um dos disponiveis
  else:
    print('Sinal inválido! Por favor escolha entre +, -, *, e /')
  # Soma da equação
  if sinal in ['+', '-', '*', '/']:
    print(f'{numero1} {sinal} {numero2} = {total}')
  # Caso o usuario escreva um número inválido
except ValueError:
  print('Por favor digite apenas número válidos')
  # Caso o usuario tente dividir por 0
except ZeroDivisionError:
  print('Não é possível dividir por 0')
