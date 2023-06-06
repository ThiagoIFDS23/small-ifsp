N = int(input())
contador = []
for i in range(0, 101):
    contador.append([False, 0])

i = 1
while i <= N:
    x = input()
    x = x.split()
    tipo = x[0]
    amigo = int(x[1])

    if tipo == "R" or tipo == "E":
        for amiguinho in contador:
                    if amiguinho[0] == True:
                        amiguinho[1]+=1

    if tipo == "R":
        contador[amigo][0] = True
    elif tipo == "E":
        contador[amigo][0] = False
    elif tipo == "T":
        for amiguinho in contador:
                    if amiguinho[0] == True:
                        amiguinho[1]+=amigo-1
    i += 1

i = 1

while i <= 100:
    if contador[i][0] == True:
        print(str(i) + " -1")
    else:
        if contador[i][1] != 0:
            print(str(i) + " " + str(contador[i][1]))
    i += 1
