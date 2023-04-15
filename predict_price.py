import numpy as np
import matplotlib.pyplot as plt

my_file=open('files/project_data.csv','r')
my_data=my_file.read()
my_file.close()

lines=my_data.split('\n')
lines.pop(0)


table=[]
for line in lines:
	if line:
		cols=line.split(',')
		cols[0]=' '
		cols[9]=' '
		column=[]
		for col in cols:
			if col:
				if col != ' ':
					column.append(float(col))
		table.append(column)

table=np.array(table)
data_close=table[:, 4]
#print(data_close)
size_data_close=data_close.shape
size_data_close=size_data_close[0]
#print(size_data_close)

x=table[:,0]
#print(x)
#print(data_close)

dy=data_close[1:]-data_close[:-1]
dx=x[1:]-x[:-1]

ydot=data_close.copy()
ydot[1:]=dy/dx
ydot[0]=ydot[1]

#plt.plot(x, data_close, label= 'value')
#plt.plot(x, ydot, label= 'd/dx')
plt.xlabel('day')
plt.ylabel('value')
plt.title('FAMELI close price since 2007 until 2022')
plt.legend()
#plt.show()


xi=0
xf=10
data_value=[]

for j in range(0, size_data_close-10):
	data_value_i=[]
	for i in data_close[xi:xf]:
		data_value_i.append(i)
	xi=xi+1
	xf=xf+1
	data_value.append(data_value_i)
print(data_value)
print(len(data_value))

data_predict=[]

j=1

for i in data_value:
	if j>len(data_value)-1:
		break
	a=i[-1]
	b=data_value[j][-1]
	if b>a:
		data_predict.append(True)
	else:
		data_predict.append(False)
	j=j+1

print(data_predict)
