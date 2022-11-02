class HashMap:
    def __init__(self):
        self.size = 1024
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
                else:
                    self.map[key_hash].append(list([key_value]))
                    return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None :
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def print(self):
        for item in self.map:
            if item is not None:
                print(str(item))

class REPL:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(REPL, cls).__new__(cls)

            #las siguientes variables son para el manejo de las datas en visitor
            cls.data = HashMap()# data general
            #los indices de las datas a la que las funciones acceden
            cls.datas_indices = [0]

            #almacena las datas, la principal siempre está.
            cls.datas = [cls.data]

            #indice el indice disponible para la data, aumenta y decrementa según se empiece y termine una llamada a función
            cls.indice_datas = 1

            #pila general
            cls.stack = []
        return cls.instance

    def add_data(self, data):
        #se aumenta el indice de datas para que la siguiente data se guarde en la siguiente posición
        self.indice_datas += 1
        #se crea una nueva data y se agrega a la lista de datas
        self.datas.append(data)

    def del_data(self):
        #se decrementa el indice de datas para que la siguiente data se guarde en la siguiente p
        self.indice_datas -= 1
        #se elimina la data actual de la lista de datas
        self.datas.pop()