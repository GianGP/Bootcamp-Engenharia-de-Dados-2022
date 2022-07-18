import datetime
import math
from typing import List


""" class Pessoa:
    def __init__(self, nome: str, sobrenome: str, data_de_nascimento: datetime.date):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_de_nascimento = data_de_nascimento
    
    @property
    def idade(self) -> int:
        return math.floor((datetime.date.today() - self.data_de_nascimento).days/365.2425)

    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome} tem {self.idade} anos'

class Curriculo:
    def __init__(self, pessoa: Pessoa, experiencias: List[str]) -> None:
        self.pessoa = pessoa
        self.experiencias = experiencias
    
    @property
    def qtde_experiencias(self) -> int:
        return len(self.experiencias)
    
    @property
    def empresa_atual(self) -> str:
        return self.experiencias[-1]
    
    def adiciona_experiencia(self, experiencia: str) -> None:
        self.experiencias.append(experiencia)

    def __str__(self) -> str:
        return f'{self.pessoa.nome} {self.pessoa.sobrenome} tem {self.pessoa.idade} anos e já ' \
               f'trabalhou em {self.qtde_experiencias} empresas e atualmente trabalha '\
               f'na empresa {self.empresa_atual}'


gian = Pessoa(nome='Gian', sobrenome='Panacioni', data_de_nascimento=datetime.date(1998,8,4))

curriculo_gian = Curriculo(pessoa=gian, experiencias=['PET', 'Eletrizar', 'Yapira', 'Everywhere Analytics', 'DP6'])

print(curriculo_gian)
curriculo_gian.adiciona_experiencia('Empresa')
print(curriculo_gian)
"""


class Vivente:
    def __init__(self, nome: str, data_de_nascimento: datetime.date) -> None:
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
    
    @property
    def idade(self):
        return math.floor((datetime.date.today() - self.data_de_nascimento).days/365.2425)
    
    def emite_ruido(self, ruido: str):
        print(f'{self.nome} fez ruido: {ruido}')
    

class PessoaHeranca(Vivente):
    def __str__(self) -> str:
        return f'{self.nome} tem {self.idade} anos'

    def fala(self, frase):
        return self.emite_ruido(frase)
        
class Cachorro(Vivente):
    def __init__(self, nome: str, data_de_nascimento: datetime.date, raca: str) -> None:
        super().__init__(nome, data_de_nascimento) 
        self.raca = raca

    def __str__(self) -> str:
        return f'{self.nome} é da raça {self.raca} e tem {self.idade} anos'

    def late(self):
        return self.emite_ruido('Au! Au!')


gian2 = PessoaHeranca(nome='Gian', data_de_nascimento=datetime.date(1998,8,4))

print(gian2)

moana = Cachorro(nome='Moana', data_de_nascimento=datetime.date(2016,4,2), raca='Vira-lata')

print(moana)

moana.late()
moana.late()
moana.late()
moana.late()
moana.late()

gian2.fala('Deu né')