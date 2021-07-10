n = int(input())
glassesArr = [int(numStr) for numStr in input().split(' ')]
glassesPerTable = sum(glassesArr)//n

costLR = 0
glassesMoving = 0
glassesArrLR = glassesArr[:]

for _ in range(2):
  for i in range(n):
    costLR += glassesMoving

    if (glassesArrLR[i] > glassesPerTable):
      glassesMoving += glassesArrLR[i] - glassesPerTable
      glassesArrLR[i] = glassesPerTable
    elif (glassesArrLR[i] < glassesPerTable):
      minNum = min((glassesPerTable -
                    glassesArrLR[i]), glassesMoving)
      glassesArrLR[i] += minNum
      glassesMoving -= minNum

costRL = 0
glassesMoving = 0
glassesArrRL = glassesArr[::-1]

for _ in range(2):
  for i in range(n):
    costRL += glassesMoving

    if (glassesArrRL[i] > glassesPerTable):
      glassesMoving += glassesArrRL[i] - glassesPerTable
      glassesArrRL[i] = glassesPerTable
    elif (glassesArrRL[i] < glassesPerTable and glassesMoving > 0):
      minNum = min((glassesPerTable -
                    glassesArrRL[i]), glassesMoving)
      glassesArrRL[i] += minNum
      glassesMoving -= minNum

print(min(costLR, costRL))
