import json
with open('nermin.json','r') as kimlik:
	kimlik_n=json.load(kimlik)
for item in kimlik_n.values():
	print(item)
