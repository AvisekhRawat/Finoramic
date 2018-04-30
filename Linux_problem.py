import os
import sys 
import subprocess 
import json

def fun(l):
	lis=[]
	for dat in l:		
		try:
			test = subprocess.check_output(['pip3','install',dat])
			print('installing ', dat)
		except subprocess.CalledProcessError as er:
			#print ("Error as  :",er.returncode,er.output )
			lis.append(dat)
	return lis

data = []

with open("dep.json") as o:
	dct=json.load(o)
	dic=dct['Dependencies']
	for d in dic:
		ss=('%s==%s' %(d,dic[d]))		
		data.append(ss)

ll =fun(data)
if(len(ll)>0):
	print('Failed to install')
	for i in ll:
		print(i)
else:
	print('ll is empty , successful')
		
