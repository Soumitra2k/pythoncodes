import requests

#get requet

response= requests.get("http://216.10.245.166/Library/GetBook.php",{'ID':'huj878'},)
print(response.text)