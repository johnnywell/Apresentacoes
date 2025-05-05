# SOLID: Princípios de Design Orientado a Objetos
# ------------------------------------------------

# Introdução
# ----------
# SOLID é um acrônimo que representa cinco princípios fundamentais da programação orientada a objetos:
# - S: Single Responsibility Principle (Princípio da Responsabilidade Única)
# - O: Open/Closed Principle (Princípio Aberto/Fechado)
# - L: Liskov Substitution Principle (Princípio da Substituição de Liskov)
# - I: Interface Segregation Principle (Princípio da Segregação de Interface)
# - D: Dependency Inversion Principle (Princípio da Inversão de Dependência)
#
# Estes princípios, quando aplicados corretamente, ajudam a criar código mais:
# - Manutenível
# - Escalável
# - Testável
# - Flexível

# %%
# Vamos explorar cada princípio individualmente, com exemplos práticos

# %%
# S: Princípio da Responsabilidade Única (SRP)
# ------------------------------------------
# "Uma classe deve ter apenas uma razão para mudar"

print("### Princípio da Responsabilidade Única (SRP) ###")
print("Uma classe deve ter apenas uma única responsabilidade.")

# %%
print("Exemplo Ruim - Violando SRP:")

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.dados_salvos = False
    
    def validar_email(self):
        # Valida formato do email
        return "@" in self.email and "." in self.email
    
    def salvar_no_banco(self):
        # Código para salvar no banco de dados
        print(f"Salvando {self.nome} no banco de dados...")
        self.dados_salvos = True
        return True
    
    def enviar_email_boas_vindas(self):
        # Código para enviar email
        print(f"Enviando email de boas-vindas para {self.email}...")
        return True

# Demonstração
usuario = Usuario("Ana Silva", "ana@exemplo.com")
if usuario.validar_email():
    usuario.salvar_no_banco()
    usuario.enviar_email_boas_vindas()

# %%
print("\nExemplo Bom - Aplicando SRP:")

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class ValidadorEmail:
    @staticmethod
    def validar(email):
        return "@" in email and "." in email

class RepositorioUsuario:
    @staticmethod
    def salvar(usuario):
        print(f"Salvando {usuario.nome} no banco de dados...")
        return True

class ServicoEmail:
    @staticmethod
    def enviar_boas_vindas(usuario):
        print(f"Enviando email de boas-vindas para {usuario.email}...")
        return True

# Demonstração
usuario = Usuario("Ana Silva", "ana@exemplo.com")
if ValidadorEmail.validar(usuario.email):
    RepositorioUsuario.salvar(usuario)
    ServicoEmail.enviar_boas_vindas(usuario)

# %%
# O: Princípio Aberto/Fechado (OCP)
# ------------------------------
# "Entidades de software devem ser abertas para extensão, mas fechadas para modificação"

print("\n### Princípio Aberto/Fechado (OCP) ###")
print("Classes devem estar abertas para extensão, mas fechadas para modificação.")

# %%
print("\nExemplo Ruim - Violando OCP:")

class CalculadoraDescontos:
    def calcular_desconto(self, produto, tipo_cliente):
        if tipo_cliente == "regular":
            return produto.preco * 0.05
        elif tipo_cliente == "premium":
            return produto.preco * 0.10
        elif tipo_cliente == "vip":
            return produto.preco * 0.15
        else:
            return 0

# Se quisermos adicionar um novo tipo de cliente, precisamos modificar a classe existente
# o que viola o OCP

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

# Demonstração
calculadora = CalculadoraDescontos()
produto = Produto("Laptop", 1000)
desconto_premium = calculadora.calcular_desconto(produto, "premium")
print(f"Desconto Premium para {produto.nome}: R${desconto_premium}")

# %%
print("\nExemplo Bom - Aplicando OCP:")

from abc import ABC, abstractmethod

class Cliente(ABC):
    @abstractmethod
    def obter_taxa_desconto(self):
        pass

class ClienteRegular(Cliente):
    def obter_taxa_desconto(self):
        return 0.05

