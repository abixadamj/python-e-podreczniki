from flask import Flask, request
from Morse_Code import *


# tworzymy główny obiekt aplikacji
app = Flask("Alfabet_Morse")

# definiujemy akcję związaną z URL: "/"
@app.route('/', methods = ['POST',"GET"])
def koduj_formularz():
    post = """
    <h1> Kodowanie Morse'a </h1> <hr>
    <form method="POST" action="/">
    Wpisz tekst do zakodowania: <input type="text" name="ciag_znakow"><br>
    <input type="submit" value="Zakoduj">
    </form>"""

    if request.method == 'GET':
        return post
    else:
        kod = Morse_Code(request.form['ciag_znakow'])
        tekst = f"""
        <h1> Kodowanie Morse'a </h1> <hr>
        Podano do zakodowania ciąg znaków: <pre>{request.form['ciag_znakow']}</pre> <br>
        Zakodowany w kodach Morse'a: <br> <pre>{kod.ciag_kodow}</pre>
        """
        return tekst

# definiujemy akcję związaną z URL: "/koduj"
@app.route('/koduj/<name>', methods=['GET'])
def zakoduj_morse(name):

    kod = Morse_Code(name)
    tekst = f"""
    <h1> Kodowanie Morse'a </h1> <hr>
    Podano do zakodowania ciąg znaków: <pre>{name}</pre><br>
    Zakodowany w kodach Morse'a: <br> <pre>{kod.ciag_kodow}</pre>
    """
    return tekst

# start - uruchamiamy serwer WWW pod adresem http://127.0.0.1:5000
app.run()
