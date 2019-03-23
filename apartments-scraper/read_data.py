import csv

fd = open('output.csv')
data = list(csv.reader(fd))

output = []
titles = True
for i in range(len(data)):
	if titles:
		titles = False
		continue

	listing = []
	addr = data[i][2] #address
	addr = addr[addr.find('[')+1 : addr.find(']')]
	listing.append(addr)
	listing.append(data[i][4]) #rent
	listing.append(data[i][8]) #distance
	listing.append(data[i][9]) #time
	output.append(listing)

print(len(output))
