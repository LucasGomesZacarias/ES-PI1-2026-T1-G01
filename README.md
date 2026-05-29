# Sistema de Votação Digital — ES-PI1-2026-T1-G01

Projeto desenvolvido para a disciplina de **Projeto Integrador 1** da **PUC Campinas** (2026 — Turma 1 — Grupo 01).

---

## Descrição do Projeto

Este projeto consiste no desenvolvimento de um sistema de votação digital fictício, com finalidade didática. O sistema simula um processo eleitoral completo, rodando inteiramente no terminal (sem interface gráfica), com persistência de dados via banco MySQL.

As funcionalidades implementadas são:

- Cadastro de eleitores com validação de CPF (dígitos verificadores) e título de eleitor (cálculo dos dígitos verificadores por unidade federativa)
- Geração de chave de acesso única e aleatória para cada eleitor cadastrado
- Criptografia e descriptografia de dados sensíveis (CPF, título de eleitor e chave de acesso) usando cifra de Hill com matriz chave 2x2
- Cadastro de candidatos com nome, partido e número
- Autenticação do mesário por título de eleitor, prefixo do CPF e chave de acesso antes de abrir a votação
- Zerézima: zeramento dos votos e reset de confirmações antes de cada eleição, com limpeza do log
- Registro seguro de votos com bloqueio de votos duplicados por eleitor
- Suporte a voto nulo
- Emissão de protocolo de votação criptografado e único para cada eleitor
- Listagem de protocolos em ordem para auditoria
- Contagem automática de votos por candidato e por partido ao encerrar a eleição
- Exibição do resultado final com destaque ao vencedor (boletim de urna)
- Estatísticas de comparecimento: total de eleitores, total de votantes e percentual de participação
- Validação de integridade: comparação entre votos registrados na urna e eleitores marcados como "já votou"
- Log automático de ocorrências com timestamp para todas as ações relevantes (abertura, encerramento, acesso negado, voto duplo, voto realizado)
- Exibição do histórico de logs pelo terminal
- Menus de navegação para Gerenciamento, Votação e Auditoria/Resultados

---

## Integrantes

- Augusto Henrique Marçura
- Felipe Evangelista Cruz
- Gabriel Grigoletto Ribas
- Lucas Gomes Zacarias
- Luiz Felipe da Conceição

---

## Tecnologias Utilizadas

**Linguagem e banco de dados**

- Python 3.x — linguagem principal do sistema
- MySQL — banco de dados relacional para persistência de eleitores, candidatos e votos

**Bibliotecas externas (instalar via pip)**

- `mysql-connector-python` — conexão e execução de queries no banco MySQL
- `pyfiglet` — geração do banner ASCII da tela inicial ("ELEICOES PUC")
- `colorama` — colorização e estilo de texto no terminal (cores, brilho, reset)
- `tqdm` — barra de progresso animada nas telas de carregamento e zerézima
- `rich` — formatação de mensagens de erro com cores no terminal

**Bibliotecas nativas do Python (sem instalação)**

- `datetime` — geração dos timestamps nos registros de log
- `random` — geração do protocolo de votação único e aleatório
- `os` — limpeza de tela compatível com Windows (`cls`) e Linux/macOS (`clear`)
- `time` — pausas e animações entre telas

---

## Pré-requisitos

Antes de executar o sistema, certifique-se de ter instalado:

