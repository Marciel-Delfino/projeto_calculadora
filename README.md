# Calculadora GITHUB

## Descrição
É uma calculadora simples de adição, subtração, divisão e multiplicação. 

## Como executar
Para executar a calculadora basta ter o arquivo "calculadora.sh" e o arquivo "calculadora.py" no mesmo diretório, após isso basta verificar se o arquivo tem permissão para ser executado utilizando o comando 'ls -l', se não tiver basta usar o comando 'chmod 744 calculadora.sh' ou 'chmod u+x calculadora.sh' lembrando que 'x' é de executar, assim ele podera ser executado, após isso basta utilizar o comando './calculadora.sh'

## Como funciona o código Python
- Usamos uma coleta simples de dados utilizando `float(input(...))` para os números e `input(...)` para os operadores 
- Após isso usamos if,elif e else para decidir que tipo de equação será feita dependendo do operador escolhido pelo usuário
- Após a escolha da equação utilizamos 'if' para identificar se o operador é um dos operadores válidos, se não for um operador válido não mostra o resultado, agora se o operador for válido usamos um `print` para exibir a equação e o resultado 
- Por fim usamos dois `except` para tratar possíveis erros, sendo eles `except ValueError` caso o usuário escolha números inválidos e `except ZeroDivisionError` caso o usuário tente dividir por 0
