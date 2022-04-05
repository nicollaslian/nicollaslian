#veiculo.py

#classe mãe -> genérica
class Veiculo:

    #construtor ou inicializador da classe
    def __init__(self,marca,modelo,ano):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano

    #funções no padrao __xxx__ são chamadas funções builtin
    def __str__(self):
        return f'Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}'
    #comportamentos, funções ou métodos da classe Veiculo
    def ligar(self):
        print('Veículo ligando...')

    def desligar(self):
        print('Veículo desligado...')

    def abastecer(self):
        print('Veículo abastecendo...')

    def acelerar(self):
        print('Veículo acelerando... Vrum... Vrum...')

    def freiar(self):
        print('Veículo freiando...')

#classe Carro é filha de Veiculo -> logo, Carro é um veiculo
#processo de herança, no qual a classe filha HERDA as funções da classe mãe
class Carro(Veiculo):

    #construtor ou inicializador da classe
    def __init__(self,marca,modelo,placa,ano):
        self.marca=marca
        self.modelo=modelo
        self.placa=placa
        self.ano=ano
        
        
class Motocicleta(Veiculo):

        #construtor ou inicializador da classe
    def __init__(self,marca,modelo,placa,ano,cilindrada):
        self.marca=marca
        self.modelo=modelo
        self.placa=placa
        self.ano=ano
        self.cilindrada=cilindrada

        
if __name__=='__main__':
    #objeto         Classe
    #porsche     =   Veiculo('Chevrolet','porsche','NIC-0114$',2030)
    porsche=Carro ('Chevrolet','porsche','NIC-0114$',2030)
    porsche.ligar()
    porsche.desligar()
    porsche.abastecer()
    porsche.acelerar()
    porsche.freiar()
    print(porsche)
    print('Placa: '+porsche.placa)

    moto=Motocicleta('Harley','CG 160 Titan', 'XYZ-4321',2021,800)
    print(moto)
    print('Placa: '+porsche.placa)
