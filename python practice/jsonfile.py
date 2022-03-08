import json as j
#data='{"name":"alex","city":"delhi"}'   # ' ' -> represents json, else it is dictionary
data={"name":"alex","city":"delhi"}
jsondata=j.dumps(data)     #used to convert dictionary to json

myjsonData=j.loads(jsondata)    #parsing
print(myjsonData["name"])