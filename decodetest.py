import string
import hashlib
import random

flag=""
cipher=""
alphabet = string.ascii_letters + string.digits + string.punctuation
f = open("cipher.txt","r")
for line in f:
	s=line
	str1 = line
	str2 = ''
	kt=1
	for i in range(len(str1)-1):
	    str2 = str2 + str1[i]
	for c in alphabet:
		for i in alphabet:
			temp=cipher+c+i
			if (hashlib.md5(temp.encode('utf-8')).hexdigest()==str2):
				cipher=temp
				flag=flag+i
				kt=0
				break
		if (kt==0):
			break
	for c in alphabet:
		for i in alphabet:
			for j in alphabet:
				temp=cipher+c+i+j
				if (hashlib.md5(temp.encode('utf-8')).hexdigest()==str2):
					cipher=temp
					flag=flag+j
					kt=0
					break
			if (kt==0):
				break
		if (kt==0):
			break
	for c in alphabet:
		for i in alphabet:
			for j in alphabet:
				for k in alphabet:
					temp=cipher+c+i+j+k
					if (hashlib.md5(temp.encode('utf-8')).hexdigest()==str2):
						cipher=temp
						flag=flag+k
						kt=0
						break
				if (kt==0):
					break
			if (kt==0):
				break
		if (kt==0):
			break;
	print(cipher)		

print(flag)				

f.close()