- [Python 3.x](https://www.python.org/downloads/)
- [MySQL Server](https://dev.mysql.com/downloads/mysql/)
- Git

---

## Como Usar

**1. Clonar o repositório**

```bash
git clone https://github.com/LucasGomesZacarias/ES-PI1-2026-T1-G01.git
cd ES-PI1-2026-T1-G01
```

**2. Instalar as dependências**

```bash
pip install mysql-connector-python pyfiglet colorama tqdm rich
```

**3. Criar o banco de dados**

Abra o MySQL (Workbench ou terminal) e execute:

```sql
CREATE DATABASE banco_dados_pi;
USE banco_dados_pi;
```

Em seguida, rode o script SQL para criar as tabelas e inserir os dados de exemplo:

```bash
mysql -u root -p banco_dados_pi < BD/BD-ProjetoPI.sql
```

**4. Configurar a conexão com o banco**

Abra o arquivo `scripts/conexao_bd.py` e altere as credenciais conforme o seu ambiente:

```python
host     = "localhost"
user     = "root"
password = "SUA_SENHA_AQUI"
database = "banco_dados_pi"
```

**5. Iniciar o sistema**

A partir da pasta `scripts/`, execute:

```bash
cd scripts
python principal.py
```

O sistema exibe uma tela inicial com banner animado. Pressione Enter para continuar.

**6. Cadastrar eleitores e candidatos (Gerenciamento)**

No menu principal, selecione a opção `1. Gerenciamento`. A partir dali é possível:

- Cadastrar eleitores informando nome, CPF e título de eleitor — o sistema valida os dígitos verificadores automaticamente e gera uma chave de acesso única para cada eleitor
- Cadastrar candidatos informando nome, partido e número
- Editar, buscar, listar e remover eleitores e candidatos já cadastrados

Ao menos um eleitor deve ser cadastrado com o campo `mesario = TRUE` no banco para poder abrir a votação.

**7. Abrir a votação (Votação → Abrir votação)**

No menu principal, selecione `2. Votação` e depois `1. Abrir votação`. O sistema solicita as credenciais do mesário:

- Título de eleitor
- 4 primeiros dígitos do CPF
- Chave de acesso

Após autenticação bem-sucedida, a zerézima é executada automaticamente: todos os votos anteriores são zerados, as confirmações de voto dos eleitores são resetadas e o arquivo de log é limpo. A votação fica disponível.

**8. Registrar votos**

Com a votação aberta, cada eleitor se identifica informando título de eleitor, 4 primeiros dígitos do CPF e chave de acesso. Em seguida digita o número do candidato desejado ou opta por voto nulo. O sistema emite um protocolo criptografado único como comprovante e bloqueia novas tentativas de voto do mesmo eleitor.

**9. Encerrar a votação**

No menu `2. Votação`, selecione a opção de encerramento. O mesário deve se autenticar novamente. Ao confirmar, o encerramento é registrado no log.

**10. Consultar resultados (Votação → Resultados)**

No menu de Votação, selecione `3. Resultados da Votação`. As opções disponíveis são:

- Boletim de urna: exibe votos por candidato e destaca o vencedor
- Votos por partido: exibe o total de votos válidos agrupados por partido
- Estatísticas de comparecimento: exibe total de eleitores, total de votantes e percentual de participação

**11. Auditar a eleição (Votação → Auditoria)**

No menu de Votação, selecione `2. Auditoria de votação`. As opções disponíveis são:

- Validação de integridade: compara o total de votos registrados na urna com o total de eleitores marcados como "já votou" e informa se há inconsistências
- Listagem de protocolos: exibe todos os protocolos de votação em ordem, permitindo que cada eleitor confirme o seu comprovante
- Histórico de logs: exibe todas as ocorrências registradas no arquivo `log_ocorrencias.txt` com data e hora

---

## Observações

- O sistema roda exclusivamente no terminal, sem interface gráfica.
- O banco de dados MySQL deve estar em execução antes de iniciar o sistema.
- Apenas o mesário cadastrado e autenticado pode abrir e encerrar a votação.
- A zerézima é executada automaticamente na abertura, zerando todos os votos anteriores e limpando o log.
- Cada eleitor só pode votar uma vez; tentativas de voto duplo são bloqueadas e registradas no log.
- Os dados sensíveis (CPF, título de eleitor, chave de acesso e protocolos) são armazenados criptografados no banco.
