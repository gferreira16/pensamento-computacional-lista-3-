'''
lista de exercício 3 pensamento computacional:

1 - Métodos de Lógica Dedutiva e Indutiva

Explique a diferença entre o método dedutivo e o método indutivo. Em seguida, escreva um código que utilize lógica dedutiva para verificar se um número é par ou ímpar, e um código com lógica indutiva que faz uma lista dos números ímpares de 1 até 100:

Método Dedutivo:

O método dedutivo parte de uma regra ou princípio geral para chegar a conclusões específicas.
Método Indutivo:
O método indutivo parte de casos específicos para formar uma regra geral.
'''
#código dedutivo:
def verificar_par_ou_impar(numero):
        if numero % 2 == 0:
        return f"{numero} é par."
    else:
        return f"{numero} é ímpar."


print(verificar_par_ou_impar(4))  
print(verificar_par_ou_impar(7))  

#código indutivo:
def gerar_numeros_impares(limite):
        numeros_impares = []
    for numero in range(1, limite + 1):
        if numero % 2 != 0:
            numeros_impares.append(numero)
    return numeros_impares


print(gerar_numeros_impares(100))  


'''
2 - Tipos de Variáveis e Suas Funcionalidades
Descreva os tipos de variáveis que estudamos e escreva um script que exemplifique o uso de cada um, incluindo int, float, str, e bool.

nt (Inteiros):
Representam números inteiros, positivos ou negativos, sem decimais.
Exemplo: 1, -5, 42.

float (Ponto Flutuante):
Representam números com partes decimais, numeros nao inteiros.
Exemplo: 3.14, -0.001, 42.0.

str (String):
Representam cadeias de caracteres (texto). Strings são delimitadas por aspas simples ou duplas.
Exemplo: "Olá", '1234', "Python".

bool (Booleano):
Representam valores lógicos, que podem ser True (verdadeiro) ou False (falso).
Exemplo: True, False.
'''

'''
3 - Relacione Operadores com seus Significados
Relacione cada operador com sua função: <, =, >=, !=, <=, NOT, AND, >, ==, OR. Em seguida, 
escreva exemplos de código que demonstrem cada um desses operadores em uma condição prática.



Operador	Significado
<	Menor que
>	Maior que
<=	Menor ou igual a
>=	Maior ou igual a
=	Atribuição (atribui valor a uma variável)
==	Igualdade (compara se dois valores são iguais)
!=	Diferente (compara se dois valores são diferentes)
NOT	Negação (inverte o valor lógico)
AND	E lógico (verdadeiro se ambas condições forem verdadeiras)
OR	Ou lógico (verdadeiro se pelo menos uma condição for verdadeira)
'''
# Operadores relacionais e lógicos em condições práticas

# Exemplo 1: Comparação com <, >, <=, >=
idade = 18
if idade < 20:
    print("Você é jovem!")  # Menor que
if idade >= 18:
    print("Você é maior de idade!")  # Maior ou igual a

# Exemplo 2: Igualdade e diferença com ==, !=
senha = "abc123"
if senha == "abc123":
    print("Acesso permitido!")  # Igualdade
if senha != "senhaerrada":
    print("Senha correta, continue.")  # Diferença

# Exemplo 3: Operadores lógicos NOT, AND, OR
is_estudante = True
has_cartao = False

# NOT: Inverte o valor lógico
if not has_cartao:
    print("Você precisa de um cartão para entrar.")

# AND: Verdadeiro se ambas condições forem verdadeiras
if is_estudante and idade < 25:
    print("Você tem direito ao desconto estudantil.")

# OR: Verdadeiro se pelo menos uma condição for verdadeira
if has_cartao or is_estudante:
    print("Você pode acessar a biblioteca.")

# Atribuição com =
nota = 9.5  # Atribuindo um valor à variável
print(f"Sua nota foi {nota}.")



'''
4 - Estruturas Condicionais
Explique o que são estruturas condicionais e crie um exemplo em Python com uma aplicação prática de if,
elif e else para verificar a idade e o sexo de uma pessoa e determinar se ela é menor de idade, adulto ou idoso, com base em intervalos de idade.
'''

