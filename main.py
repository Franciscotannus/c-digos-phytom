import os
usuario = []
ingressos = []
print("Seja muito bem vindo ao sistema de login da balada NEW_ERA Open Bar")
criarConta = input("Você quer criar um conta? s/n: ")
if criarConta == "s":
    nome = input("Nome: ")
    senha = input("Senha: ")
    confSenha = input("Repita a senha: ")
    if confSenha == senha:
        idade = int(input("Idade: "))
        if idade <= 17:
            print("acesso NEGADO")
        else:
            print("Seja bem vindo", nome)
            tipoIngresso = int(input("QUal tipo de ingrsso você quer?"))
    else:
        print("acesso NEGADO")
        
else:
    print("Obrigado pela preferencia")
usuario.append({
    "Nome": nome,
    "Senha": senha,
    "Idade": idade
})