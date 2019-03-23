import csv, re

fd = open('output.csv')
data = list(csv.reader(fd))

addr = data[5][2] #address
address = addr[addr.find("[")+1:addr.find("]")]
print(address)
print(data[5][4]) #rent
print(data[5][8]) #distance
print(data[5][9]) #time
print(data[5][21]) #picture url

s = data[5][21]
print(s[s.find('(')+1 : s.find(')')])

'''

for i in data[5]:
	print(i)
'''
