import os
mensagem = []
nomeUsu = input("Digite seu nickname: ")

while True:
    os.system('cls')
    if len(mensagem) >=0:
        for m in mensagem:
            print(m['nome'], "-", m['texto'])
            
    print("_________________________________________________")   
    texto= input("Mensagem: ")
    if texto == "fim":
        os.system('cls')
        break
    
    mensagem.append({
        "nome": nomeUsu,
        "texto": texto
        
    })
