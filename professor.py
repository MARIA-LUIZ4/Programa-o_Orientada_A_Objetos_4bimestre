import random
from classe import Pessoa

class Professor(Pessoa):
  def __init__(self, nome, email, num_matricula, senha):
    super().__init__(nome, email, num_matricula)
    self.senha = senha
  @classmethod
  def obter_professor(cls, matricula, senha):
    #TRATAMENTO DE EXCEÇÃO TRY/EXCEPT
      try:
          with open("professores.txt", "r", encoding="utf-8") as arquivo:
              linhas = arquivo.readlines()
              for linha in linhas:
                  nome, email, num_mat, senha_armazenada = linha.strip().split(",")
                  if num_mat == matricula and senha == senha_armazenada:
                    return cls(nome, email, num_mat, senha)
      except FileNotFoundError:
          print("Erro ao abrir o arquivo")
      return None
    #O método obter_professor é responsável por procurar um professor no arquivo "professores.txt" com base na matrícula e senha fornecidas e retornar uma instância da classe Professor se encontrar uma correspondência.
    #Esta parte foi feita para verificar a autenticidade de um professor durante o login no sistema.
  #O professor pode alterar, remover e/ou adicionar um aluno e/ou capitão, dependendo da escolha do professor.
  def adicionar(self, tipo, obj):
    if tipo == "capitao":
        with open("capitao_cadastro.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"Curso: {obj['Curso']}, Nome Completo: {obj['Nome Completo']}, E-mail: {obj['E-mail']}, Número de Matrícula: {obj['Número de Matrícula']}, Data de nascimento: {obj['Data de Nascimento']}, Número da camisa: {obj['Número da Camisa']}\n")
    elif tipo == "aluno":
        with open("alunos_cadastrados.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"Nome Completo: {obj['Nome Completo']}, Curso: {obj['Curso']}, E-mail: {obj['E-mail']}, Número de Matrícula: {obj['Número de Matrícula']}, Data de Nascimento: {obj['Data de Nascimento']}, Número da Camisa: {obj['Número da Camisa']}\n")

  def remover(self, tipo, obj):
    if tipo == "capitao":
        with open("capitao_cadastro.txt", "r+", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            arquivo.seek(0)
            for linha in linhas:
                if obj['E-mail'] not in linha:
                    arquivo.write(linha)
            arquivo.truncate()
    elif tipo == "aluno":
        with open("alunos_cadastrados.txt", "r+", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            arquivo.seek(0)
            for linha in linhas:
                if obj['E-mail'] not in linha:
                    arquivo.write(linha)
            arquivo.truncate()
  def modificar(self, tipo, obj_original, obj_modificado):
    self.remover(tipo, obj_original)
    self.adicionar(tipo, obj_modificado)
  def visualizar_inscricoes(self):
    #TRATAMENTO DE EXCEÇÃO TRY/EXCEPT
    try:
        with open("capitao_cadastro.txt", "r", encoding="utf-8") as arquivo:
            cadastros = arquivo.readlines()
            for cadastro in cadastros:
                print(cadastro.strip())
        with open("alunos_cadastrados.txt", "r", encoding="utf-8") as arquivo:
            alunos = arquivo.readlines()
            for aluno in alunos:
                print(aluno.strip())
    except FileNotFoundError:
        print("Erro ao abrir o arquivo!")

#OBSERVAÇÃO: Eu não consegui fazer a classe jogos
#Não achei necessário fazer a classe equipes já que eu mudei a forma como o chaveamento funciona.
#O chaveamento funciona da seguinte maneira:
#O def carregar_capitaes é chamado para obter informações sobre os capitães das equipes a partir do arquivo "capitao_cadastro.txt".
#Depois, é verificado se há pelo menos 6 equipes disponíveis para realizar o chaveamento. Se o número de equipes for insuficiente, uma mensagem é exibida, e o processo é interrompido.
#As equipes são agrupadas por curso em um dicionário chamado equipes_por_curso, onde a chave é o nome do curso e o valor é uma lista de equipes daquele curso.
#A classe itera sobre as equipes, que foram embaralhadas aleatoriamente, e agrupa elas em chaves de forma aleatória. 
#Para cada iteração, um contador (i) é incrementado, criando uma chave única composta pelo número da chave e pelo nome do curso associado. 
#Por fim, é imprimido na tela as chaves criadas, mostrando o número e nome do curso associado a cada chave, assim como as equipes que pertencem a essa chave. 
#Então, basicamente, o sorteamento das chaves é baseado nos capitães escritos no arquivo txt.
#E o nome das equipes é o curso que o capitão coloca em seu arquivo txt.
#E essa é uma estrutura completamente diferente do que eu estava pensando em fazer anteriormente, porém foi o que deu certo para mim.

class Chaveamento:
  def __init__(self, nome: str):
    self.professor_logado = False
    self.chave = None
    self.chaves = {}
    self.equipes = []
    self.rodada_atual = 1
  def carregar_capitaes(self):
    try:
        with open("capitao_cadastro.txt", 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                capitao_info = linha.strip().split(", ")
                if len(capitao_info) == 6:
                    nome_curso, nome_completo, email, num_matricula, _, num_camisa = capitao_info
                    capitao = {"Curso": nome_curso,}
                    self.equipes.append(capitao)
                else:
                    print(f"Dados inválidos na linha: {linha}")
    except FileNotFoundError:
        print("O arquivo de capitães não foi encontrado.")
  def sortear_chaves(self):
    self.carregar_capitaes()
    if len(self.equipes) < 6:
        print("Não há capitães suficientes para realizar o chaveamento. Tente Novamente.")
        return
    self.chaves = {}
    random.shuffle(self.equipes)
    equipes_por_curso = {}
    for equipe in self.equipes:
        curso = equipe['Curso']
        if curso not in equipes_por_curso:
            equipes_por_curso[curso] = []
        equipes_por_curso[curso].append(equipe)
    for i, (curso, equipes_curso) in enumerate(equipes_por_curso.items(), start=1):
        chave = f"Chave {i} - {curso}"
        print(f"{chave}: {equipes_curso}")
        self.chaves[chave] = equipes_curso
  def criar_chave(self):
    if not self.professor_logado:
      return
    self.carregar_capitaes()
    if len(self.equipes) >= 6:
      self.chave = []
      capitao_disponiveis = self.equipes.copy()
      while capitao_disponiveis:
        capitao1 = random.choice(capitao_disponiveis)
        capitao_disponiveis.remove(capitao1)
        capitao2 = random.choice(capitao_disponiveis)
        capitao_disponiveis.remove(capitao2)
        self.chave.append((capitao1, capitao2))
        print("Chave criada com sucesso.")
    else:
      print("Não há capitães suficientes para realizar o chaveamento. Tente Novamente.")
 
  def chave_criada(self):
    return self.chave is not None