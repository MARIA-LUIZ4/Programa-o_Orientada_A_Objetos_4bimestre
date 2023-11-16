#Aqui tem as funções usadas para fazer o cadastro do capitão, aluno, professor.
#Quando uma opção é escolhida no main.py, a função é chamada
#Não é nada muito uau, eu só queria deixar o main.py um pouco mais organizado e limpo porque é muito satisfatório.
from professor import *
from classe import *

def cadastro_capitao():
  curso_capitao = input('Digite seu curso: ')
  nome_capitao = input('Digite seu Nome Completo: ')
  email_capitao = input('Digite seu e-mail: ')
  num_matricula_capitao = input('Digite seu número de matrícula: ')
  data_nascimento_capitao = input('Digite a sua data de nascimento(00/00/00): ')
  num_camisa_capitao = input('Digite o número da sua camisa: ')
  capitao = CapitaoEquipe(nome_capitao, email_capitao, num_matricula_capitao, curso_capitao, data_nascimento_capitao, num_camisa_capitao)
  capitao.cadastrar_capitao(curso_capitao, nome_capitao,email_capitao, num_matricula_capitao, data_nascimento_capitao, num_camisa_capitao)

def cadastro_aluno():
  nome_aluno = input('Digite seu Nome Completo: ')
  curso_aluno = input('Digite seu curso: ')
  email_aluno = input('Digite seu e-mail: ')
  num_matricula_aluno = input('Digite seu número de matrícula: ')
  data_nascimento_aluno = input('Digite a sua data de nascimento(00/00/00): ')
  num_camisa_aluno = input('Digite o número da sua camisa: ')
  aluno = AlunoEquipe(nome_aluno,curso_aluno, email_aluno, num_matricula_aluno, data_nascimento_aluno,num_camisa_aluno)
  aluno.cadastrar_aluno(nome_aluno,curso_aluno, email_aluno, num_matricula_aluno, data_nascimento_aluno, num_camisa_aluno)
  print('Aluno cadastrado com sucesso!')


def menu_prof(professor_instance, chaveamento_instance):
  
  while True:
    print("\n━━━━━━━ 𝐌𝐞𝐧𝐮 𝐝𝐨 𝐩𝐫𝐨𝐟𝐞𝐬𝐬𝐨𝐫 ━━━━━━━\n")
    print(" 1. Adicionar Aluno/Capitão")
    print(" 2. Remover Aluno/Capitão")
    print(" 3. Modificar Aluno/Capitão")
    print(" 4. Visualizar Inscrições")
    print(" 5. Realizar Chaveamento")
    print(" 6. Sair do menu do professor")
    escolha = int(input("Opção: "))
    if escolha == 1:
      tipo = input("Adicionar (aluno/capitao): ").lower()
      obj = {} 
      obj['Nome Completo'] = input("Digite o nome completo: ")
      obj['Curso'] = input("Digite o curso: ")
      obj['E-mail'] = input("Digite o e-mail: ")
      obj['Número de Matrícula'] = input("Digite o número de matrícula: ")
      obj['Data de Nascimento'] = input("Digite a data de nascimento: ")
      obj['Número da Camisa'] = input("Digite o número da camisa: ")
      professor_instance.adicionar(tipo, obj)
    elif escolha == 2:
      tipo = input("Remover (aluno/capitao): ").lower()
      email = input("Email do Aluno/Capitão para remover: ")
      obj = {'E-mail': email}
      professor_instance.remover(tipo, obj)
    elif escolha == 3:
      tipo = input("Modificar (aluno/capitao): ").lower()
      email = input("Email do Aluno/Capitão para modificar: ")
      obj_modificado = {}
      professor_instance.modificar(tipo, email, obj_modificado)
    elif escolha == 4:
      professor_instance.visualizar_inscricoes()      
    elif escolha == 5:
      chaveamento_instance.sortear_chaves()
      if chaveamento_instance.chaves:
        print("Chaves Sorteadas!")
      
    elif escolha == 6:
      break
def exibir_cadastro():
  with open("capitao_cadastro.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
      print(linha.rstrip())

def exibir_cadastro2():
  with open("alunos_cadastrados.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
      print(linha.rstrip())