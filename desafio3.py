class Heroi:

    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        ataques = {
            'mago':'usando magia',
            'guerreiro':'usando espada',
            'monge':'usando artes marciais',
            'ninja':'usando shuriken'
        }

        ataque = ataques.get(self.tipo, 'fez um ataque padrão.')
        print(f'o {self.tipo} atacou {ataque}')

personagem = Heroi('Deivison', 25, 'monge')
personagem.atacar()