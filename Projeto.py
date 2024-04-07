import os 

#Limpa o terminal.
os.system("cls||clear")

#solicitando dados para usuario
print("pressione qualquer tecla para continuar...")
input()
print("Começando excutar!")

nome=input("Digite seu nome:")
idade=int(input('Digite a sua idade:'))
for i in range(5):
    print(i)
nota=float(input('digite sua nota:'))
print(f"Nome:{nome}")
print(f"idade:{idade}")
print(f"nota:{nota}")
