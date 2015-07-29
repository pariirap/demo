import requests

r= requests.get('http://www.cnn.com')

#assert isinstance(r.text, object)
print ( r.text)