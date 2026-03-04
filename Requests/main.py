
import requests
url = "https://classroom.google.com/h"
response = requests.get(url)
print(response)
print(response.status_code)

response =requests.get("https://docs.teknolabs.net/courses/advanced-python/2-requests/")
print(response.content)

data = {"name": "Salah", "message": "Hello!"}
url = "https://httpbin.org/post"

response = requests.post(url, json=data)
response_data = response.json()
# Shows the data as a dictionary
print(response_data)

response = requests.get("https://httpbin.org/status/404")
# if status code is not 200 (successful response), then show error message
if response.status_code != 200:
    print(f"HTTP Error: {response.status_code}")

url = "https://httpbin.org/delay/10"

try:
    response = requests.get(url, timeout=5)
except requests.exceptions.Timeout as err:
    print(err)

auth_token = "XXXXXXXX"

# here we set the authorization header with the 'bearer token' for authentication purposes.
headers = {
    "Authorization": f"Bearer {auth_token}"
}

url = "https://httpbin.org/headers"
response = requests.get(url, headers=headers)
print(response.json())

auth_token="XXXX"
headers ={
    "Authorization":f"Bearer {auth_token}"
}
url = "https://httpbin.org/headers"
response = requests.get(url, headers=headers)
print(response.json())

from bs4 import BeautifulSoup

url = "https://www.youtube.com/watch?v=weXU_s16uaQ&list=RDMM&index=26"
# this will get all the HTML, javascript, css code
response = requests.get(url)

url = "https://docs.teknolabs.net/courses/advanced-python/2-requests/"
response1 = requests.get(url)
soup = BeautifulSoup(response1.content, "html.parser")

title = soup.title.text
content = soup.find("p").text
links = [a["href"] for a in soup.find_all("a")]

print(title, content, links)


import urllib.request
import urllib.parse

data = urllib.parse.urlencode({"key": "value"}).encode("utf-8")
req = urllib.request.Request("https://httpbin.org/delay/10", data=data, method="post")
with urllib.request.urlopen(req) as response:
    html = response.read().decode("utf-8")
print(html)