'''
Estruturas condicionais são blocos de código que executam diferentes instruções com base em uma condição lógica.
Em Python, as estruturas condicionais principais são:
'''
'''
if: Avalia uma condição e executa o bloco associado se a condição for verdadeira.
elif: Permite verificar múltiplas condições alternativas (abreviação de "else if").
else: Define o bloco de código a ser executado se nenhuma das condições anteriores for verdadeira.
'''

def classificar_pessoa(idade, sexo):
    # Usando estruturas condicionais
    if idade < 18:
        categoria = "menor de idade"
    elif 18 <= idade < 60:
        categoria = "adulto"
    else:
        categoria = "idoso"

    if sexo.lower() == "masculino":
        return f"Você é um {categoria} do sexo masculino."
    elif sexo.lower() == "feminino":
        return f"Você é uma {categoria} do sexo feminino."
    else:
        return f"Você é um(a) {categoria} de gênero não especificado."

print(classificar_pessoa(16, "masculino"))  # Menor de idade
print(classificar_pessoa(25, "feminino"))   # Adulto
print(classificar_pessoa(70, "outro"))      # Idoso




'''
5 - Avaliação de Afirmativas

Considere um trecho de código semelhante ao das questões, onde o programa toma decisões com base na idade e sexo. 
Codifique o exemplo e avalie se as afirmações dadas são verdadeiras ou falsas.
''



def avaliar_pessoa(idade, sexo):
    if idade < 18:
        if sexo.lower() == "masculino":
            return "Você é um menino menor de idade."
        elif sexo.lower() == "feminino":
            return "Você é uma menina menor de idade."
        else:
            return "Você é menor de idade e de gênero não especificado."
    elif 18 <= idade < 60:
        if sexo.lower() == "masculino":
            return "Você é um homem adulto."
        elif sexo.lower() == "feminino":
            return "Você é uma mulher adulta."
        else:
            return "Você é adulto(a) de gênero não especificado."
    else:
        if sexo.lower() == "masculino":
            return "Você é um homem idoso."
        elif sexo.lower() == "feminino":
            return "Você é uma mulher idosa."
        else:
            return "Você é idoso(a) de gênero não especificado."

print(avaliar_pessoa(16, "masculino"))  # Menino menor de idade
print(avaliar_pessoa(25, "feminino"))   # Mulher adulta
print(avaliar_pessoa(70, "outro"))      # Idoso(a) de gênero não especificado




'''
6 - Tabelas Verdade Booleanas

Preencha tabelas verdadeiras booleanas com as expressões A || (B && C), !A && B && C, !(A && B && !C). 
Use variáveis em Python para validar cada expressão e comparar os resultados.
'''

'''
codigo da tabela:
valores = [(False, False, False), (False, False, True),
           (False, True, False), (False, True, True),
           (True, False, False), (True, False, True),
           (True, True, False), (True, True, True)]

print(f"{'A':^5} {'B':^5} {'C':^5} {'A || (B && C)':^15} {'!A && B && C':^15} {'!(A && B && !C)':^15}")

for A, B, C in valores:
    expr1 = A or (B and C)
    expr2 = not A and B and C
    expr3 = not (A and B and not C)
    print(f"{A!s:^5} {B!s:^5} {C!s:^5} {expr1!s:^15} {expr2!s:^15} {expr3!s:^15}")


ao executar esse sera o resultado:
  A     B     C   A || (B && C)    !A && B && C    !(A && B && !C)
False False False      False           False            True      
False False True       False           False            True      
False True  False      False           False            True      
False True  True       True            True             True      
True  False False      True            False            True      
True  False True       True            False            True      
True  True  False      True            False            True      
True  True  True       True            False            False     
'''




'''
7 - Escrita de Tabela Verdade para Proposições

