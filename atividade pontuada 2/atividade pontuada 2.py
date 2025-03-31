import os 
os.system("clear || cls ")

soma = 0
valor_pagar = 0
valor_com_acrescimo = 0

while True: 

    print("""
    =============== MENU ========================    
    código \t prato \t\t\t valor
    1\t pizza  \t\t R$ 50,00
    2\t lasanha \t\t R$ 40,00
    3\t churrasco \t\t R$ 30,00
    4\t bife com fritas \t R$ 25,00
    5\t feijoada  \t\t R$ 20,00
    6\t hamburguer \t\t R$ 15,00
    7\t queijo coalho \t\t R$ 10,00
    """)

    opcao = int(input("Digite o numero da opção desejada: "))

    match opcao:  
        case 1:
            prato = "pizza"
            preço = 50
        case 2:
            prato = "lasanha"
            preço = 40 
        case 3:
            prato = "churrasco"  
            preço = 30
        case 4:
            prato = "bife com fritas"
            preço = 25   
        case 5:
            prato = "feijoada"
            preço = 20
        case 6:
            prato = "hamburger"
            preço = 15
        case 7:    
            prato = "queijo coalho"
            preço = 10 
            if repetir:
                soma += preço
                repetir = input("Deseja escolher outro prato ? \nDigite 'S' ou 'N' : "). lower()
                if repetir == 'N': 
                    break
        case 0:
            forma_de_pagamento = int(input("""
            1- a vista                               
            2- cartão de crédito                              
            digite a forma de pagamento: """))
            
            if forma_de_pagamento:
                 # aplicando desconto de 10%
                 desconto = soma * 0.10
                 valor_pagar = soma - desconto

            elif forma_de_pagamento:
                # aplicando acrescimo de 10%
                acrescimo = soma * 0.10
                valor_pagar = acrescimo 
                print("Valor com acrescimo de 10%: ", valor_com_acrescimo)



   