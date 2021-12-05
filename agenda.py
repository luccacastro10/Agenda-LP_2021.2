import os

path = "lista.txt"

def main():
    print("\n -------------------------------------------")
    print(" ---              Agenda.py              ---")
    print(" -------------------------------------------")

    comandos()
    
    while True:
        if (lerComando() == False):
            break


def lerComando():
    comando = input("\nEntre com o comando: ")
    agenda = open(path, "r+")
    lines = agenda.readlines()

    if (comando == 'rd' or comando == "read"):
        ler(lines)
        return True

    if (comando == 'w'or comando == "write"):
        escrever(agenda)
        return True

    elif (comando == 'rm' or comando == "remove"):
        remover(agenda, lines)
        return True

    elif (comando == 's' or comando == "search"):
        buscar(lines)
        return True

    elif (comando == 'h' or comando == "help"):
        comandos()
        return True

    elif (comando == 'c' or comando == "close"):
        agenda.close()
        print("A agenda foi finalizada com sucesso\n")
        return False

    else:
        print("Nenhum comando válido!")
        return True

def ler(lines):
    print("\n-----------------------------\n")

    for line in lines:
        print(line)
    print("-----------------------------")

def escrever(agenda):

    nome = input("\nEntre com o nome: ")
    end = input("Entre com o endereço: ")
    contato = input("Entre com o contato: ")

    agenda.writelines( nome + ", " + end + ", " + contato + "\n")
    print("Agenda atualizada!")

def remover(agenda, lines):
    print("\nPrimeiramente busque pela informação que quer remover!")
    lineAt = buscar(lines)

    rmLines = []
    i = 1
    n = "\n"

    for rm in lineAt:

        if rm != lineAt[0]:
            n = ""

        cmd = input( n + "Deseja remover a linha %i da agenda? (s/n) " % rm)

        if (cmd == "s"):
            rmLines.append(rm)
        if (cmd == "n"):
            pass

    if len(rmLines) != 0:
        agenda.close()
        agendaAux = open(path, "w")

        for j in rmLines:
            lines.pop(j-i)
            i += 1

        for line in lines:
            agendaAux.write(line)

        agendaAux.close()
        print("Linhas removidas com sucesso!")
    else:
        print("Nenhuma linha foi removida")

def buscar(lines):
    
    busca = input("\nEntre com a informação que quer buscar: ")
    j = 1
    i = 0
    lista = []
    n = "\n"

    for line in lines:
        info = line.find(busca)

        if(info != -1):
            if line != lines[0]:
                n = ""
            line = line.split("\n")
            print(n + line[0] + " -> Linha %i" %j)
            lista.insert(i, j)
            i += 1
    
        j += 1

    if not i:
        print("Informação não encontrada!")
        
    return lista

def comandos():
    print("\nLista de comandos: \n")
    print("read:   Lê a agenda por competo        | rd")
    print("write:  Adiciona informações na agenda | w")
    print("remove: Remove informações da agenda   | rm")
    print("search: Busca informações na agenda    | s")
    print("close:  Salva e finaliza o programa    | c")
    print("help:   Retorna à lista de comandos    | h\n")
    

if __name__ == '__main__': 
    main() 