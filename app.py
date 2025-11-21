import os
import json

# Define o nome do arquivo onde os dados serão salvos
NOME_ARQUIVO = 'restaurantes.json'

def carregar_dados():
    '''Carrega os dados dos restaurantes do arquivo JSON, se ele existir. Caso contrário, retorna uma lista vazia.'''
    # Verifica se o arquivo existe
    if os.path.exists(NOME_ARQUIVO):
        try:
            with open(NOME_ARQUIVO, 'r', encoding='utf-8') as f:
                # Carrega o conteúdo do arquivo
                return json.load(f)
        except json.JSONDecodeError:
            # Retorna lista vazia se o arquivo estiver corrompido ou vazio
            return []
    # Retorna lista vazia se o arquivo não existir
    return []

def salvar_dados(restaurantes):
    '''Salva a lista atual de restaurantes no arquivo JSON.'''
    # Abre o arquivo em modo de escrita ('w') e usa encoding utf-8 para caracteres especiais
    with open(NOME_ARQUIVO, 'w', encoding='utf-8') as f:
        # Usa indent=4 para formatar o JSON de forma legível
        json.dump(restaurantes, f, indent=4, ensure_ascii=False)

# Carrega os dados na variável global (restaurantes) assim que o programa inicia
restaurantes = carregar_dados()


# --- Funções de Apresentação ---

def exibir_nome_do_programa():
    ''' Exibe o nome do programa '''
    print("""
  ______                                                  
 |  ____|                                                 
 | |__ ___  _ __   ___  _ __ ___  _   _  ___  ___  _ __  
 |  __/ _ \| '_ \ / _ \| '_ ` _ \| | | |/ _ \/ _ \| '_ \ 
 | | | (_) | | | | (_) | | | | | | |_| |  __/ (_) | | | |
 |_|  \___/|_| |_|\___/|_| |_| |_|\__, |\___|\___/|_| |_|
                                   __/ |                
                                  |___/                 
    """)

def exibir_opcoes():
    ''' Exibe as opções disponíveis no menu principal '''
    print('1. Cadastrar novo restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def exibir_subtitulo(texto):
    ''' Exibe um subtítulo com linha de separação '''
    print(texto)
    print('-' * len(texto))

def exibir_linha(tamanho=50):
    ''' Exibe uma linha de separação '''
    print('-' * tamanho)

def voltar_ao_menu_principal():
    ''' Solicita input do usuário para retornar ao menu principal '''
    input('\nDigite [ENTER] para voltar ao menu principal: ')
    main()


# --- Funções de Processamento ---

def cadastrar_novo_restaurante():
    ''' Cadastra um novo restaurante na lista e salva os dados '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input('Digite o nome da categoria do restaurante (Nome do restaurante): ')
    
    # Cria o dicionário do novo restaurante
    dados_do_restaurante = {
        'nome': nome_do_restaurante.title(), # Salva com a primeira letra maiúscula
        'categoria': categoria.title(),
        'ativo': False # Todo restaurante começa desativado
    }
    
    # Adiciona à lista
    restaurantes.append(dados_do_restaurante)
    
    # Salva os dados permanentemente
    salvar_dados(restaurantes) 
    
    print(f'O restaurante "{nome_do_restaurante.title()}" foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    ''' Exibe a lista de todos os restaurantes cadastrados '''
    exibir_subtitulo('Listando restaurantes')
    
    # Cabeçalho da tabela
    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    exibir_linha(60)
    
    if not restaurantes:
        print("Nenhum restaurante cadastrado.")
    else:
        # Itera sobre a lista de restaurantes
        for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            # Define o status (Ativado ou Desativado)
            ativo = 'ATIVADO' if restaurante['ativo'] else 'DESATIVADO'
            
            # Exibe a linha formatada
            print(f'{nome_restaurante.ljust(22)} | {categoria.ljust(20)} | {ativo}')
            
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    ''' Altera o status (ativo/desativado) de um restaurante '''
    exibir_subtitulo('Alterando estado do restaurante')
    
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ').title()
    restaurante_encontrado = False
    
    # Procura pelo restaurante na lista
    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            restaurante_encontrado = True
            # Inverte o valor booleano de 'ativo' (True vira False, e False vira True)
            restaurante['ativo'] = not restaurante['ativo']
            
            # Monta a mensagem de sucesso
            mensagem = (f'O restaurante {nome_restaurante} foi ATIVADO com sucesso!' 
                        if restaurante['ativo'] else 
                        f'O restaurante {nome_restaurante} foi DESATIVADO com sucesso!')
            
            print(mensagem)
            
            # Salva os dados após a alteração
            salvar_dados(restaurantes) 
            break
            
    if not restaurante_encontrado:
        print(f'O restaurante "{nome_restaurante}" não foi encontrado.')
        
    voltar_ao_menu_principal()

def finalizar_app():
    ''' Exibe mensagem de finalização e encerra o programa '''
    exibir_subtitulo('Finalizando app')

def opcao_invalida():
    ''' Exibe mensagem de erro e retorna ao menu principal '''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()


# --- Menu Principal ---

def main():
    ''' Função principal que gerencia o fluxo do programa '''
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa o terminal
    exibir_nome_do_programa()
    exibir_opcoes()
    
    try:
        opcao_digitada = int(input('Escolha uma opção: '))
        
        # Mapeia a opção digitada para a função correspondente
        if opcao_digitada == 1:
            cadastrar_novo_restaurante()
        elif opcao_digitada == 2:
            listar_restaurantes()
        elif opcao_digitada == 3:
            alternar_estado_restaurante()
        elif opcao_digitada == 4:
            finalizar_app()
        else:
            opcao_invalida()
    
    except ValueError:
        # Trata erro se o usuário digitar algo que não é número
        opcao_invalida()

# Inicia o programa
if __name__ == '__main__':
    main()
