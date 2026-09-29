# Relatório de análise — camada index.html

O index.html concentra layout global, catálogo, modal, paginação, navegação, CSS de várias páginas e JavaScript. Isso funciona como uma base improvisada, mas cria acoplamento e falhas de manutenção.
A validação manage.py check não encontrou problemas de configuração, porém ela não identifica rotas que falham ao renderizar, assets inexistentes, HTML mal estruturado ou funcionalidades incompletas.

Problemas críticos
- A rota “Relatórios” está quebrada: a view procura home/sections/relatorios.html, mas o arquivo não existe. O CSS home/css/paginas/relatorios.css também é referenciado e inexistente. Ao acessar o menu, ocorrerá erro de template.
- O HTML-base tem fechamento incorreto da estrutura dentro do {% block content %}. Quando biblioteca.html ou historico.html substituem o bloco, deixam de ser emitidos os fechamentos de main-layout e container. O navegador tenta corrigir automaticamente o DOM, mas isso torna o layout imprevisível.
- “Ler livro” altera o estado da aplicação por GET, via JavaScript e URL fixa: adiciona o livro à biblioteca e cria histórico. Operações que criam/removem dados devem usar POST, proteção CSRF e uma URL gerada por Django.
- A paginação exibida é apenas visual: os botões não possuem links, não há Paginator na view e todos os livros continuam sendo carregados.
- O botão de favorito não possui implementação, feedback nem semântica acessível.
Organização e estrutura de diretórios
A separação básica entre templates, static, views, models e urls é compatível com a convenção Django. Porém, a organização da camada de apresentação é inconsistente:
- index.html atua simultaneamente como página de catálogo e como template-base para páginas internas.
- Todos os CSS de páginas são carregados globalmente no template-base, inclusive o inexistente CSS de relatórios.
- Há CSS específico da tela principal, biblioteca e histórico, mas não há uma camada compartilhada explicitamente definida.
- A view referencia home/sections/relatorios.html, enquanto os demais templates usam home/paginas/; isso indica uma convenção incompleta.
- Há código morto e comentado em templates, testes e CSS, aumentando ruído e dificultando identificar o comportamento vigente.
- requirements.txt está vazio, o que impede reproduzir o ambiente de forma confiável.
Sugestão: estabelecer templates/home/base.html como layout global, manter cada página em templates/home/paginas/, centralizar estilos compartilhados em css/base.css e manter JS em static/home/js/.

Acoplamento excessivo
O maior acoplamento está em [`index.html`](C:/Users/cleit/Desktop/biblioteca/home/templates/home/paginas/index.html):
- O modal recebe todos os dados do livro como argumentos no atributo onclick; qualquer mudança no modelo, no texto ou no JavaScript exige alterações em vários pontos.
- JavaScript inline, handlers inline e CSS inline (style="font-size: 22px") misturam responsabilidades e dificultam testes, Content Security Policy e reutilização.
- A URL /adicionar-biblioteca/${id}/ está codificada no JavaScript, ignorando o resolvedor de URLs do Django.
- O layout-base conhece elementos exclusivos do catálogo, como o modal e a paginação.
- A busca do cabeçalho é compartilhada com todas as páginas, mas o histórico já possui outra busca, resultando em UX duplicada e ambígua.
Sugestão: usar data-* no cartão do livro, um arquivo JavaScript com addEventListener, e um formulário POST para a ação de adicionar à biblioteca.

Boas práticas, convenções e funcionalidades
Pontos positivos observados:
- Uso correto de {% static %}, {% url %}, {% csrf_token %} na remoção e escapejs nos textos enviados ao modal.
- Views internas usam @login_required.
- Busca no catálogo e histórico usa filtros icontains e Q.
- As imagens possuem alt, e a busca possui label visualmente oculta.

Pontos que precisam de correção:
- O campo “nome” na tabela do modal contém o autor; a semântica e o conteúdo estão incorretos.
- O modal não tem role="dialog", aria-modal, botão real de fechar, controle de foco, fechamento por Esc ou clique no fundo.
- Botões só com ícones não têm aria-label; o ícone de favorito e o avatar são exemplos.
- Há duas bibliotecas de ícones externas (Font Awesome e Ionicons), causando dependências e carregamento redundantes.
- Fontes e ícones externos não têm integrity/crossorigin e dependem de CDNs.
- @import para Google Fonts no CSS prejudica desempenho em relação a um <link> otimizado no <head>.
- A estatística “1,248” é fixa, embora a aplicação tenha dados no banco.
- O item de menu ativo não é definido conforme a rota atual.
- A interface declara filtros e ações no histórico que não possuem comportamento no backend.
- A rota bilioteca/ contém erro de grafia, criando uma URL pública pouco consistente.
- Há mistura de português e inglês em nomes de classes e termos de interface (borrow-btn, favorite-btn, book-card), sem padrão definido.

Melhorias futuras recomendadas
1. Criar um base.html com <head>, cabeçalho, menu, scripts e blocos específicos para título, estilos, conteúdo e scripts.
2. Separar o catálogo em componentes/includes reutilizáveis: cartão de livro, modal, paginação e sidebar.
3. Implementar paginação real com django.core.paginator.Paginator, preservando o parâmetro de busca.
4. Substituir ações mutáveis por formulários POST; exigir métodos HTTP no backend e manter CSRF.
5. Implementar ou remover controles que não funcionam: favoritos, continuidade de leitura, filtros do histórico, impressão e relatórios.
6. Tornar estatísticas e estado ativo do menu dinâmicos a partir da view/context processor.
7. Adotar convenções consistentes de nomes, URLs com barra final e remover trechos comentados obsoletos.
8. Criar testes reais: atualmente [`home/tests.py`](C:/Users/cleit/Desktop/biblioteca/home/tests.py) contém testes inteiramente comentados, portanto não há cobertura automatizada efetiva.
9. Preencher requirements.txt, separar configurações sensíveis do código e remover credenciais fixas de [`settings.py`](C:/Users/cleit/Desktop/biblioteca/biblioteca/settings.py).
10. Validar acessibilidade e HTML renderizado em navegador/validador, especialmente após corrigir a herança de templates.