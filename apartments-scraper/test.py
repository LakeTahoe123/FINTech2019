import csv, re

fd = open('output.csv')
data = list(csv.reader(fd))

addr = data[5][2] #address
address = addr[addr.find("[")+1:addr.find("]")]
print(address)
rent = data[5][4].split()) #rent
if len(rent) == 3:
	rent_min = int(rent[0][1:])
	rent_max = int(rent[2])
elif len(rent) == 1:
	rent_min = int(rent[1:])
	rent_max = 0
else:
	print('Edge case at index: ')
print(float(data[5][8])) #distance
print(int(data[5][9])) #time
print(data[5][21]) #picture url

s = data[5][21]
print(s[s.find('(')+1 : s.find(')')])

'''

for i in data[5]:
	print(i)
'''
