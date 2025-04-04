import os

usuarios = []
ingressos = []

print("Seja muito bem vindo ao sistema de login da balada NEW_ERA Open Bar")

while True:
    criarConta = input("Você quer criar uma conta? s/n: ").lower()
    
    if criarConta == 's':
        nome = input("Nome: ")
        senha = input("Senha: ")
        confSenha = input("Repita a senha: ")
        
        if confSenha != senha:
            print("As senhas não coincidem. Acesso NEGADO")
            continue
            
        idade = int(input("Idade: "))
        if idade <= 17:
            print("Acesso NEGADO - Menor de idade")
            break
            
        print("Seja bem vindo", nome)
        
        while True:
            try:
                tipoIngresso = int(input("Qual tipo de ingresso você quer? 1:basico, 2:basico+, 3:premium, 4:premium+: "))
                if tipoIngresso not in [1, 2, 3, 4]:
                    print("Opção inválida. Tente novamente.")
                    continue
                    
                if tipoIngresso == 1:
                    preco_opcoes = {1: 150.00, 2: 150.00, 3: 310.00}
                elif tipoIngresso == 2:
                    preco_opcoes = {1: 180.00, 2: 180.00, 3: 360.00}
                elif tipoIngresso == 3:
                    preco_opcoes = {1: 210.00, 2: 210.00, 3: 430.00}
                elif tipoIngresso == 4:
                    preco_opcoes = {1: 240.00, 2: 240.00, 3: 470.00}
                    
                preco_tipo = int(input(f"Você quer: Meia estudante({preco_opcoes[1]}):1, meia idoso({preco_opcoes[2]}):2, inteira({preco_opcoes[3]}):3: "))
                
                if preco_tipo not in [1, 2, 3]:
                    print("Opção inválida. Tente novamente.")
                    continue
                    
                precoTotal = preco_opcoes[preco_tipo]
                escolha = input(f"{tipoIngresso}, {precoTotal}: Você tem certeza disso? s/n: ").lower()
                
                if escolha == 's':
                    ingressos.append({
                        "tipo de ingresso": tipoIngresso,
                        "preço": precoTotal
                    })
                    
                    usuarios.append({
                        "Nome": nome,
                        "Senha": senha,
                        "Idade": idade
                    })
                    
                    print("Muito obrigado", nome, "pela preferência!")
                    break
                else:
                    print("Operação cancelada.")
                    break
                    
            except ValueError:
                print("Por favor, digite um número válido.")
                
    elif criarConta == 'n':
        print("Obrigado pela preferência")
        break
        
    else:
        print("Opção inválida. Digite 's' para sim ou 'n' para não.")
