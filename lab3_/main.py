class SymbolTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        hash_value = sum(ord(char) for char in key)
        return hash_value % self.size

    def insert(self, key, value):
        index = self.hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    self.table[index][i] = (key, value)
                    return
            self.table[index].append((key, value))

    def lookup(self, key):
        index = self.hash(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

    def delete(self, key):
        index = self.hash(key)
        if self.table[index] is not None:
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    del self.table[index][i]
                    return


sym_table = SymbolTable(100)
sym_table.insert("x", 42)
sym_table.insert("y", 30)
sym_table.insert("z", 15)

print(sym_table.lookup("x")) 
print(sym_table.lookup("y"))  
print(sym_table.lookup("z"))  

sym_table.delete("y")
print(sym_table.lookup("y"))