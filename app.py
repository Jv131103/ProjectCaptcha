from flask import Flask, render_template, request
from cp import CreateCaptcha

app = Flask(__name__)

@app.route('/')
def home():
    c = CreateCaptcha()
    captcha_text = c.Gerar()
    c.GerarImagem(captcha_text)
    return render_template('captcha.html', captcha_text=captcha_text)


@app.route('/check', methods=['POST'])
def check_captcha():
    user_input = request.form['captcha_input'].upper()
    captcha_text = request.form['captcha_text']
    c = CreateCaptcha()
    is_valid = c.Validar(captcha_text, user_input)
    return "Olá, você acessou o site<br>O captcha foi preenchido corretamente :)" if is_valid == True else "Hmm que pena o captcha não foi preenchido corretamente :(" 

if __name__ == '__main__':
    app.run(debug=True, port=5001, host="0.0.0.0")
