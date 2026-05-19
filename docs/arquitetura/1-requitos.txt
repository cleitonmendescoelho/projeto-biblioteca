📌 REQUISITOS FUNCIONAIS

🔹 1.Seções de Páginas

* Login
* Cadastro
* Recuperação de senha
* Painel principal
* Minha Biblioteca
* Histórico
* Favoritos
* Relatórios
---------------------------------------------------------------------------------


🔹 2. Cadastro

A aplicação deve coletar informações do usuário para realização do cadastro. Tais informações devem ser fornecidas:

* Nome
* Sobrenome
* CPF
* Data de Nascimento
* Telefone
* Email
* Senha

🔹 2.1 - lógica de negócio

* Nome: 
 - O campo não pode está vazio.
 - O campo não pode ter menos que 5 caracteres.
 - O campo não pode permitir números.

  * Sobrenome: 
 - O campo não pode está vazio.
 - O campo não pode ter menos que 5 caracteres.

 * Data de Nascimento:
 - Não pode permitir data futura
 - Não pode está vazia
 - A data salva no banco de dados deve seguir o formato D/M/A

 * CPF: 
 - Não pode está vazio
 - Deve conter 11 digitos
 - Não pode conter valores alfabéticos
 - Não deve permitir CPF duplicados

 * Telefone:
 - Não pode está vazio
 - deve conter o DDD
 - deve ter no mínimo 10 caracteres

 * Email:
 - Não pode está vazio
 - O campo email deve respeitar o padrão dos emails.
 - Não pode conter email duplicados

 * Senha:
 - Não pode está vazio
 - Deve ter no minimo 8 caracteres

🔹 3 - Login

* A aplicação deve verificar se o email do usuário está cadastrado na base de dados
* A aplicação deve consultar se a senha digitada pelo usuário corresponde a cadastrada no banco de dados
* A aplicação deve informar ao usuário qualquer problema no processo de autenticação referente a verificação do email e senha
* A aplicação deve fornecer um método de recuperação de senha que implemente etapas de verificação do usuário que vise garantir a segurança e autenticidade
* A aplicação deve fornecer métodos alternativos de login

🔹 4. Interface — Painel principal

* A interface principal deve exibir os livros (biblioteca) que o usuário pode pegar
* O usuário pode favoritar os livros desejados
* A interface principal deve permitir o usuário pesquisar os livros
* Cada livro deve ter a opção "Ler"


🔹 5 - Minha Biblioteca

* A seção deve armazenar todos os livros clicados em Ler
* A seção deve permitir a remoção dos livros armazenadas


🔹 6 - Favoritos
* A seção deve armazenar todos os livros marcados como Favoritos
* A seção deve permitir a remoção dos livros favoritados

🔹 7 - Histórico


🔹 8 - Relatórios










------------------------------------------------------------------------------------------
💻 Recursos:

* A Tela inicial irá conter um acervo digital de livros
* A tela inicial deve conter uma barra de pesquisa de livros
* A tela inicial deve possibilitar a filtragem de tipo de livro
* A tela inicial deve conter o mecanismo de gerenciamento de dados e logon
* A tela inicial deve contar os dados estatisticos de imprestimo de livros
* Cada livro tem a opção do usuário favoritar
* Quando o usuário clicar em reservar a aplicação deve registrar a data e a hora em que foi realizado o registro.

📊 Consulta de Status e Histórico

A aplicação vai conter uma consulta de status que irá gerar:

O status atual (livros que estão em uso)

O histórico anteriores de livros que foram imprestados

O histórico irá ter os seguintes registros:

Nome do livro

codigo do livro

Data do cadastro

Hora do cadastro

Data da devolução

Horários da devolução

Status (concluido ou pendente)

⚙ Ações disponíveis

Permitir que o usuario filte por data, ano e mês

Permitir que usuário faça o download do histórico em formato PDF

