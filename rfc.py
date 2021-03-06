Implementing a Random Forest Classifier:

from sklearn.ensemble import RandomForestClassifier
from numpy import genfromtxt, savetxt
 
dataset = genfromtxt(open('Data/train.csv','r'), delimiter=',' , dtype='f8')[1:]        
target = [x[0] for x in dataset]    
train = [x[1:] for x in dataset]    
test = genfromtxt(open('Data/test.csv','r'), delimiter=',' , dtype='f8')[1:]        
#create and train the random forest    
#multi-core CPUs can use: rf = RandomForestClassifier(n_estimators=100, n_jobs=2)    

rf = RandomForestClassifier(n_estimators=100)    
rf.fit(train, target)    
savetxt('Data/submission2.csv', rf.predict(test), delimiter=',' , fmt='%f')
