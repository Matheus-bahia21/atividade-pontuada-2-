import os
os.system("cls || clear")

comanda = 0
contador = 0
comida= ""

while True:
    cardapio = int(input("""
Selecione o prato que deseja:
Código \t Prato \t\t Preço
1 \t Lasanha \t R$25                    
2 \t Feijoada \t R$25                     
3 \t batata frita \t R$18                     
4 \t Pizza \t\t R$23                     
5 \t strogonoff \t R$30                   
6 \t frango frito \t R$20                    
7 \t hamburguer \t R$15                
"""))   
    
    match cardapio:
        case 1 :
            comanda += 25
            contador += 1
            prato = "Lasanha"
        case 2:
            prato = "Feijoada"
            comanda += 25
            contador += 1
        case 3:
            prato =  "batata frita"
            contador += 1
            comanda += 18
        case 4:
            prato = "Pizza"
            contador += 1
            comanda += 23
        case 5:
            prato = "strogonoff"
            contador += 1
            comanda += 30 
        case 6:
            prato = "frango frito"
            contador += 1
            comanda += 120
        case 7:
            prato = "hamburguer"
            contador += 1
            comanda += 3
        case _:
            print("codigo invalido.")

    comida += prato + " "
  
    permissao = int(input("Deseja pedir mais um prato? Digite '0' para encerrar a comanda, caso queira prosseguir, digite '1': "))
    if permissao == 0:
        break

pagamento = int(input("Qual a forma de pagamento ? 1 para a vista e 2 para cartão de credito: "))
    
match pagamento:
    case 1:
        pagamento = "Á vista"
        desconto = comanda * 0.1
        desconto2 = comanda - comanda * 0.1
        print(f" Valor da comanda {comanda}")
        print(f"\nSeu desconto foi de: {desconto}")
        print(f"total a pagar : {desconto2} ")
        print(f"Forma de pagemento: {pagamento}")
    case 2:
        pagamento = "Cartão de crédito"
        acrescimo = comanda * 0.1
        acrescimo2 = comanda + (comanda * 0.1)
        print(f"\nValor total comanda {comanda}")
        print(f"Seu acrescimo foi de: {acrescimo}")
        print(f"total a pagar: {acrescimo2} ")
        print(f"Forma de pagemento: {pagamento}")
        
print(comida)