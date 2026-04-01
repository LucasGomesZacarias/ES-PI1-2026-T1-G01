# ES-PI1-2026-T1-G01
Descrição do Projeto 

Este projeto consiste no desenvolvimento de um sistema de votação digital fictício, com finalidade didática, desenvolvido para a disciplina de Projeto Integrador 1 da PUC Campinas. 

O sistema simula um processo eleitoral completo, sendo responsável por: 

- Cadastrar eleitores com validação de CPF e título de eleitor
- Gerar uma chave de acesso única para cada eleitor
- Cadastrar candidatos com número e partido
- Permitir a abertura da votação apenas por um mesário autorizado
- Registrar votos de forma segura e impedir votos duplicados
- Gerar um protocolo de votação para cada eleitor
- Realizar a contagem dos votos automaticamente
- Exibir o resultado final da eleição
- Gerar estatísticas de participação dos eleitores
- Registrar logs de todas as ações importantes do sistema
- Permitir auditoria para verificação da integridade dos dados 


Integrantes 
- Augusto Henrique Marçura
- Felipe Evangelista Cruz 
- Gabriel Grigoletto Ribas 
- Lucas Gomes Zacarias 
- Luiz Felipe da Conceição 

Tecnologias Utilizadas 
- Python 3.x 
- MySQL 
- Biblioteca mysql.connector 
- Biblioteca datetime
- Git e GitHub 

Instruções para Execução do Sistema 
1. Clonar o repositório
- Abra o terminal de seu computador e execute: git clone <link-do-repositorio>
- Depois entre na pasta do projeto, escrevendo o seguinte comando: cd nome-do-repositorio
2. Instalar dependências
- Certifique-se de ter Python instalado. Logo em seguida, execute o seguinte comando: pip install mysql-connector-python
3. Configurar o banco de dados (MySQL)
- Abra o MySQL (Workbench ou terminal)
- Crie o banco de dados: CREATE DATABASE votacao;
- Use o banco: USE votacao;
- Execute o script SQL do projeto (caso exista um arquivo '.sql') ou crie as tabelas manualmente conforme o desenvolvimento.
4. Configurar conexão com o banco
No código Python (geralmente em um arquivo de conexão), altere:
- host (ex: localhost)
- user (ex: root)
- password (sua senha do MySQL)
- database (votacao)
5. Executar o sistema
- No terminal, execute: python main.py
6. Utilizar o sistema
Após iniciar, escolha um módulo:
- Gerenciamento (cadastros)
- Votação
- Auditoria / Resultados

- Sigas as instruções exibidas no terminal

Observação
O sistema roda totalmente no terminal (sem interface gráfica) e depende do banco de dados configurado corretamente para funcionar. 
