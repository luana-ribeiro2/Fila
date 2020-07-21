class Fila():
    def __init__(self):
        self.__items = []

    def __repr__(self):
        return repr(self.__items)

    def __str__(self):
        return str(self.__items)

    def __len__(self):
        return len(self.__items)

    def primeiro(self):
        return self.__items[0]

    def inserir(self, item):
        self.__items.append(item)

    def dequeue(self):
        item = self.__items[0]
        del self.__items[0]
        return item

testes = Fila()
teste = int(input())
for i in range(teste):
    print('Caso ' + str(i + 1) + ':')
    comandos = int(input())
    identificacaoRegular = Fila()
    identificacaoPreferencial = Fila()
    for j in range(comandos):
        comando = input()

        if comando[0] == 'f':
            identificacao = int(comando[2:])
            identificacaoRegular.inserir(identificacao)
        elif comando[0] == 'p':
            identificacao = int(comando[2:])
            identificacaoPreferencial.inserir(identificacao)
        elif comando[0] == 'A':
            if len(identificacaoRegular) > 0:
                identificacaoRegular.dequeue()
            elif len(identificacaoPreferencial) > 0:
                identificacaoPreferencial.dequeue()
        elif comando[0] == 'B':
            if len(identificacaoPreferencial) > 0:
                identificacaoPreferencial.dequeue()
            elif len(identificacaoRegular) > 0:
                identificacaoRegular.dequeue()
        elif comando[0] == 'I':
            regular = 0
            preferencial = 0
            if len(identificacaoRegular) > 0:
                regular = identificacaoRegular.primeiro()
            if len(identificacaoPreferencial) > 0:
                preferencial = identificacaoPreferencial.primeiro()
            print(regular, preferencial)
