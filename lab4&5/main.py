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


def tokenize(text):
    tokens = text.replace('+', ' + ') \
                 .replace('-', ' - ') \
                 .replace('*', ' * ') \
                 .replace('/', ' / ') \
                 .replace('==', ' == ') \
                 .replace('<=', ' <= ') \
                 .replace('>=', ' >= ') \
                 .replace('<', ' < ') \
                 .replace('>', ' > ') \
                 .replace('=', ' = ') \
                 .replace('{', ' { ') \
                 .replace('}', ' } ') \
                 .replace('(', ' ( ') \
                 .replace(')', ' ) ') \
                 .replace('[', ' [ ') \
                 .replace(']', ' ] ') \
                 .replace('%', ' % ') \
                 .replace('<<', ' >> ') \
                 .replace('"', ' " ') \
                 .replace(',', ' , ') \
                 .replace('#', ' # ') \
                 .replace(':', ' : ') \
                 .replace('&&', ' && ') \
                 .replace('||', ' || ') \
                 .split()

    return tokens
def isIdentifier(string):
    if "_" in string:
        if string[0] =="_":
            return string[1:].isalnum()
        else:
            return False
    else:
        return string.isalnum()
def scan(programs_file_content,token_file_content):
    symbol_table = SymbolTable(100)
    PIF = []

    programs_lines = programs_file_content.splitlines()
    line_number = 0
    error_message = ""

    token_lines=token_file_content.splitlines()

    for line in programs_lines:
        line_number += 1
        tokens = tokenize(line)
      #  print(f"Tokens in line {line_number}: {tokens}")
        flag=0
        for token in tokens:
            if token in token_lines:
                PIF.append((token, -1))
                if token=="\"" or token=="#":
                    if flag==0 :
                        flag=1
                    else:
                        flag=0
                continue
            if flag==0:
                if isIdentifier(token):
                    value = symbol_table.lookup(token)
                    if value is None:
                        symbol_table.insert(token, "Identifier")
                    PIF.append((token, symbol_table.hash(token)))
                else:
                    error_message = f"Lexical error at line {line_number}: {token}"
                    print(error_message)
                    break

    return symbol_table, PIF

if __name__ == '__main__':
    programs_file_path = 'programs.txt'
    try:
        with open(programs_file_path, 'r') as programs_file:
            programs_file_content = programs_file.read()
        print("File read successfully.")
    except FileNotFoundError:
        print("File not found. Please provide the correct file path.")

    tokens_file_path = 'token.in'
    try:
        with open(tokens_file_path, 'r') as tokens_file:
            tokens_file_content = tokens_file.read()
        print("File read successfully.")
    except FileNotFoundError:
        print("File not found. Please provide the correct file path.")

    symbol_table, PIF = scan(programs_file_content,tokens_file_content)

    with open('ST.out', 'w') as st_out:
        for i, bucket in enumerate(symbol_table.table):
            if bucket:
                st_out.write(f"Table {i}: {', '.join(entry[0] for entry in bucket)}\n")

    with open('PIF.out', 'w') as pif_out:
        for entry in PIF:
            pif_out.write(f"{entry[0]}, {entry[1]}\n")