class ClientePremium(Cliente):
    def obter_taxa_desconto(self):
        return 0.10

class ClienteVIP(Cliente):
    def obter_taxa_desconto(self):
        return 0.15

class CalculadoraDescontos:
    def calcular_desconto(self, produto, cliente):
        return produto.preco * cliente.obter_taxa_desconto()

# Agora podemos adicionar novos tipos de clientes sem modificar a CalculadoraDescontos
class ClienteFidelidade(Cliente):
    def obter_taxa_desconto(self):
        return 0.20

# Demonstração
calculadora = CalculadoraDescontos()
produto = Produto("Laptop", 1000)
cliente_premium = ClientePremium()
desconto = calculadora.calcular_desconto(produto, cliente_premium)
print(f"Desconto Premium para {produto.nome}: R${desconto}")

cliente_fidelidade = ClienteFidelidade()
desconto = calculadora.calcular_desconto(produto, cliente_fidelidade)
print(f"Desconto Fidelidade para {produto.nome}: R${desconto}")

# %%
# L: Princípio da Substituição de Liskov (LSP)
# -----------------------------------------
# "Objetos de uma classe derivada devem poder substituir objetos da classe base sem afetar a corretude do programa"

print("\n### Princípio da Substituição de Liskov (LSP) ###")
print("Subclasses devem ser substituíveis por suas classes base sem alterar o comportamento do programa.")

# %%
print("\nExemplo Ruim - Violando LSP:")

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def set_largura(self, largura):
        self.largura = largura
    
    def set_altura(self, altura):
        self.altura = altura
    
    def area(self):
        return self.largura * self.altura

class Quadrado(Retangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)
    
    def set_largura(self, largura):
        self.largura = largura
        self.altura = largura
    
    def set_altura(self, altura):
        self.largura = altura
        self.altura = altura

def imprimir_area(retangulo):
    retangulo.set_largura(5)
    retangulo.set_altura(4)
    # Uma função que espera um retângulo espera que a área seja 5 * 4 = 20
    print(f"Área esperada: 20, Área obtida: {retangulo.area()}")

# Demonstração
print("Usando Retângulo:")
imprimir_area(Retangulo(0, 0))

print("Usando Quadrado:")  
imprimir_area(Quadrado(0))  # Viola LSP, pois o comportamento é diferente

# %%
print("\nExemplo Bom - Aplicando LSP:")

from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def area(self):
        return self.largura * self.altura

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado * self.lado

def imprimir_area(forma):
    print(f"Área da forma: {forma.area()}")

# Demonstração
retangulo = Retangulo(5, 4)
quadrado = Quadrado(5)

print("Usando Retângulo:")
imprimir_area(retangulo)

print("Usando Quadrado:")
imprimir_area(quadrado)

# %%
# I: Princípio da Segregação de Interface (ISP)
# ------------------------------------------
# "Muitas interfaces específicas são melhores do que uma interface geral"

print("\n### Princípio da Segregação de Interface (ISP) ###")
print("É melhor ter muitas interfaces específicas do que uma interface geral.")

# %%
print("\nExemplo Ruim - Violando ISP:")

from abc import ABC, abstractmethod

class Trabalhador(ABC):
    @abstractmethod
    def trabalhar(self):
        pass
    
    @abstractmethod
    def comer(self):
        pass
    
    @abstractmethod
    def dormir(self):
        pass

class Humano(Trabalhador):
    def trabalhar(self):
        print("Humano trabalhando...")
    
    def comer(self):
        print("Humano comendo...")
    
    def dormir(self):
        print("Humano dormindo...")

class Robo(Trabalhador):
    def trabalhar(self):
        print("Robô trabalhando...")
    
    def comer(self):
        # Robôs não comem, mas são forçados a implementar este método
        raise NotImplementedError("Robôs não comem!")
    
    def dormir(self):
        # Robôs não dormem, mas são forçados a implementar este método
        raise NotImplementedError("Robôs não dormem!")

# Demonstração
humano = Humano()
humano.trabalhar()
humano.comer()
humano.dormir()

