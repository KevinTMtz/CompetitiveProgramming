import math

temp = input().split(' ')
n = int(temp[0])
x = int(temp[1])

startTimeArr = []
durationArr = []

for i in range(n):
  temp = input().split(' ')
  startTimeArr.append(int(temp[0]))
  durationArr.append(int(temp[1]))

startTime = 0
conflicts = float('inf')

for j in range(0, 481):
  tempConflicts = 0

  for i in range(n):
    multiple = math.floor((startTimeArr[i]-j)/x)*x+j
    while(multiple <= startTimeArr[i] + durationArr[i]):
      if (multiple >= startTimeArr[i] and multiple <= startTimeArr[i] + durationArr[i] and j <= multiple):
        tempConflicts += 1
      multiple += x

  if (tempConflicts < conflicts):
    startTime = j
    conflicts = tempConflicts

print(startTime, conflicts)
