# создать два списка пробить их по циклу к каждому прибавить значение и глянуть по счётчику максимальное
# нужно учитывать перемещение по обеим осям

countOfTargets = int(input())
xCounter = 0
yCounter = 0
temp = 0
xCounterList = []
yCounterList = []
xCoordinatesOfTargets = []
yCoordinatesOfTargets = []

for i in range(countOfTargets):
    x, y = map(float, input().split())
    xCoordinatesOfTargets.append(x)
    yCoordinatesOfTargets.append(y)


for i in range(10):
    xCounterList.append(0)
    yCounterList.append(0)

print("xCoordinatesOfTargets", xCoordinatesOfTargets)
print("yCoordinatesOfTargets", yCoordinatesOfTargets)

for i in range(len(xCounterList)):
    for j in range(countOfTargets):
        if (abs(xCoordinatesOfTargets[j]) + 0.1 * (i + 1)) // 1 > (abs(xCoordinatesOfTargets[j]) + 0.1 * (i)) // 1:
            xCounter += 1
            print("xCounter :", xCounter)
    xCounterList[i] = int(xCounter)
    xCounter = 0
print("temp : ", xCounterList.index(max(xCounterList)), "\n", xCounterList)


maxX = 1 - (xCounterList.index(max(xCounterList)) + 1) * 0.1

for i in range(len(yCounterList)):
    for j in range(countOfTargets):
        if (abs(yCoordinatesOfTargets[j]) + 0.1 * (i + 1)) // 1 > (abs(yCoordinatesOfTargets[j]) + 0.1 * (i)) // 1:
            yCounter += 1
            print("yCounter :", yCounter)
    yCounterList[i] = int(yCounter)
    yCounter = 0


maxY = 1 - (yCounterList.index(max(yCounterList)) + 1) * 0.1
print("temp : ", yCounterList.index(max(yCounterList)), "\n", yCounterList)
xMaxOfCounter = xCounterList.index(max(xCounterList))
yMaxOfCounter = yCounterList.index(max(yCounterList))
maxCountOfHit = max(xMaxOfCounter, yMaxOfCounter)
if maxCountOfHit == 0 : print()
print("answer is :", round((maxX**2 + maxY**2)**0.5, 5))

# УЧИТЫВАТЬ ПОПАДАНИЯ ЕСЛИ ПРИЦЕЛ НЕ НУЖНО ПЕРЕМЕЩАТЬ
# ПРОВЕРИТЬ НУЖНО ЛИ УЧИТЫВАТЬ ПЕРЕМЕЩЕНИЕ В ОБРАТНУЮ СТОРОНУ(ВРОДЕ НЕТ)
