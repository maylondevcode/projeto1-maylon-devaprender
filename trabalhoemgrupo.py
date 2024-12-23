print("\t\t\tFICHA DE TRABALHO 2\n\n"
      # Calcular a Média
      F"Ex.1")

num1 = float(input("Insira 1º valor:\n"))
num2 = float(input("Insira 2º valor:\n"))
num3 = float(input("Insira 3º valor:\n"))
num4 = float(input("Insira 4º valor:\n"))
num5 = float(input("Insira 5º valor:\n"))
num6 = float(input("Insira 6º valor:\n"))
num7 = float(input("Insira 7º valor:\n"))

media = (num1 + num2 + num3 + num4 + num5 + num6 + num7) / 7
print(F"A média é {media:.2f}\n\n")

# calcular imc
print("Ex.2")

peso = float(input("Qual o seu peso?\n"))
altura = float(input("Qual a sua altura?\n"))
imc = peso / altura ** 2

print(F"O seu IMC é: {imc:.1f}")

# calcular o troco
print("\nEx.3")

ttl_fatura = float(input("Qual o valor total da fatura?\n"))
pagamento = float(input("Quantidade de dinheiro recebido na caixa desta compra?\n"))
troco = pagamento - ttl_fatura

print(F"O troco a receber é: {troco:.2f}€")

# Calcular área e perímetro
print("\nEx.4")

lado = float(input("Qual o tamanho do lado?\n"))
area = lado ** 2
perimetro = 4 * lado

print(F"O valor da área é {area:.2f}m e o perímetro é {perimetro:.2f}m")

# sucessor e antecessor
print("\nEx.5")

n = int(input("Digite um numero inteiro:\n"))
s = n + 1
a = n - 1

print(F"O SUCESSOR deste numero é: {s} e o ANTECESSOR é: {a}")

# valor do produto: com desconto/sem desconto
print("\nEx.6")

preco = float(input("Digite o preço do produto para ganhar o desconto DE 10% AGORA!:\n"))
desconto = preco * 0.10
desconto = preco - desconto
print(
    F"Acabou de receber um desconto de 10% e vai pagar {desconto:.2f}€, "
    F"caso não tivesse feito agora iria pagar {preco:.2f}€"
)

# calcular idade baseando no ano de nascimento e ano que estamos
print("\nEx.7")

ano_nascimento = int(input("Em que ano nasceu?\n"))
ano_atual = int(input("Em que ano estamos?\n"))
idade = ano_atual - ano_nascimento

print(F"Você tem {idade} anos em {ano_atual}")
