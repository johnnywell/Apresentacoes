# Apresentacoes

Repositorio de apresentacoes sobre engenharia de software, cobrindo principios de design, arquitetura limpa, refatoracao de codigo legado e qualidade de codigo atraves de testes. O material e voltado para encontros de comunidades e guilds de engenharia, com foco em exemplos praticos e discussoes em grupo.

Todas as apresentacoes sao Jupyter Notebooks executaveis, com exemplos de codigo em Python que podem ser rodados interativamente.

## Apresentacoes

### Principios SOLID

**Arquivo:** `SOLID.ipynb`

Apresentacao didatica sobre os 5 principios SOLID, com exemplos comparativos de codigo "antes e depois" para cada principio:

- **Single Responsibility (SRP)** - Separacao de responsabilidades em classes
- **Open/Closed (OCP)** - Extensao sem modificacao via abstracoes
- **Liskov Substitution (LSP)** - Substituicao segura de subtipos
- **Interface Segregation (ISP)** - Interfaces especificas ao inves de genericas
- **Dependency Inversion (DIP)** - Depender de abstracoes, nao de implementacoes

Demonstra como a aplicacao iterativa dos principios SOLID leva naturalmente ao surgimento do **Strategy Pattern**.

---

### Refatorando Codigo Legado com SOLID e Design Patterns

**Arquivo:** `Refatorando Codigo Legado com SOLID e Design Patterns.ipynb`

Workshop pratico e interativo sobre refatoracao de codigo legado. Aborda:

- Complexidade essencial vs. acidental
- Identificacao de code smells: condicionais excessivas, classes gigantes, metodos longos
- Exercicios guiados de refatoracao aplicando SRP, OCP e Factory Method
- Estrategias para refatoracao incremental com cobertura de testes

Formato de oficina com pausas para os participantes pensarem e codificarem antes de ver a solucao.

---

### Entenda Clean Architecture De Vez

**Arquivo:** `7o Forum da Guilda de Engenharia de Software.ipynb`

Discussao guiada sobre Clean Architecture, apresentada no 7o Forum da Guilda de Engenharia de Software. Cobre:

- A regra de ouro: dependencias apontam para o dominio
- Componentes principais com exemplos de codigo: Entities, UseCases, Presenters, Services, Repositories, Adapters e Controllers
- Exemplo completo de Presenter com enriquecimento de dados
- Quando Clean Architecture parece "overengineering" e como lidar
- Aplicacao em projetos pequenos e legados

Inclui diagramas visuais da arquitetura e referencias bibliograficas.

---

### Testes como Ferramenta para Identificar Codigo que Pede Refatoracao

**Arquivo:** `Testes como ferramenta para identificar codigo que pede refatoracao.ipynb`

Exercicios praticos que demonstram como a dificuldade em testar revela problemas de design:

- **Acoplamento excessivo** - Injecao de dependencia como solucao
- **Violacao do SRP** - Separacao de responsabilidades para testabilidade
- **Violacao do DIP** - Uso de Protocols/interfaces para facilitar mocks
- **God Object** - Decomposicao em classes coesas e independentes

Cada exercicio apresenta o codigo problematico, mostra por que e dificil testar e aplica a refatoracao com o resultado testavel.

---

### Relatorio: O Lugar que Ainda Nao Existe

**Pasta:** `relatorio_o_lugar_que_ainda_nao_existe/`

Pesquisa de mercado sobre um potencial espaco de coworking criativo/maker em Curitiba. Contem analise de 19 respostas com visualizacoes graficas sobre interesse, frequencia de uso, preco e colaboracao.

## Como usar

### Requisitos

- Python 3.10+
- Jupyter Notebook

### Instalacao

```bash
pip install -r requirements.txt
```

### Executando as apresentacoes

Como notebooks interativos:

```bash
jupyter notebook
```

Para gerar slides HTML:

```bash
jupyter nbconvert --to slides <notebook>.ipynb --post serve
```

## Autor

**Johnny Wellington** - CEO & Engenheiro de Software na Arbet Studio. 17+ anos de experiencia, com passagens por Nubank, QuintoAndar e Snowman Labs. Especialista em arquitetura de software, design de APIs, testes automatizados e CI/CD.

## Licenca

Este material e disponibilizado para fins educacionais.
