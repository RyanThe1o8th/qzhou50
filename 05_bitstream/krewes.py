'''
Qianjun(Ryan) Zhou
Boa's
SoftDev
<Learning how read and use a file>
2024-09-17
.5
'''
import random

file = open("krewes.txt", "r")
krewes = {}

data=file.read()

data = data.replace("@", "$")
outputdata = ""
for i in range(len(data) -1):
    if not(i != 0 and data[i] == "$" and data[i - 1] == "$"):
        outputdata = outputdata + data[i]

#print (outputdata)

data = outputdata
table = data.split("$")
#print(table)
keyVal = 0


#brute force to remove index 0
i = 0
while i<(len(table)-1):
    if(table[i].isnumeric()):
        keyVal = int(table[i])
        if (not(keyVal in krewes)):
            krewes[keyVal] = []
    else:
        krewes[keyVal].append("name: " + table[i] + "\nduckie: " + table[i+1])
        i+=1
    i+=1

a = (random.choice(list(krewes)))
print("period: " + str(a))
b = (random.choice(list(krewes[a])))
print(b)