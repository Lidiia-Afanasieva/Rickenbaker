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


precision = 14
dictX = {}
dictY = {}
matchMatrix = []  # x*y
# координаты по Ох двигаем вправо (новое начало абсцисс - влево)
# координаты по Оу двигаем вверх(новое начало ординат - вниз)

countOfTargets = int(input())
xCoordOfTargets = []
yCoordOfTargets = []

for i in range(countOfTargets):
    X, Y = map(float, input().split())
    xCoordOfTargets.append(X)
    yCoordOfTargets.append(Y)

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
        round((((indexKeysX[item[1]]) ** 2 + (indexKeysY[item[0]]) ** 2) ** 0.5), precision))  # вспомни, почему наоброт


print(maxEl, "%.5f" % min(distanceFromOrigin))
