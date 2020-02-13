import pandas as pd 
temp = pd.read_csv(file_name)

from sklearn import mixture
model = mixture.GaussianMixture(n_components=3,
            covariance_type='full')
            
X = temp[['Land and Ocean','N Hem','S Hem']]
X.head()

model.fit(X)
# Determine cluster labels
y = model.predict(X)

X["cluster"]=y
X.head()
# See how we added a cluster 
            
import seaborn as sns
sns.lmplot(x="Land and Ocean", y="N Hem",data=X, col='cluster')
sns.lmplot(x="Land and Ocean", y="S Hem",data=X, col='cluster')
sns.lmplot(x="N Hem", y="s Hem",data=X, col='cluster')

# what do the plots show? 
