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
```

## Contribuições
Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novos recursos para este projeto. Basta abrir uma issue ou enviar um pull request no GitHub.


