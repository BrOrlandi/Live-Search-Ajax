# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
import json
app = Flask(__name__)
app.config.update(dict(
    DEBUG=True,
))

# Usually the searchs occurs in databases, for this simple example we're using search in this array
BRAZIL_STATES = [u"Acre - Rio Branco",
u"Alagoas - Maceió",
u"Amapá - Macapá",
u"Amazonas - Manaus",
u"Bahia - Salvador",
u"Ceara - Fortaleza",
u"Distrito Federal - Brasília",
u"Espírito Santo - Vitória",
u"Goiás - Goiânia",
u"Maranhão - São Luiz",
u"Mato Grosso - Cuiabá",
u"Mato Grosso do Sul - Campo Grande",
u"Minas Gerais - Belo Horizonte",
u"Pará - Belém",
u"Paraíba - João Pessoa",
u"Paraná - Curitiba",
u"Pernambuco - Recife",
u"Piauí - Terezina",
u"Rio de Janeiro - Rio de Janeiro",
u"Rio Grande do Norte - Natal",
u"Rio Grande do Sul - Porto Alegre",
u"Rondônia - Porto Velho",
u"Roraima - Boa Vista",
u"Santa Catarina - Florianópolis",
u"São Paulo - São Paulo",
u"Sergipe - Aracajú",
u"Tocantins - Palmas"]


@app.route("/")
def index():
    return render_template("index.html") # render the page

@app.route("/search")
def search():
	text = request.args['searchText'] # get the text to search for
	# create an array with the elements of BRAZIL_STATES that contains the string
	# the case is ignored
	result = [c for c in BRAZIL_STATES if unicode(text).lower() in c.lower()]
	# return as JSON
	return json.dumps({"results":result}) 

if __name__ == "__main__":
    app.run()