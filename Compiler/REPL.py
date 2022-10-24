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

class Frame:
    def __init__(self, ctx):
        self.ctx = ctx

    def add_data(self):
        repl = REPL()
        repl.datas.append(self.data)
    def visit(self, args):
        self.scopes = [0]
        self.data = HashMap()
        self.add_data()
        self.args = args
        repl = REPL()
        self.scope = len(repl.datas) - 1
    def addScope(self, scope):
        self.scopes.append(scope)

    def setNext(self, next):
        self.next.append(next)

    def setPrev(self, prev):
        self.prev = prev

    def getCtx(self):
        return self.ctx

    def getScopes(self):
        return self.scopes

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

class REPL:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(REPL, cls).__new__(cls)
            cls.data = HashMap()
            cls.stack = []
            cls.scope = 0
            cls.datas = []
            cls.frame = Frame(None)
            cls.datas.append(cls.data)
        return cls.instance

