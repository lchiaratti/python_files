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
    

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
        #super().__init__(programas)
    
    def __getitem__(self, item):
        return self._programas[item]
    
    @property
    def listagem(self):
        return self._programas

    #@property
    def __len__(self):
        return len(self._programas)
    
 #   def tamanho(self):
 #      return len(self.programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

#print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} '
#      f' - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()
#rint(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} '
#      f' - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')


filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playslist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da Playlist: {len(playslist_fim_de_semana)}')

print(vingadores in playslist_fim_de_semana)

#print(playslist_fim_de_semana[0])


#for programa in filmes_e_series:
for programa in playslist_fim_de_semana:    
    #detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    #if hasattr(programa, 'duracao'):
    #    detalhes = programa.duracao
    #else:
    #    detalhes = programa.temporadas

    #print(f'Nome: {programa.nome} - {detalhes} - Likes: {programa.likes}')
    #programa.imprime()
    print(programa)

print(f'Tá ou não tá? {demolidor in playslist_fim_de_semana}')