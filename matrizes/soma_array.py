## Exercício 1: Soma de Array
##- **Descrição**: Escreva uma função que recebe um array de números e retorna a soma de todos os elementos.

##- **Regra**: Não utilize funções de bibliotecas que façam a soma diretamente

##- **Input**: [1, 2, 3, 4, 5]
##- **Output**: 15
##- **Input**: [-1, 1, 0, 5, -5]
##- **Output**: 0



numlist1 = [1, 2, 3, 4, 5]
numlist2 = [-1, 1, 0, 5, -5]

listSum = 0

for number in numlist1:
  listSum += number


print(f"{listSum}")

listSum = 0

for number in numlist2:
  listSum += number

print(f"{listSum}")
