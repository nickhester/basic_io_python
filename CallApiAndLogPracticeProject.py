import sys
import requests

# read from file
reader = open(sys.argv[1])
inputText = reader.read()
reader.close()

# call API
response = requests.get("http://numbersapi.com/" + inputText, { 'Content-Type': 'application/json' })
if response.status_code != 200:
    raise Exception("API failed to return a successful response")
responseText = response.content.decode('utf-8')

# write to file
writer = open(sys.argv[2], "w")
writer.write(responseText)
writer.close()
