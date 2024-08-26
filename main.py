import os

#exibir menu
def exibir_menu():
    print('1 - Ler arquivo')
    print('2 - Gravar novos dados no arquivo.')
    print('3 - Sair do Progragama')

#função para gravar novos dados
def gravar_arquivo(dados, nome, email, profissao):
    dados += f'\n\n{'-'*30}\n\nNome: {nome}\nE-mail:{email}\nPofissão:{profissao}'
    with open('arquivo.txt','w', encoding ='utf-8') as arquivo:
        arquivo.write(dados)

#função de leitura de arquivo
def ler_arquivo():
    with open("arquivo.txt",'r', encoding = 'utf-8') as arquivo:
        dados = arquivo.read()
    return dados



#programa princial
if __name__ == '__main__':
    while True:
        dados = ler_arquivo()
        exibir_menu()
        opcao = input('Opção desejada: ')
        match opcao:
            case '1':
                print(f'\n{dados}\n')
                continue
            case '2':
                print('NOVO CADASTRO:\n')
                novo_nome = input('Informe o nome do novo usuário: ')
                novo_email = input('Informe o e-mail do novo usuário: ')
                nova_profissao = input('Informe a a profissão do novo usuário: ')
                gravar_arquivo(dados, novo_nome, novo_email, nova_profissao)
                continue
            case '3':
                print('Programa finalizad.')
                break
            case _:
                print('Opção inválida')
                continue