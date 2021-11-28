from flask import Flask, render_template

app = Flask(__name__)

# criar a 1° página do site
# route -> nomedapagina.com/
# função -> o que está sendo exibido na página
# template

# Página inicial
@app.route('/')
def homepage():
    return render_template("homepage.html")

# Exemplo de mais páginas
@app.route('/pagina2')
def pagina2():
    return render_template("pagina2.html")



# Caso a gente vá usar login no site, deixa isso aq guardado
@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario) 


# por o site no ar(ao rodar, irá ser disponibilizado um link no terminal, acessando o link vc terá um servidor local)
if __name__ == '__main__':
    app.run(debug=True)