robo = Robo()
robo.trabalhar()
# robo.comer()  # Isso causaria um erro

# %%
print("\nExemplo Bom - Aplicando ISP:")

from abc import ABC, abstractmethod

class Trabalhador(ABC):
    @abstractmethod
    def trabalhar(self):
        pass

class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

class Dorminhoco(ABC):
    @abstractmethod
    def dormir(self):
        pass

class Humano(Trabalhador, Comedor, Dorminhoco):
    def trabalhar(self):
        print("Humano trabalhando...")
    
    def comer(self):
        print("Humano comendo...")
    
    def dormir(self):
        print("Humano dormindo...")

class Robo(Trabalhador):
    def trabalhar(self):
        print("Robô trabalhando...")

# Demonstração
humano = Humano()
humano.trabalhar()
humano.comer()
humano.dormir()

robo = Robo()
robo.trabalhar()
# Agora não temos métodos desnecessários na classe Robo

# %%
# D: Princípio da Inversão de Dependência (DIP)
# ------------------------------------------
# "Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações."

print("\n### Princípio da Inversão de Dependência (DIP) ###")
print("Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações.")

# %%
print("\nExemplo Ruim - Violando DIP:")

class MySQLDatabase:
    def conectar(self):
        print("Conectando ao MySQL...")
    
    def executar_query(self, query):
        print(f"Executando query no MySQL: {query}")

class ServicoUsuario:
    def __init__(self):
        # Dependência direta de uma implementação concreta
        self.db = MySQLDatabase()
    
    def salvar_usuario(self, usuario):
        self.db.conectar()
        query = f"INSERT INTO usuarios VALUES ('{usuario.nome}', '{usuario.email}')"
        self.db.executar_query(query)

# Se quisermos mudar para outro banco de dados, precisamos modificar ServicoUsuario
# Demonstração
usuario = Usuario("Carlos Silva", "carlos@exemplo.com")
servico = ServicoUsuario()
servico.salvar_usuario(usuario)

# %%
print("\nExemplo Bom - Aplicando DIP:")

from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def conectar(self):
        pass
    
    @abstractmethod
    def executar_query(self, query):
        pass

class MySQLDatabase(Database):
    def conectar(self):
        print("Conectando ao MySQL...")
    
    def executar_query(self, query):
        print(f"Executando query no MySQL: {query}")

class PostgreSQLDatabase(Database):
    def conectar(self):
        print("Conectando ao PostgreSQL...")
    
    def executar_query(self, query):
        print(f"Executando query no PostgreSQL: {query}")

class ServicoUsuario:
    def __init__(self, database):
        # Dependência de abstração, não de implementação concreta
        self.db = database
    
    def salvar_usuario(self, usuario):
        self.db.conectar()
        query = f"INSERT INTO usuarios VALUES ('{usuario.nome}', '{usuario.email}')"
        self.db.executar_query(query)

# Demonstração
usuario = Usuario("Carlos Silva", "carlos@exemplo.com")

# Usando MySQL
servico_mysql = ServicoUsuario(MySQLDatabase())
servico_mysql.salvar_usuario(usuario)

# Usando PostgreSQL
servico_postgres = ServicoUsuario(PostgreSQLDatabase())
servico_postgres.salvar_usuario(usuario)

# %%
# De SOLID para Design Patterns
# ----------------------------
print("\n## SOLID como fundação para Design Patterns ##")
print("Vamos ver como a aplicação repetida dos princípios SOLID naturalmente nos leva a um design pattern.")

# %%
print("\n# Exemplo: Sistema de Notificações")
print("Começamos com uma classe que viola vários princípios SOLID e evoluímos para uma solução que implementa o padrão Strategy sem pensar nele explicitamente.")

# %%
print("\nEstágio 1: Código Inicial (Ruim)")

class GerenciadorNotificacoes:
    def enviar_notificacao(self, tipo, mensagem, destinatario):
        if tipo == "email":
            print(f"Enviando email para {destinatario}: {mensagem}")
            # Lógica de envio de email
        elif tipo == "sms":
            print(f"Enviando SMS para {destinatario}: {mensagem}")
            # Lógica de envio de SMS
        elif tipo == "push":
            print(f"Enviando notificação push para {destinatario}: {mensagem}")
            # Lógica de envio de push
        else:
            raise ValueError("Tipo de notificação não suportado")

