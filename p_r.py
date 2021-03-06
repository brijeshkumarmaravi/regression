import numpy as np
import matplotlib.pyplot as plt

X=[]
Y=[]
for line in open ("data_poly.csv"):
	x,y=line.split(',')
	x=float(x)
	X.append([1,x,x*x])
	Y.append(float(y))

# convert to numpy array
X=np.array(X)
Y=np.array(Y)

#lets plot the array and value in the graph
plt.scatter(X[:,1],Y)
plt.show()


# Calculate weights

#w=np.linalg.solve(np.dot(X.T,X), np.dot(X.T,Y))
w = np.linalg.solve(np.dot(X.T, X), np.dot(X.T, Y))

Yhat = np.dot(X, w)
#w = np.linalg.solve(np.dot(X.T, X), np.dot(X.T, Y))
#Yhat = np.dot(X, w)

#plot it all togetther 
plt.scatter(X[:,1],Y)
plt.plot(sorted(X[:,1]),sorted(Yhat))
plt.show();

# Accuracy
d1= Y-Yhat
d2=Y-Y.mean()

r2=1-(d1.dot(d1)/(d2).dot(d2))

print"the accuracy is given as:",r2
