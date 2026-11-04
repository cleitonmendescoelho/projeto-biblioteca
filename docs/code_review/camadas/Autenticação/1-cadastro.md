
- [x] **Campos sem `<label>`:** e-mail e senha dependem apenas de `placeholder`, o que prejudica a acessibilidade e faz com que a identificação desapareça ao digitar.

- [x] **Atributos de autocomplete ausentes:** adicionar `autocomplete="email"` e `autocomplete="current-password"`, importantes para gerenciadores de senha e usabilidade.

- [ ] **Mensagem de erro sem região de alerta:** a mensagem é exibida como uma lista sem `role="alert"` ou `aria-live`, portanto leitores de tela podem não anunciá-la. Além disso, o CSS remove apenas o marcador da lista, mas preserva suas margens padrão, podendo causar desalinhamento.

- [ ] **Layout não responsivo:** há `padding: 100px`, largura fixa de `900px`, imagem com `600px` e painel de formulário com altura fixa. Em telas pequenas, isso tende a criar rolagem horizontal ou conteúdo espremido.

- [ ] **Ausência de foco visível:** não há estilo de foco visível para campos, links e botão. A navegação por teclado fica pouco perceptível.

- [x] **Ícones sem funcionalidade definida:** os três ícones aparentam ser ações alternativas de autenticação, mas não são botões nem links e não possuem comportamento. Se não forem funcionalidades planejadas, devem ser removidos; se forem, precisam de semântica, texto acessível e implementação.

- [x] **Texto alternativo genérico na imagem:** o `alt="logo-login"` é genérico. Para uma imagem decorativa, usar `alt=""`; se a imagem comunica uma marca, descrevê-la adequadamente.