# Demonstração
notificador = GerenciadorNotificacoes()
notificador.enviar_notificacao("email", "Olá, seu pedido foi confirmado!", "cliente@exemplo.com")
notificador.enviar_notificacao("sms", "Seu código de verificação: 1234", "+5511999999999")

# %%
print("\nEstágio 2: Aplicando SRP")
print("Separamos cada tipo de notificação em sua própria classe")

class NotificadorEmail:
    def enviar(self, mensagem, destinatario):
        print(f"Enviando email para {destinatario}: {mensagem}")
        # Lógica específica de envio de email

class NotificadorSMS:
    def enviar(self, mensagem, destinatario):
        print(f"Enviando SMS para {destinatario}: {mensagem}")
        # Lógica específica de envio de SMS

class NotificadorPush:
    def enviar(self, mensagem, destinatario):
        print(f"Enviando notificação push para {destinatario}: {mensagem}")
        # Lógica específica de envio de push

class GerenciadorNotificacoes:
    def enviar_notificacao(self, tipo, mensagem, destinatario):
        if tipo == "email":
            notificador = NotificadorEmail()
            notificador.enviar(mensagem, destinatario)
        elif tipo == "sms":
            notificador = NotificadorSMS()
            notificador.enviar(mensagem, destinatario)
        elif tipo == "push":
            notificador = NotificadorPush()
            notificador.enviar(mensagem, destinatario)
        else:
            raise ValueError("Tipo de notificação não suportado")

# %%
print("\nEstágio 3: Aplicando OCP")
print("Tornamos o sistema aberto para extensão")

from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensagem, destinatario):
        pass

class NotificadorEmail(Notificador):
    def enviar(self, mensagem, destinatario):
        print(f"Enviando email para {destinatario}: {mensagem}")
        # Lógica específica de envio de email

class NotificadorSMS(Notificador):
    def enviar(self, mensagem, destinatario):
        print(f"Enviando SMS para {destinatario}: {mensagem}")
        # Lógica específica de envio de SMS

class NotificadorPush(Notificador):
    def enviar(self, mensagem, destinatario):
        print(f"Enviando notificação push para {destinatario}: {mensagem}")
        # Lógica específica de envio de push

class GerenciadorNotificacoes:
    def __init__(self):
        self.notificadores = {
            "email": NotificadorEmail(),
            "sms": NotificadorSMS(),
            "push": NotificadorPush()
        }
    
    def enviar_notificacao(self, tipo, mensagem, destinatario):
        if tipo not in self.notificadores:
            raise ValueError("Tipo de notificação não suportado")
        
        notificador = self.notificadores[tipo]
        notificador.enviar(mensagem, destinatario)
    
    def registrar_notificador(self, tipo, notificador):
        self.notificadores[tipo] = notificador

# Demonstração
notificador = GerenciadorNotificacoes()
notificador.enviar_notificacao("email", "Olá, seu pedido foi confirmado!", "cliente@exemplo.com")

# Agora podemos adicionar novos tipos de notificação sem modificar o gerenciador
class NotificadorWhatsApp(Notificador):
    def enviar(self, mensagem, destinatario):
        print(f"Enviando WhatsApp para {destinatario}: {mensagem}")

notificador.registrar_notificador("whatsapp", NotificadorWhatsApp())
notificador.enviar_notificacao("whatsapp", "Olá! Temos uma promoção para você!", "+5511999999999")

# %%
print("\nEstágio 4: Aplicando DIP")
print("Invertemos a dependência fazendo com que o cliente injete o notificador")

from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensagem, destinatario):
        pass

class NotificadorEmail(Notificador):
    def enviar(self, mensagem, destinatario):
        print(f"Enviando email para {destinatario}: {mensagem}")

class NotificadorSMS(Notificador):
    def enviar(self, mensagem, destinatario):
        print(f"Enviando SMS para {destinatario}: {mensagem}")