Dadas as proposições: “Está chovendo”, “Está fazendo sol”, e “Hoje temos avaliação G1”. 
Escreva a tabela verdade para a proposição "Teremos avaliação G1 caso faça chuva ou faça sol".
'''



valores = [(False, False, False), (False, False, True),
           (False, True, False), (False, True, True),
           (True, False, False), (True, False, True),
           (True, True, False), (True, True, True)]

print(f"{'P (Chovendo)':^15} {'Q (Sol)':^10} {'R (Avaliação)':^15} {'(P || Q) -> R':^15}")

for P, Q, R in valores:
    implicacao = (P or Q) <= R  # Operador condicional (P || Q) -> R
    print(f"{P!s:^15} {Q!s:^10} {R!s:^15} {implicacao!s:^15}")





8 - Maior Entre Três Números

Escreva um código que leia três números inteiros e determine o maior deles. Entregue o script em Python.



def maior_entre_tres(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print("Digite três números inteiros:")
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Terceiro número: "))

maior = maior_entre_tres(num1, num2, num3)
print(f"O maior número entre {num1}, {num2} e {num3} é: {maior}")





9 - Sistema de Elegibilidade para Empréstimos

Desenvolva um sistema que recebe a renda, pontuação de crédito e despesas mensais de um cliente. 
Com base nisso, calcula a renda líquida e determina a elegibilidade para um empréstimo com as condições dadas. 
Adicione um bônus onde o sistema também compara a parcela mensal com 30% da renda líquida.



def calcular_renda_liquida(renda, despesas):
    return renda - despesas

def verificar_elegibilidade(renda_liquida, pontuacao_credito, valor_emprestimo, meses):
    parcela_mensal = valor_emprestimo / meses
    limite_parcela = 0.3 * renda_liquida  # 30% da renda líquida

    if pontuacao_credito >= 700 and renda_liquida > 0 and parcela_mensal <= limite_parcela:
        return True, parcela_mensal
    else:
        return False, parcela_mensal

print("Sistema de Elegibilidade para Empréstimos")
renda = float(input("Digite sua renda mensal: R$ "))
despesas = float(input("Digite suas despesas mensais: R$ "))
pontuacao_credito = int(input("Digite sua pontuação de crédito (0 a 1000): "))
valor_emprestimo = float(input("Digite o valor do empréstimo desejado: R$ "))
meses = int(input("Digite o número de meses para pagamento: "))

renda_liquida = calcular_renda_liquida(renda, despesas)

elegivel, parcela_mensal = verificar_elegibilidade(renda_liquida, pontuacao_credito, valor_emprestimo, meses)

print("\nResultado da Análise:")
print(f"Renda líquida: R$ {renda_liquida:.2f}")
print(f"Pontuação de crédito: {pontuacao_credito}")
print(f"Valor da parcela mensal: R$ {parcela_mensal:.2f}")

if elegivel:
    print("Parabéns! Você é elegível para o empréstimo.")
else:
    print("Infelizmente, você não atende aos critérios para o empréstimo.")
    if parcela_mensal > 0.3 * renda_liquida:
        print("Motivo: A parcela mensal excede 30% da sua renda líquida.")
    if pontuacao_credito < 700:
        print("Motivo: Sua pontuação de crédito é insuficiente.")
    if renda_liquida <= 0:
        print("Motivo: Sua renda líquida é negativa ou zero.")








10 - Diferença entre Estruturas de Controle while e for

Explique a diferença entre while e for, e implemente um exemplo de cada para percorrer uma lista de números de 1 a 10, mostrando o quadrado de cada número.



FOR:
numeros = list(range(1, 11))

print("Usando 'for':")
for numero in numeros:
    print(f"O quadrado de {numero} é {numero ** 2}")



WHILE:
# Lista de números de 1 a 10
numeros = list(range(1, 11))
indice = 0

print("\nUsando 'while':")
while indice < len(numeros):
    numero = numeros[indice]
    print(f"O quadrado de {numero} é {numero ** 2}")
    indice += 1





11 - Funções em Python
Escreva uma função em Python para calcular a média de dois números. A função deve receber os valores como parâmetros e retornar o resultado.



def calcular_media(numero1, numero2):
    return (numero1 + numero2) / 2

# Testando a função
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

media = calcular_media(num1, num2)
print(f"A média de {num1} e {num2} é: {media}")





12 - Métodos pop e remove em Listas

Crie uma lista e demonstre a diferença entre os métodos pop e remove. Explique quando utilizar cada um.



pop:

Remove e retorna o elemento de uma lista com base no índice.
Se nenhum índice for especificado, remove o último elemento por padrão.
Útil quando você quer trabalhar com o elemento removido ou sabe a posição exata do elemento na lista.
remove:

Remove a primeira ocorrência de um valor específico na lista.
Útil quando você conhece o valor do elemento, mas não o índice.
Gera um erro (ValueError) se o valor não existir na lista


codigo:

frutas = ["maçã", "banana", "laranja", "maçã", "uva"]

print("Lista inicial:", frutas)

removido_por_pop = frutas.pop(2)  # Remove o elemento no índice 2 (laranja)
print("\nApós usar pop(2):", frutas)
print("Elemento removido por pop:", removido_por_pop)

frutas.remove("maçã")  # Remove a primeira ocorrência de "maçã"
print("\nApós usar remove('maçã'):", frutas)

ultimo_removido = frutas.pop()  # Remove o último elemento (uva)
print("\nApós usar pop() (sem índice):", frutas)
print("Último elemento removido:", ultimo_removido)





13 - Uso de break e continue em Laços

Escreva um código que itera de 1 a 10. Use break para parar o laço quando o número for igual a 5, e continue para pular o número 3. Mostre o resultado.


for numero in range(1, 11):
    if numero == 3:
        continue  #
    if numero == 5:
        break  
    print(f"Número atual: {numero}")







14 - Função para Remover Duplicados

Crie uma função remover_duplicados que receba uma lista de números e retorne uma nova lista com apenas os valores únicos, sem duplicados.




def remover_duplicados(lista):
    lista_unica = []
    for elemento in lista:
        if elemento not in lista_unica:
            lista_unica.append(elemento)
    return lista_unica

numeros = [1, 2, 2, 3, 4, 4, 5, 1, 6]
resultado = remover_duplicados(numeros)
print(f"Lista original: {numeros}")
print(f"Lista sem duplicados: {resultado}")





15 - Jogo de Adivinhação com while

Crie um jogo onde o usuário deve adivinhar um número aleatório entre 1 e 100. 
Utilize random.randint() e pare o loop quando o usuário acertar o número, exibindo uma mensagem de parabéns.




import random

def jogo_adivinhacao():
    numero_aleatorio = random.randint(1, 100)  # Gera o número aleatório
    tentativa = None  

    print("Tente adivinhar o número, entre 1 e 100.")

    while tentativa != numero_aleatorio:
        try:
            tentativa = int(input("Digite sua tentativa: "))

            if tentativa < numero_aleatorio:
                print("Muito baixo! Tente novamente.")
            elif tentativa > numero_aleatorio:
                print("Muito alto! Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido!")

    print(f"Parabéns! Você acertou o número: {numero_aleatorio}")

jogo_adivinhacao()





16 - Gerenciamento de Lista de Tarefas (To-Do List)

Desenvolva um programa que permita ao usuário adicionar, visualizar e remover tarefas de uma lista. Inclua condições para verificar se o índice de uma tarefa é válido antes de removê-la.
Esses exercícios devem ser entregues em arquivos separados de Python (.py) para cada questão ou grupo de questões, conforme o solicitado.



tarefas = []

while True:
    print("\n--- Menu de Tarefas ---")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Remover tarefa")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a nova tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada!")
    
    elif opcao == "2":
        if not tarefas:
            print("A lista de tarefas está vazia.")
        else:
            print("\nSuas tarefas:")
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa}")

    elif opcao == "3":
        if not tarefas:
            print("A lista de tarefas está vazia. Nada para remover.")
        else:
            print("\nSuas tarefas:")
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa}")
            
            try:
                indice = int(input("Digite o número da tarefa que deseja remover: "))
                if 1 <= indice <= len(tarefas):
                    tarefa_removida = tarefas.pop(indice - 1)
                    print(f"Tarefa '{tarefa_removida}' removida!")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Por favor, insira um número válido.")
    
    elif opcao == "4":
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Opção inválida. Tente novamente.")
