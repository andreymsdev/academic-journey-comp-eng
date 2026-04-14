# Fundamentos de Internet e Web
Professor Júlio Cezar Estrella

## Semana 4

**Como surgiu a WWW?**

As ideias por trás da WWW inciaram-se na década de 1980 na Suíça.

- Havia o desejo de tornar mais fácil as pesquisas. 

**1990** - berners-lee usou um computador nextcube ara escrever o primeiro servidor web e o primeiro navegador chamado de WorldWideWeb.

**1991** - Nasce a WWW. Já havia protocolos como os de serviços de e-mail ((FTP) File transfer Protocol)

**Funcionamento Básico da WEB**

Tudo é armazenado em servidores.

O usuário/cliente/browser não consegue acessar diretamente o arquivo que deseja ler sem pedir para o servidor.

---

Recursos: (áudio, vídeo, texxto), os quais são obtidos por meio de uma URL e armazenados em servidores

---

URL - endereço

HTTP - protocolo que especifíca como o navegador e o servidor web se comunicam entre si

Sockets: são a interface de comunicação entre aplicações e a rede

HTTP Methods:

**GET:** Solicita a representação de um recurso (usado apenas para buscar dados).

**POST:** Envia dados para o servidor para criar um novo recurso.

**PUT:** Substitui todas as representações atuais de um recurso pelos dados da requisição.

**PATCH** Aplica modificações parciais a um recurso já existente.

**DELETE:** Remove um recurso específico do servidor.

**HEAD:** Semelhante ao GET, mas solicita apenas o cabeçalho (sem o corpo da resposta).

**OPTIONS:** Descreve as opções de comunicação (quais métodos são permitidos) para o recurso.

Exemplo

GET (Metódo) Path (HTTP) Versão do protocolo (1.1) Headers (developer.mozilla.org)

get/http/1.1/developer.mozilla.org

---

**DNS (Domain Name System)**

É uma sigla para o sistema de nomes de domínio.

É um registro que contém nomes de sites e seus respectivos endereços IP associados.

---

O DNS (Domain Name System) é essencialmente a "lista de contatos" da internet. Sem ele, a Web como conhecemos não seria funcional para seres humanos.

Aqui estão os motivos principais:

    Tradução de nomes: Ele converte endereços amigáveis (como google.com) em endereços IP numéricos (como 142.250.190.46) que os computadores entendem.

    Memorização: Seria impossível para nós memorizarmos sequências de números para cada site que visitamos; o DNS permite usar palavras.

    Localização de Recursos: Ele direciona seu navegador para o servidor correto onde os arquivos do site estão hospedados.

    Flexibilidade: Se uma empresa muda de servidor (e muda o IP), ela só precisa atualizar o registro DNS, e o endereço www.site.com continua funcionando normalmente para o usuário.

    Eficiência e Velocidade: Através de sistemas de cache, o DNS resolve essas buscas em milissegundos, garantindo que o carregamento das páginas seja fluido.

---

[Atividade Avaliativa](atividade-avaliativa.png)
Obs: questão 8 mal formulada.