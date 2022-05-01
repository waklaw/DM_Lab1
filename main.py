from prettytable import PrettyTable


def getFile():
    text = []
    with open("data.txt", "r") as file:
        lines = file.readlines()
        for i in lines:
            text.append(i.replace('\n', ''))
    for i in range(len(text)):
        text[i] = text[i].split(" ")
    return text


def prima(N, G):
    selected_node = [0 for i in range(N)]
    no_edge = 0
    selected_node[0] = True

    table = PrettyTable(['Edge', 'Weight'])
    while no_edge < N - 1:
        minimum = 9999999
        a = 0
        b = 0

        for m in range(N):
            if selected_node[m]:
                for n in range(N):
                    if (not selected_node[n]) and G[m][n]:
                        if minimum > G[m][n]:
                            minimum = G[m][n]
                            a = m
                            b = n
        table.add_row([f"{chr(65 + a)} -> {chr(65 + b)}", G[a][b]])
        selected_node[b] = True
        no_edge += 1
    print(table)


if __name__ == '__main__':
    array = getFile()
    array = [[int(j) if '.' not in j else float(j) for j in i] for i in array]
    numberOfNodes = int(array[0][0])
    matrix = array[1:]

    table = PrettyTable([chr(i) for i in range(65, 65 + numberOfNodes)])
    for i in matrix:
        table.add_row(i)
    print(table)

    prima(numberOfNodes, matrix)
