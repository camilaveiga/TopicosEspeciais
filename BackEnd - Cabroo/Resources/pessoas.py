from flask_restful import Resource, reqparse

pessoas = [
    {
        'Id': 1,
        'Nome': 'Bruno',
        'Idade': 24
    },
    {
        'Id': 2,
        'Nome': 'Jacqueline',
        'Idade': 27
    },
    {
        'Id': 3,
        'Nome': 'Deise',
        'Idade': 42
    },
]


class Pessoas(Resource):
    def get(self):
        return {'pessoas': pessoas}


class Pessoa(Resource):
    def get(self, Id):
        for pessoa in pessoas:
            if pessoa['Id'] == Id:
                return pessoa
        return {'message': 'Pessoa não encontrada'}, 404

    def post(self, Id):
        argumentos =  reqparse.RequestParser()

        argumentos.add_argument('Nome')
        argumentos.add_argument('Idade')

        dados = argumentos.parse_args()

        cadastrarPessoa = {
            'Id': Id,
            'Nome': dados['Nome'],
            'Idade': dados['Idade']
        }

        pessoas.append(cadastrarPessoa)
        return cadastrarPessoa, 200

    def put(self, Id):
        pass

    def delete(self, Id):
        pass
