symbolTable = []

INT = 'int'
FLOAT = 'float'
STRING = 'string'
BOOL = 'boolean'
TYPE = 'type'
PARAMS = 'params'
BINDABLE = 'bindable'
FUNCTION = 'fun'
VARIABLE = 'var'
SCOPE = 'scope'

DEBUG = 0
Number = [INT, FLOAT]

def printTable():
    global DEBUG
    if DEBUG == -1:
        print('Tabela:', symbolTable)

def beginScope(nameScope):
    global symbolTable
    symbolTable.append({})
    symbolTable[-1][SCOPE] = nameScope

def getBindable(bindableName):
    global symbolTable
    for i in reversed(range(len(symbolTable))):
        if (bindableName in symbolTable[i].keys()):
            return symbolTable[i][bindableName]
    return None

def addVar(name, type):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: VARIABLE, TYPE : type}

def addFunction(name, params):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: FUNCTION, PARAMS: params}

def endScope():
    global symbolTable
    symbolTable.pop()

def main():
    global DEBUG
    DEBUG = -1
    print('\n# Criando escopo main')
    beginScope('main')
    print ('\n# Adicionando Vinculavel funcao some')
    addFunction('some', ['a', INT, 'b', INT], INT)
    print('\n# Criando escopo some')
    beginScope('some')
    print('\n# Adicionando var a do tipo int')
    addVar('a', INT)
    print('\n# Adicionando var b do tipo int')
    addVar('b', INT)
    print('\n# Consultando bindable')
    print(str(getBindable('sumparabola')))
    print('\n# Consultando bindable')
    print(str(getBindable('some')))
    print('\n# Removendo escopo some')
    endScope()

if __name__ == "__main__":
    main()