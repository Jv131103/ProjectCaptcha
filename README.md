# ProjectCaptcha
Projeto Simples de integração de captcha

# CreateCaptcha - Gerador e Validador de Captcha

O CreateCaptcha é uma classe Python que permite gerar e validar códigos CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart). CAPTCHAs são usados para verificar se um usuário é humano antes de permitir o acesso a um serviço ou recurso.

## Como Usar

Primeiro, importe a classe `CreateCaptcha` em seu código Python:

```python
from cp import CreateCaptcha
```
Em seguida, você pode criar uma instância da classe CreateCaptcha e usá-la para gerar um código CAPTCHA:

```python
c = CreateCaptcha()
codigo_captcha = c.Gerar()
```

Isso gerará um código CAPTCHA aleatório composto por letras maiúsculas e números.

Para criar uma imagem do CAPTCHA e salvá-la em um arquivo:

```python
c.GerarImagem(codigo_captcha)
```

Isso criará uma imagem contendo o código CAPTCHA gerado e a salvará em um arquivo chamado element_image.png na pasta static/image.

Para validar uma resposta do usuário em relação ao código CAPTCHA gerado:

```python
resposta_usuario = input("Copie aqui ou digite errado: ").upper()
valido = c.Validar(codigo_captcha, resposta_usuario)

if valido:
    print("Código CAPTCHA válido. O usuário é humano.")
else:
    print("Código CAPTCHA inválido. O usuário pode ser um bot.")
```

## Requisitos
Certifique-se de ter instalada a biblioteca Pillow (PIL) para manipulação de imagens:

```Terminal
pip install Pillow
pip install flask
pip install Flask Pillow
```

# Flask Captcha Example

Este é um exemplo simples de aplicação web Flask que gera e valida CAPTCHAs (Completely Automated Public Turing test to tell Computers and Humans Apart) usando a classe `CreateCaptcha`.

## Visão Geral

Esta aplicação web tem duas rotas principais:

. `/`: Esta rota gera um novo CAPTCHA e exibe-o na página da web para o usuário. O usuário pode preencher o CAPTCHA e verificar se está correto clicando em "Verificar".

. `/check`: Esta rota recebe a resposta do usuário para o CAPTCHA e verifica se ela está correta ou não. Em seguida, exibe uma mensagem apropriada.

1. Execute a aplicação Flask:
``` python
python app.py
```

2. Acesse a aplicação em seu navegador em http://localhost:5000/ (ou outro endereço e porta, se configurado de forma diferente).

3. Você verá um CAPTCHA gerado na página. Copie o texto do CAPTCHA exibido.

4. Cole o texto do CAPTCHA no campo de entrada e clique em "Verificar".

5. A aplicação informará se o CAPTCHA foi preenchido corretamente ou não.

## Arquivos do Projeto
### app.py: 
O arquivo principal da aplicação Flask que contém as rotas e a lógica da aplicação.<br>
### cp.py: 
O arquivo que contém a classe CreateCaptcha responsável pela geração e validação do CAPTCHA.
templates/captcha.html: O arquivo HTML que exibe o CAPTCHA e a interface do usuário.

## Contribuições
Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novos recursos para este projeto. Basta abrir uma issue ou enviar um pull request no GitHub.


