#Tabalho Bimestral de Programação Orientada a Objetos
#Professora: Camila Carolina Salgueiro Serrao
#Aluna: Maria Luiza Rodrigues da Silva;
from classe import SistemaDeCadastro
from professor import Professor
from professor import Chaveamento
from funçoes import *
import stdiomask


chaveamento_instance = Chaveamento(nome="Chaveamento Manager")
while True:
  print("")
  print("━━━━━━━ 𝐒𝐢𝐬𝐭𝐞𝐦𝐚 𝐝𝐞 𝐂𝐚𝐝𝐚𝐬𝐭𝐫𝐨 ━━━━━━━")
  print("\nMenu:")
  print(" 1. Cadastrar Capitão de Equipe")
  print(" 2. Cadastrar Aluno")
  print(" 3. Exibir Cadastro")
  print(" 4. Acesso de Professor")
  print(" 5. Sair do sistema de cadastro")
  opcao = int(input("Opção: "))
  if opcao == 1:
    cadastro_capitao()
  elif opcao == 2:
    cadastro_aluno()
  elif opcao == 3:
    exibir_cadastro()
    exibir_cadastro2()
  elif opcao == 4:
    print("\n━━━━━━━ 𝐀𝐜𝐞𝐬𝐬𝐨 𝐝𝐨 𝐏𝐫𝐨𝐟𝐞𝐬𝐬𝐨𝐫 ━━━━━━━")
    print(" 1. Login")
    print(" 2. Cadastrar novo Professor")
    escolha_prof = int(input("Escolha: "))
    if escolha_prof == 1:
      matricula = input("Digite sua matricula: ")
      senha = stdiomask.getpass("Digite sua senha: ", mask="•")
      professor_instance = Professor.obter_professor(matricula, senha)
      if professor_instance is not None:
        if SistemaDeCadastro.autenticar(senha,professor_instance.senha):
          print("Bem vindo, Professor!")
          print("")
          menu_prof(professor_instance, chaveamento_instance)
        else:
         print("senha e/ou matricula incorreta")
      else:
        print("professor não encontrado")
    elif escolha_prof == 2:
      nome = input("Digite seu nome completo: ")
      email = input("Digite seu email: ")
      matricula = input("Digite sua matricula: ")
      senha = stdiomask.getpass("Digite uma senha: ", mask="•")      
      novo_prof = Professor(nome, email, matricula, senha)
      SistemaDeCadastro.cadastrar_professor(novo_prof)
      print("Professor cadastrado com sucesso!")
      print("")
      menu_prof(novo_prof, chaveamento_instance)
  elif opcao == 5:
    print("Saindo do sistema...")
    break
  else:
    print("Opção inválida. Por favor, tente novamente.")
