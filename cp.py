#You'r a robot?
from random import randint, randrange
from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

class CreateCaptcha:
    def __init__(self):
        self.valido = False
        self.l = []
        self.width = 300
        self.height = 150
        self.font_size = 60  # Tamanho maior da fonte

    def Gerar(self):
        y = randrange(4, 12, 4) #pega valores em um intervalo aleatório
        cont = y #Vai gerar o tamanho do capcha
        while cont > 0:
            n = randint(0, 1)
            if n == 0:
                val = chr(randint(65, 90))
            else:
                val = chr(randint(49, 57))
            self.l.append(val)
            cont -= 1
        #print(f"CARACETERES DE VERIFICAÇÃO: {l}") #Apenas para análise
        l = ''.join(self.l) #Uni as letras
        return l

    def Validar(self, MeuGerador, ValorUser):
        #Executa a validação
        if ValorUser == MeuGerador:
            self.valido = True
            return self.valido
        else:
             return self.valido

    def GerarImagem(self, text):
        # Cria uma imagem em branco
        image = Image.new('RGB', (self.width, self.height), color=(255, 255, 255))

        # Cria um objeto de desenho
        draw = ImageDraw.Draw(image)

        # Carrega uma fonte para o texto com tamanho maior
        font = ImageFont.load_default()
        font = ImageFont.truetype("arial.ttf", self.font_size)  # Use a fonte TrueType e defina o tamanho da fonte

        # Obtém as dimensões da caixa do texto
        text_bbox = draw.textbbox((0, 0), text, font)

        # Centraliza o texto na imagem
        x = (self.width - text_bbox[2] - text_bbox[0]) / 2
        y = (self.height - text_bbox[3] - text_bbox[1]) / 2

        # Desenha o texto na imagem
        draw.text((x, y), text, fill=(0, 0, 0), font=font)

        # Adiciona um risco à imagem
        for _ in range(10):
            x1 = randint(0, self.width - 1)
            y1 = randint(0, self.height - 1)
            x2 = randint(0, self.width - 1)
            y2 = randint(0, self.height - 1)
            draw.line([(x1, y1), (x2, y2)], fill=(0, 0, 0), width=2)

        # Adiciona um padrão de fundo aleatório (pontos)
        for _ in range(1000):
            x = randint(0, self.width - 1)
            y = randint(0, self.height - 1)
            draw.point((x, y), fill=(0, 0, 0))

        #Salve o arquivo na pasta image
        d = os.getcwd()
        i = "static\\image"
        caminho  = os.path.join(d, i)
        element_image_path = os.path.join(caminho, "element_image.png")

        # Salva a imagem como um arquivo
        image.save(element_image_path)


if __name__ == "__main__":
    c = CreateCaptcha()
    x = c.Gerar()
    c.GerarImagem(x)
    print(x)
    y = input("Copie aqui ou digite errado: ").upper()
    print(c.Validar(x, y))

        
