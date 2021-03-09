import requests
#Url we want to get a request.
url='http://requestbin.net/r/1knwlwe1'
#We are sending informations about us .
r=requests.get(url,params={'Name':'Salih','Surname' :'Alperen'})
#Also we can have a request by sending User-Agent.
withPost=requests.post(url,headers={'User-Agent':'Salih'},params={'awaraness':'Munteare'},data={'name':'unkown'})


#Printing some propeties.
#Status code gives us information about we reached or not.


print(withPost.status_code)
#Ok means we get the whole source code.
print(withPost.ok)
#It gives us whole url
print(withPost.url)
#We can have headers.
print(withPost.headers)
print(withPost.text.strip())
#This code give us meta deta.
print(withPost.encoding)
#Status code history.
print(withPost.history)

print(withPost.request)
#Reaching time.
print(withPost.elapsed.total_seconds())


