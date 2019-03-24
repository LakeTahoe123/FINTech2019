import csv, json

fd = open('output.csv')
data = list(csv.reader(fd))

output = {}
counter = 1
index = 0
while counter < len(data):
	add = True
	listing = {}
	addr = data[counter][2] #address
	addr = addr[addr.find('[')+1 : addr.find(']')]
	listing['address'] = addr
	rent = data[counter][4].split() #rent
	if type(rent) == list and len(rent) == 3:
		try:
			rent = int(rent[0][1:].replace(',', ''))
		except:
			add = False
	elif len(rent) == 1:
		try:
			rent = int(rent[0][1:].replace(',', ''))
		except:
			add = False
		rent_max = 0
	else:
		print('Edge case at index: %s' % i)
	listing['rent'] = rent
	listing['distance'] = round(float(data[counter][8].split()[0]), 2)
	listing['time'] = int(data[counter][9].split()[0])
	url = data[counter][21] #picture url
	listing['img_url'] = url[url.find('(')+1 : url.find(')')]
	if add:
		output[index] = listing
		index += 1
		counter += 1
	else:
		counter += 1

with open('list.json', 'w') as fd:
	fd.write(json.dumps(output))

print(len(output))
