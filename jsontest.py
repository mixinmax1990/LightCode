import json
data = {'people':[{'name': 'Scott', 'website': 'stackabuse.com', 'from': 'Nebraska'}, {'name': 'Danny', 'website': 'stackabuse.com', 'from': 'Nebraska'}, {'name': 'Danny', 'website': 'stackabuse.com', 'from': 'Nebraska'}]}
y = {'name': 'Susan', 'website': 'stackabuse.com', 'from': 'Nebraska'}
data['people'].append(y)
x = {'name': 'Scott', 'website': 'stackabuse.com', 'from': 'Nebraska'}
i = {'name': 'Bobbia', 'website': 'stackabuse.com', 'from': 'Nebraska'}
try:
    data['things'].append(x)
except KeyError:
    data['things'] = []
    data['things'].append(x)

try:
    data['things'].append(i)
except KeyError:
    data['things'] = []
    data['things'].append(i)

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)