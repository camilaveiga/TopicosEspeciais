from flask import Flask
from flask_restful import Api
from Resources.pessoas import Pessoas, Pessoa

app = Flask(__name__)
api = Api(app)

api.add_resource(Pessoas, '/pessoas')
api.add_resource(Pessoa, '/pessoas/<int:Id>')

if __name__ ==  '__main__':
    app.run(debug=True)