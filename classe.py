import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Admito ter simpatizado bastante com o try/except
#Aqui as classes aluno e cap estão quase a mesma coisa, nada muito grande foi mudado
#Mas houve mudanças
class Pessoa:
  def __init__(self, nome, email, num_matricula):
      self.nome = nome
      self.email = email
      self.num_matricula = num_matricula
class AlunoEquipe(Pessoa):
  def __init__(self, nome, email, num_matricula, curso, data_nascimento, num_camisa):
      super().__init__(nome, email, num_matricula)
      self.curso = curso
      self.data_nascimento = data_nascimento
      self.num_camisa = num_camisa
  def cadastrar_aluno(self, nome_aluno,curso_aluno, email_aluno, num_matricula_aluno, data_nascimento_aluno, num_camisa_aluno):
    #RAISE ERROR - EMAIL INVALIDO
    if not self._verificar_email(email_aluno):
      raise ValueError("O e-mail deve estar no formato do Gmail.")
      #Este trecho chama o método _verificar_email
      #Este método recebe um email como argumento e verifica se ele atende a um padrão específico.
    #RAISE ERROR - NÚMERO DE MATRÍCULA INVÁLIDO
    if len(num_matricula_aluno) != 13:
      raise ValueError("O número de matrícula deve ter exatamente 13 dígitos.")
    #Esse trecho verifica o comprimento da variável num_matricula_aluno.
    #O objetivo dessa verificação é garantir que a matrícula do aluno tenha exatamente 13 dígitos.

    with open("alunos_cadastrados.txt", "a", encoding="utf-8") as arquivo:
      arquivo.write(f"Nome Completo: {nome_aluno}, Curso: {curso_aluno}, E-mail: {email_aluno}, Numero de Matricula: {num_matricula_aluno}, Data de Nascimento: {data_nascimento_aluno}, Número da camisa: {num_camisa_aluno}\n")
      
  #ESSA FUNÇÃO TRABLAHA EM CONJUNTO COM O RAISE ERROR - EMAIL INVALIDO.
   #_verificar_email verifica se o e-mail contém o domínio "@gmail.com" e a validação com raise é acionada se essa verificação falha. 
  #Aqui, eu defini o método _verificar_email, que aceita como único argumento o email. 
  #Esse método irá verificar se o endereço de e-mail está no formato do Gmail.
  @staticmethod
  def _verificar_email(email):
      """Verifica se o e-mail é do Gmail."""
    #Aqui, eu defini um padrão de expressão regular(regex)que vai ser usado para verificar o formato do e-mail.
    #O padrão [^@]+@gmail\.com está procurando por e-mails que tenham o domínio gmail.com. 
      pattern = r"[^@]+@gmail\.com"
    #Esta linha vai verificar se o e-mail passado como argumento corresponde ao padrão definido anteriormente.
      return bool(re.match(pattern, email))

