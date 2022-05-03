class Produto:

    def __init__(self, descricao, preco, quantidade, id):
        self.__id = id
        self.__descricao = descricao
        self.__preco = preco
        self.__quantidade = quantidade

    # funções built-in do python tem formato __xxx__
    def __str__(self):
        return f'Código:  {self.id}  \nDescrição:  {self.descricao} \nPreço: R$ {self.preco:.2f} ' \
               f'\nQuantidade: {self.quantidade} '

    # propriedades permitem ler os valores, mas não deixam alterar
    @property
    def id(self):
        return self.__id

    @property
    def descricao(self):
        return self.__descricao

    @property
    def preco(self):
        return self.__preco

    @property
    def quantidade(self):
        return self.__quantidade

    # setters permitem alterar os valores dos campos
    @id.setter
    def id(self, id):
        self.__id = id

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade
