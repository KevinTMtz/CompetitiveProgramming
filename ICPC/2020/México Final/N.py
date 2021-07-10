n = int(input())
balance = float(input()[1:])
counter = 0

for i in range(n):
  balance = balance + float(input()[1:])

  if (balance - int(balance) > 0):
    counter += 1

print(counter)
