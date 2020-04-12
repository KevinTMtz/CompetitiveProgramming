# Python program showing  
# a use of input()

queries = input()
toPrint = ""
message = ""

for i in range(queries):
    message = message + raw_input()
  
num = 15  
while(num<len(message)):
    if not(message[num]=='X' and (message[num-1]=='O' or message[num-1]=='I')):
        toPrint = toPrint + message[num]
    num = num + 16
    
size = ord(toPrint[len(toPrint)-1])-64

option = toPrint[:len(toPrint)-1]
if option == "TRIANGULO" and len(toPrint)==10:
    for i in range(size):
        print ('*'*(i+1))
elif option == "CUADRADO" and len(toPrint)==9:
    for i in range(size):
        print ('*'*(size))
elif option == "PIRAMIDE" and len(toPrint)==9:
    for i in range(size):
        print (' '*(size-i-1)+'*'*(1+i*2))
else:
    print toPrint
