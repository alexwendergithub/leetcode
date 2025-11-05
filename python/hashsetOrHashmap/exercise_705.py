class MyHashSet:
#da pra manter o array ordenado tbm e usar busca binaria tbm dai ficaria um pouco mais rapido
    def __init__(self):
        self.lista = []

    def add(self, key: int) -> None:
        if key in self.lista:
            return None
        else:
            self.lista.append(key) 

    def remove(self, key: int) -> None:
        if key in self.lista:
            self.lista.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.lista


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)