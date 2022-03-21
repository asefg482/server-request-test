import requests

for i in range(1000):

    response = requests.get("http://api.open-notify.org/astros.json")
    print(response, response.elapsed.total_seconds())
