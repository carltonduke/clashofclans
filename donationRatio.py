import requests
import json
import numpy as np

# Set clan tag, API endpoint and REST method
headers = {'Authorization': 'Bearer '
                            ''}
endpoint = 'https://api.clashofclans.com/v1/clans/'
clanTag = '%232QCJGUCJQ'
addTag = '/'
apiMethod = 'members'
addTag1 = '?'
limit = "limit=100"

endpoint = endpoint + clanTag + addTag + apiMethod + addTag1 + limit
response = requests.get(endpoint, headers=headers).text
jsonOut = json.loads(response)

# Parse returned json file, store clan member's:names, troops donated, and troops received
numMembers = len(jsonOut["items"])
names = []
donations = np.empty((numMembers, 2), dtype=int)
ctr = 0

for elem in jsonOut["items"]:
    names.append(elem["name"])
    # print(elem["tag"])

    if elem["donations"] is not None:
        donations[ctr, 0] = elem["donations"]
    if elem["donationsReceived"] is not None:
        donations[ctr, 1] = elem["donationsReceived"]
    ctr += 1

    # Find ratio of troops donated to troops received for each member and print
for x in range(numMembers-1):
    if donations[x, 0] != 0 and donations[x, 1] != 0:
        ans = round(donations[x, 0] / donations[x, 1], 2)
    elif donations[x, 0] == 0 and donations[x, 1] != 0:
        ans = round(1/donations[x, 1], 4)
    elif donations[x, 1] == 0:
        ans = donations[x, 0]
    elif donations[x, 0] == 0 and donations[x, 1] == 0:
        ans = 0
    ans = round(ans * donations[x, 0], 4)
    print(names[x] + " -- Donation Ratio: % " + str(ans))
