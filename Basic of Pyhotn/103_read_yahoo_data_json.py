import json 
from urllib.request import urlopen 
with urlopen("https://www.youtube.com/watch?v=9N6a-VLBa2I") as response: 
    data = response.read() 
json_data = json.loads(data)

print(json.dumps(json_data))