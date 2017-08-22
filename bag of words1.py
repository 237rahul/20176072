#def bag():
import os
class plag(object):
	def dic(self,l,m):
		d={}
		for i in l:
			if i in d :
				d[i]+=1
			else:
				d[i]=1
		for j in m:
			if j not in d and j not in l:
				d[j]=0
		return d
	def dot_product(self,d1,d2):
		sum=0
		for i in d1:
			for j in d2:
				if i==j:
					s=d1[i]*d2[j]
			sum=sum+s
		return sum
	def euclidian_form(self,d):
		sum1=0
		for i in d:
			p=d[i]*d[i]
			sum1=sum1+p
		return sum1
def claplag(r1,r2):
	plag1=plag()
	f1=open(r1)
	f2=open(r2)
	a1=f1.read()
	a2=f2.read()
	s1=a1.lower().replace(',',' ').replace('.',' ')
	s2=a2.lower().replace(',',' ').replace('.',' ')
	l1=[]
	l1.extend(s1.split())
	l2=[]
	l2.extend(s2.split())
	d1=plag1.dic(l1,l2)
	d2=plag1.dic(l2,l1)
	m=plag1.dot_product(d1,d2)
	sq1=plag1.euclidian_form(d1)
	sq2=plag1.euclidian_form(d2)
	z=m/(((sq1)**(1/2))*((sq2)**(1/2)))
	z=z*100
	return z
l=[]
for files in os.listdir(os.getcwd()):
	l.append(files) 
print(l)
w=[]
for i in l:
	for j in l:
		z1=claplag(i,j)
		w.append(z1)
print(max(z))