class NotificadorPush(Notificador):
    def enviar(self, mensagem, destinatario):
        print(f"Enviando notificação push para {destinatario}: {mensagem}")

class ServicoNotificacao:
    def __init__(self, notificador):
        self.notificador = notificador
    
    def notificar(self, mensagem, destinatario):
        self.notificador.enviar(mensagem, destinatario)

# Demonstração
servico_email = ServicoNotificacao(NotificadorEmail())
servico_email.notificar("Olá, seu pedido foi confirmado!", "cliente@exemplo.com")

servico_sms = ServicoNotificacao(NotificadorSMS())
servico_sms.notificar("Seu código de verificação: 1234", "+5511999999999")

# %%
print("\nEstágio 5: Versão Final")
print("Chegamos naturalmente ao padrão Strategy sem planejá-lo!")

from abc import ABC, abstractmethod

# Strategy Pattern: Interface de estratégia
class EstrategiaNotificacao(ABC):
    @abstractmethod
    def notificar(self, mensagem, destinatario):
        pass

# Estratégias concretas
class NotificacaoEmail(EstrategiaNotificacao):
    def notificar(self, mensagem, destinatario):
        print(f"Enviando email para {destinatario}: {mensagem}")
        # Lógica específica de email

class NotificacaoSMS(EstrategiaNotificacao):
    def notificar(self, mensagem, destinatario):
        print(f"Enviando SMS para {destinatario}: {mensagem}")
        # Lógica específica de SMS

class NotificacaoPush(EstrategiaNotificacao):
    def notificar(self, mensagem, destinatario):
        print(f"Enviando push para {destinatario}: {mensagem}")
        # Lógica específica de push

# Contexto que usa a estratégia
class ContextoNotificacao:
    def __init__(self, estrategia=None):
        self.estrategia = estrategia
    
    def definir_estrategia(self, estrategia):
        self.estrategia = estrategia
    
    def enviar_notificacao(self, mensagem, destinatario):
        if self.estrategia is None:
            raise ValueError("Estratégia de notificação não definida")
        self.estrategia.notificar(mensagem, destinatario)

# Demonstração
contexto = ContextoNotificacao()

# Notificação por email
contexto.definir_estrategia(NotificacaoEmail())
contexto.enviar_notificacao("Seu pedido foi confirmado!", "cliente@exemplo.com")

# Notificação por SMS
contexto.definir_estrategia(NotificacaoSMS())
contexto.enviar_notificacao("Seu código de verificação: 1234", "+5511999999999")

# Fácil adicionar novas estratégias
class NotificacaoSlack(EstrategiaNotificacao):
    def notificar(self, mensagem, destinatario):
        print(f"Enviando mensagem no Slack para {destinatario}: {mensagem}")

contexto.definir_estrategia(NotificacaoSlack())
contexto.enviar_notificacao("Nova tarefa atribuída a você!", "@usuario")

# %%
print("\n## Conclusão: SOLID e Design Patterns ##")
print("""
Observamos como a aplicação iterativa dos princípios SOLID nos levou naturalmente ao Design Pattern Strategy:

1. Começamos com uma classe que violava SRP (muitas responsabilidades)
2. Aplicamos SRP separando as responsabilidades em classes diferentes
3. Aplicamos OCP tornando o sistema extensível para novos tipos de notificação
4. Aplicamos DIP invertendo as dependências
5. O resultado final é exatamente o padrão Strategy, que emergiu naturalmente da aplicação dos princípios SOLID

Os princípios SOLID são fundamentais porque:
- Fornecem diretrizes claras para resolver problemas comuns de design
- Ajudam a identificar quando um padrão de design é necessário
- Muitas vezes resultam em estruturas que são equivalentes a padrões de design conhecidos
- Permitem chegar às soluções corretas sem precisar memorizar catálogos de padrões

Em vez de pensar "Preciso usar o padrão Strategy aqui", é melhor pensar "Como posso melhorar este código com SOLID?" - os padrões emergem naturalmente.
""")
