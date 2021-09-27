import math
def to2Dcoord(index, m, n):  # для матрицы размером m*n (i*j)
    return (index % (n), index // (n))


def mathes(A, B):
    A.sort()
    B.sort()
    quan = 0
    if len(A) != len(B):
        A, B = max(A, B), min(A, B)
    for a in A:
        for b in B:
            if a == b:
                quan += 1
    return (quan)


def lastHope(dictX, dictY):
    indexKeysX = []
    indexKeysY = []

    for i in dictX:
        for j in dictY:
            matchMatrix.append(mathes(dictX[i], dictY[j]))
            indexKeysY.append(j)
        indexKeysX.append(i)


    indexMaxEl = []
    maxEl = max(matchMatrix)

    for i in range(len(matchMatrix)):
        if matchMatrix[i] == maxEl:
            indexMaxEl.append(i)

    pairsXY = []
    for item in indexMaxEl:
        pairsXY.append(to2Dcoord(item, len(dictX), len(dictY)))

    distanceFromOrigin = []
    for item in pairsXY:
        distanceFromOrigin.append(
            round((((indexKeysX[item[1]]) ** 2 + (indexKeysY[item[0]]) ** 2) ** 0.5),
                  precision))  # вспомни, почему наоброт


    return (maxEl, min(distanceFromOrigin))


def mathes(A, B):
    A.sort()
    B.sort()
    quan = 0
    if len(A) != len(B):
        A, B = max(A, B), min(A, B)
    for a in A:
        for b in B:
            if a == b:
                quan += 1
    return (quan)


precision = 14
dictX = {}
dictY = {}
matchMatrix = []  # x*y
# координаты по Ох двигаем вправо (новое начало абсцисс - влево)
# координаты по Оу двигаем вверх(новое начало ординат - вниз)

countOfTargets = int(input())
xCoordOfTargets = []
yCoordOfTargets = []
lastDeltasArray = []


for i in range(countOfTargets):
    X, Y = map(float, input().split())
    xCoordOfTargets.append(X)
    yCoordOfTargets.append(Y)
#вправо-вверх _ вправо-вниз _ влево-верх _ влево-низ _ к ближайшниу целому
## first flow in bigger side

#вправо-вверх
for i in range(len(xCoordOfTargets)):
    delta = round(abs(math.ceil(xCoordOfTargets[i]) - xCoordOfTargets[i]), precision)

    if delta in dictX:
        listOfRelevantX = dictX.pop(delta)
        listOfRelevantX.append(i)
        dictX[delta] = listOfRelevantX
    else:
        dictX[delta] = [i]
for i in range(len(yCoordOfTargets)):
    delta = round(abs(math.ceil(yCoordOfTargets[i]) - yCoordOfTargets[i]), precision)

    if delta in dictY:
        listOfRelevantY = dictY.pop(delta)
        listOfRelevantY.append(i)
        dictY[delta] = listOfRelevantY
    else:
        dictY[delta] = [i]
lastDeltasArray.append(lastHope(dictX, dictY))
dictX = {}
dictY = {}
matchMatrix = []

#вправо-вниз
for i in range(len(xCoordOfTargets)):
    delta = round(abs(math.ceil(xCoordOfTargets[i]) - xCoordOfTargets[i]), precision)

    if delta in dictX:
        listOfRelevantX = dictX.pop(delta)
        listOfRelevantX.append(i)
        dictX[delta] = listOfRelevantX
    else:
        dictX[delta] = [i]
for i in range(len(yCoordOfTargets)):
    delta = round(abs(math.floor(yCoordOfTargets[i]) - yCoordOfTargets[i]), precision)

    if delta in dictY:
        listOfRelevantY = dictY.pop(delta)
        listOfRelevantY.append(i)
        dictY[delta] = listOfRelevantY
    else:
        dictY[delta] = [i]
lastDeltasArray.append(lastHope(dictX,dictY))

dictX = {}
dictY = {}
matchMatrix = []

#влево-вверх
for i in range(len(xCoordOfTargets)):
    delta = round(abs(math.floor(xCoordOfTargets[i]) - xCoordOfTargets[i]), precision)

    if delta in dictX:
        listOfRelevantX = dictX.pop(delta)
        listOfRelevantX.append(i)
        dictX[delta] = listOfRelevantX
    else:
        dictX[delta] = [i]
for i in range(len(yCoordOfTargets)):
    delta = round(abs(math.ceil(yCoordOfTargets[i]) - yCoordOfTargets[i]), precision)

    if delta in dictY:
        listOfRelevantY = dictY.pop(delta)
        listOfRelevantY.append(i)
        dictY[delta] = listOfRelevantY
    else:
        dictY[delta] = [i]
lastDeltasArray.append(lastHope(dictX,dictY))

dictX = {}
dictY = {}
matchMatrix = []

#left-down
for i in range(len(xCoordOfTargets)):
    delta = round(abs(math.floor(xCoordOfTargets[i]) - xCoordOfTargets[i]), precision)

    if delta in dictX:
        listOfRelevantX = dictX.pop(delta)
        listOfRelevantX.append(i)
        dictX[delta] = listOfRelevantX
    else:
        dictX[delta] = [i]
for i in range(len(yCoordOfTargets)):
    delta = round(abs(math.floor(yCoordOfTargets[i]) - yCoordOfTargets[i]), precision)

    if delta in dictY:
        listOfRelevantY = dictY.pop(delta)
        listOfRelevantY.append(i)
        dictY[delta] = listOfRelevantY
    else:
        dictY[delta] = [i]
lastDeltasArray.append(lastHope(dictX,dictY))

dictX = {}
dictY = {}
matchMatrix = []

for i in range(len(xCoordOfTargets)):
    delta = round(abs(round(xCoordOfTargets[i]) - xCoordOfTargets[i]), precision)

    if delta in dictX:
        listOfRelevantX = dictX.pop(delta)
        listOfRelevantX.append(i)
        dictX[delta] = listOfRelevantX
    else:
        dictX[delta] = [i]

for i in range(len(yCoordOfTargets)):
    delta = round(abs(round(yCoordOfTargets[i]) - yCoordOfTargets[i]), precision)

    if delta in dictY:
        listOfRelevantY = dictY.pop(delta)
        listOfRelevantY.append(i)
        dictY[delta] = listOfRelevantY
    else:
        dictY[delta] = [i]

lastDeltasArray.append(lastHope(dictX,dictY))

dictX = {}
dictY = {}
matchMatrix = []
r=-1
lastDeltasArray.sort(reverse=True)
#print(lastDeltasArray)
for i in range(len(lastDeltasArray)-1):
    if lastDeltasArray[i][0]!=lastDeltasArray[i+1][0]:
        r=lastDeltasArray[i][1]
else:
    if r==-1:
        r=lastDeltasArray[len(lastDeltasArray)-1][1]
print(lastDeltasArray[0][0], "%.5f" % r)
