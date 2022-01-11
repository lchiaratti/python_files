class Programa:
    def __init__(self, nome, ano):
      self._nome = nome.title()
      self.ano = ano
      self._likes = 0
    
    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.likes} Likes'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
      super().__init__(nome, ano)
      self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {programa.likes} Likes'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
      super().__init__(nome, ano)
      self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {programa.likes} Likes'
    


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
#print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} '
#      f' - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')


atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
#rint(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} '
#      f' - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')


filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:    
    #detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    #if hasattr(programa, 'duracao'):
    #    detalhes = programa.duracao
    #else:
    #    detalhes = programa.temporadas

    #print(f'Nome: {programa.nome} - {detalhes} - Likes: {programa.likes}')
    #programa.imprime()
    print(programa)
