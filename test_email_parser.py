import requests

# you can change this path to your own email file you want to parse
path_to_email = "test subject.eml"

with open(path_to_email, 'r') as fp:
    raw_email = fp.read()

data = {'raw_email': raw_email, 'username': 'test', 'password': '@2Wr@Wxy8YvG9zk'}

res = requests.post("http://3.227.179.42:8000/parse/", json=data)

# if the result code is not equal to 200 then something went wrong
print("Result code: " + str(res.status_code))

# saving the result into the file 'result.json'
with open('result.json', 'w', encoding='utf-8') as fp:
    fp.write(res.text)
