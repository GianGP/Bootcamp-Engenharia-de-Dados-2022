import datetime
import math

class Pessoa:
    def __init__(self, nome: str, sobrenome: str, data_de_nascimento: datetime.date):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_de_nascimento = data_de_nascimento
    
    @property
    def idade(self) -> int:
        return math.floor((datetime.date.today() - self.data_de_nascimento).days/365.2425)

    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome} tem {self.idade} anos'

gian = Pessoa(nome='Gian', sobrenome='Panacioni', data_de_nascimento=datetime.date(1998,8,4))

print(gian)
print(gian.nome)
print(gian.sobrenome)
print(gian.idade)
