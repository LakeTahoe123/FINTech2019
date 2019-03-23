import csv, json

fd = open('output.csv')
data = list(csv.reader(fd))

output = {}
for i in range(1, len(data)):
	listing = {}
	###listing['id'] = i - 1
	addr = data[i][2] #address
	addr = addr[addr.find('[')+1 : addr.find(']')]
	listing['address'] = addr
	listing['rent'] = data[i][4]
	listing['distance'] = data[i][8]
	listing['time'] = data[i][9]
	url = data[i][21] #picture url
	listing['picture_url'] = url[url.find('(')+1 : url.find(')')]
	output[i - 1] = listing

with open('list.json', 'w') as fd:
	fd.write(json.dumps(output))
