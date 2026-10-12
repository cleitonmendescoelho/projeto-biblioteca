* Campos sem <label>: e-mail e senha dependem apenas de placeholder, o que prejudica acessibilidade e desaparece ao digitar.

* Faltam autocomplete="email" e autocomplete="current-password", importantes para gerenciadores de senha e usabilidade.

* A mensagem de erro é uma lista sem região de alerta (role="alert" ou aria-live), portanto leitores de tela podem não anunciá-la. Além disso, o CSS remove apenas o marcador da lista, mas preserva suas margens padrão, podendo causar desalinhamento.

* O layout não é responsivo: há padding: 100px, largura fixa de 900px, imagem com 600px e painel de formulário com altura fixa. Em telas pequenas, isso tende a criar rolagem horizontal ou conteúdo espremido.

* Não há estilo de foco visível para campos, links e botão; navegação por teclado fica pouco perceptível.

* Os três ícones aparentam ser ações alternativas de autenticação, mas não são botões nem links e não possuem comportamento. Se não forem funcionalidades planejadas, devem ser removidos; se forem, precisam de semântica, texto acessível e implementação.

* Os scripts do Ionicons vêm de CDN externo. Funciona, mas idealmente a dependência deve ser versionada/local ou ter uma política de integridade e disponibilidade definida.

* O alt="logo-login" é genérico. Para imagem decorativa, use alt=""; se comunica uma marca, descreva-a adequadamente.