#MESMO RAISE ERROR PARA CAPITAOEQUIPE
class CapitaoEquipe(Pessoa):
  def __init__(self, nome, email, num_matricula, curso, data_nascimento, num_camisa):
    super().__init__(nome, email, num_matricula)
    self.curso = curso
    self.data_nascimento = data_nascimento
    self.num_camisa = num_camisa

  def cadastrar_capitao(self, curso_capitao, nome_capitao, email_capitao, num_matricula_capitao, data_nascimento_capitao,num_camisa_capitao):
    if not self._verificar_email(email_capitao):
      raise ValueError("O e-mail deve estar no formato do Gmail.")
    if len(num_matricula_capitao) != 13:
      raise ValueError("O número de matrícula deve ter exatamente 13 dígitos.")
    with open("capitao_cadastro.txt", "a", encoding="utf-8") as arquivo:
      arquivo.write(f"Curso: {curso_capitao}, Nome Completo: {nome_capitao}, E-mail: {email_capitao}, Número de Matrícula: {num_matricula_capitao}, Data de nascimento: {data_nascimento_capitao}, Número da camisa: {num_camisa_capitao}\n")
    lista_membros = SistemaDeCadastro.obter_lista_membros()
    #IMPLEMENTAÇÃO DE DICIONÁRIO PARA ARMAZENAR OS MEMBROS DA EQUIPE
    membros_por_curso = {}
    for membro in lista_membros:
      curso_membro = membro['Curso']
      if curso_membro == curso_capitao:
        if curso_membro not in membros_por_curso:
          membros_por_curso[curso_membro] = []
          membros_por_curso[curso_membro].append(membro)
          #IMPLEMENTAÇÃO DE LISTAS PARES PARA ARMAZENAR OS MEMBROS DA EQUIPE
    capitao = {
        "Nome Completo": nome_capitao,
        "E-mail": email_capitao,
        "Número de Matrícula": num_matricula_capitao,
        "Data de Nascimento": data_nascimento_capitao,
        "Número da Camisa": num_camisa_capitao}
    if curso_capitao in membros_por_curso:
      membros_por_curso[curso_capitao].append(capitao)
    else:
      membros_por_curso[curso_capitao] = [capitao]   
    #IMPLEMENTAÇÃO DE LISTAS PARES PARA ARMAZENAR OS MEMBROS FORMATADOS DA EQUIPE
    lista_membros_formatada = []
    for curso, membros in membros_por_curso.items():
      membros_formatados = []
      for membro in membros:
          membro_str = f"Nome Completo: {membro['Nome Completo']}, Curso: {curso}, E-mail: {membro['E-mail']}, Número de Matrícula: {membro['Número de Matrícula']}, Data de Nascimento: {membro['Data de Nascimento']}, Número da Camisa: {membro['Número da Camisa']}"
          membros_formatados.append(membro_str)
      lista_membros_curso = "\n".join(membros_formatados)
      lista_membros_formatada.append(lista_membros_curso)
    lista_membros_str = "\n\n".join(lista_membros_formatada)
    self.enviar_email_confirmacao(email_capitao, nome_capitao, lista_membros_str)
  def enviar_email_confirmacao(self, email_capitao, nome_capitao, lista_membros_str):
    email_remetente = email_capitao
    email_destinatario = "projetoum8@gmail.com"
    senha_destinatario = "cswldlepklocmidl"
    mensagem = MIMEMultipart()
    mensagem["From"] = email_remetente
    mensagem["To"] = email_destinatario
    mensagem["Subject"] = "Confirmação de Cadastro"
    texto_email = f"""
    Olá, eu sou {nome_capitao}, 
    E estou finalizando o meu cadastro como capitão da minha equipe, na modalidade vôlei de areia! 
    Segue abaixo a lista de membros inscritos na equipe:
    {lista_membros_str}
    E meu e-mail para caso algo não esteja de acordo: 
    {email_capitao}
    Obrigado!
    Atenciosamente, 
    {nome_capitao}
    """
    parte_texto = MIMEText(texto_email, "plain")
    mensagem.attach(parte_texto)
    try:
      servidor_smtp = smtplib.SMTP("smtp.gmail.com", 587)
      servidor_smtp.starttls()
      servidor_smtp.login(email_destinatario, senha_destinatario)
      servidor_smtp.sendmail(email_remetente,email_destinatario,mensagem.as_string())
      servidor_smtp.quit()
      print("Email de confirmação enviado com sucesso!")
    except smtplib.SMTPException as e:
      print("Ocorreu um erro ao enviar o email de confirmação:", str(e))
  @staticmethod
  def _verificar_email(email):
    """Verifica se o e-mail é do Gmail."""
    pattern = r"[^@]+@gmail\.com"
    return bool(re.match(pattern, email))
class SistemaDeCadastro:
  @classmethod
  def autenticar(cls, senha, senha_armazenada):
    return senha == senha_armazenada
    #O método autenticar é usado para comparar a senha fornecida com a senha armazenada
    #Se as senhas coincidirem, o método retorna True, senão, retorna False.
  @classmethod
  def cadastrar_professor(cls, professor):
    with open("professores.txt", "a", encoding="utf-8") as arquivo:
      arquivo.write(f"{professor.nome},{professor.email},{professor.num_matricula},{professor.senha}\n")
      #Este método é usado para adicionar informações de um novo professor ao arquivo "professores.txt".
      #Ele formata os dados do professor e escreve no arquivo,
      #garantindo que cada registro do professor seja separado por uma quebra de linha.
  @staticmethod
  def obter_lista_membros():
    try:
     with open("alunos_cadastrados.txt", "r") as arquivo:
       linhas = arquivo.readlines()
       membros = []
       for linha in linhas:
        campos = linha.strip().split(",")
        nome_completo = campos[0].split(":")[1].strip()
        curso = campos[1].split(":")[1].strip()
        email = campos[2].split(":")[1].strip()
        num_matricula = campos[3].split(":")[1].strip()
        data_nascimento = campos[4].split(":")[1].strip()
        num_camisa = campos[5].split(":")[1].strip()
        membro = {
           "Nome Completo": nome_completo,
           "Curso": curso,
           "E-mail": email,
           "Número de Matrícula": num_matricula,
           "Data de Nascimento": data_nascimento,
           "Número da Camisa": num_camisa
        }
        membros.append(membro)
     return membros
    except FileNotFoundError:
      return []