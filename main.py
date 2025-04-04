import os
mensagem = []
usuarios = []
nomeUsu = input("Digite seu nickname: ")
usuarios.append(nomeUsu)
print(usuarios)

while True:
    os.system('cls')
    if len(mensagem) >=0:
        for m in mensagem:
            print(m['nome'], "-", m['texto'])
            
    print("_________________________________________________")   
    texto= input("Mensagem: ")
    if texto == "fim":
        break
    
    mensagem.append({
        "nome": nomeUsu,
        "texto": texto
        
    })