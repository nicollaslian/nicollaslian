#marvel.py

#classe mãe genérica

class Heroi:

#inicializador da classe mãe
    def __init__(self,nome):
        self.nome=nome
        
    def voar(self):
        print(f'{self.nome} voando...')

    def levantarPeso(self):
        print(f'{self.nome} levantando um caminhão...')

    def destruir(self):
        print(f'{self.nome} destruindo armas do inimigo...')

    def salvar(self):
        print(f'{self.nome} salvando pessoas...')


#Thor É UM herói
class Thor(Heroi):
    #inicializador da classe filha
    def __init__(self):
        super().__init__('Thor')

    def jogarMartelo(self):
        print('Thor jogando martelo...')

class Ironman(Heroi):
    #inicializador da classe filha
    def __init__(self):
        super().__init__('Ironman')

    def jarvis(self):
        print('Jarvis, pesquise "Qual é a temperatura ambiente?"')

class Shazam(Heroi):
    #inicializador da classe filha
    def __init__(self):
        super().__init__('Shazam')

    def trocarDeAparencia(self):
        print('Shazaaam!...')
        
thor = Thor()
thor.voar()
thor.levantarPeso()
thor.jogarMartelo()
thor.destruir()
thor.salvar()
print ()
iron=Ironman()
iron.voar()
iron.levantarPeso()
iron.destruir()
iron.salvar()
iron.jarvis()
print ()
shazam=Shazam()
shazam.voar()
shazam.levantarPeso()
shazam.destruir()
shazam.salvar()
shazam.trocarDeAparencia()
