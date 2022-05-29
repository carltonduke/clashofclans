  import pip._vendor.requests
import json

# Remove hashtag from clan/player tag
def cleanTag(input):
    output = input[1:len(input)]
    output = "%23" + output
    return output

# Call Clash of Clans API with the method and tag passed as args, return the formatted JSON response
def driver(method, tag):
    # Authorization omitted obviously
    headers = {'Authorization':}
    broad_endpoint = 'https://api.clashofclans.com/v1/'
    
    tag = cleanTag(tag)
    if method == "members" or method == "currentwar" or method == "warlog":
        signifier = 'clans/'
        this_endpoint = broad_endpoint + signifier
        this_endpoint = this_endpoint + tag + '/' + method
    elif method == "players":
        signifier = 'players/'
        this_endpoint = broad_endpoint + signifier
        this_endpoint = this_endpoint + tag
    elif method == "clans":
        signifier = 'clans/'
        this_endpoint = broad_endpoint + signifier + tag
    else
      jsonOut = ""
      return jsonOut, 404

    response = pip._vendor.requests.get(this_endpoint, headers=headers).text
    jsonOut = json.loads(response)
    
    responseCode = 101
    if 'reason' in jsonOut:
        if jsonOut['reason'] == 'notFound':
            responseCode = 404
    
    return jsonOut, responseCode
