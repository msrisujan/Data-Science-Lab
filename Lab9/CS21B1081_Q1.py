# In[14]:


import numpy as np
import pandas as pd


# ### KNN Classifier

# In[15]:


def euclidean_distance(X_train, X_test):
    dist = np.zeros((len(X_test), len(X_train)))
    for i in range(len(X_test)):
        for j in range(len(X_train)):
            dist[i,j] = np.sqrt(np.sum((X_test[i] - X_train[j])**2))
    return dist
class KNN:
    def __init__(self, k = 5):
        self.k = k
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train
        
    def predict(self, X_test):
        self.distances = euclidean_distance(self.X_train, X_test)
        pred = []
        for dist in self.distances:
            k_nearest_indices = np.argsort(dist)[:self.k]
            k_nearest_labels = self.y_train[k_nearest_indices]
            pred.append(np.unique(k_nearest_labels)[np.argmax(np.unique(k_nearest_labels, return_counts=True)[1])])
        return np.array(pred)


# In[16]:


df = pd.read_csv('diabetes.csv')
X = df.iloc[:, :-2].values
y = df.iloc[:, -2].values


# In[17]:


# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
X_train = X[:614]
X_test = X[614:]
y_train = y[:614]
y_test = y[614:]


# In[18]:


knn = KNN(5)
knn.fit(X_train, y_train)


# In[19]:


y_pred = knn.predict(X_test)


# In[20]:


compared = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(compared)


# In[21]:


def accuracy(y_pred,y_test):
    return np.sum(y_pred == y_test)/len(y_test)

print("Accuracy: ", accuracy(y_pred, y_test))
print("accuracy percentage for KNN classifier: ", accuracy(y_pred, y_test)*100, "%")


# ### K-means Clustering

# In[25]:


def kmeans(X, n_clusters, n_init, random_state):
    np.random.seed(random_state)
    centroids = X[np.random.choice(X.shape[0], n_clusters, replace=False)]

    for _ in range(n_init):
        labels = np.argmin(np.linalg.norm(X[:, np.newaxis] - centroids, axis=2), axis=1)
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(n_clusters)])
        
        if np.all(centroids == new_centroids):
            break

        centroids = new_centroids
    return labels


# In[26]:


n_clusters = 2
n_init = 100
random_state = 0
y_kmeans = kmeans(X, n_clusters, n_init, random_state)


# In[27]:


print("Accuracy: ", accuracy(y_kmeans, y))
print("accuracy percentage for k-means clustering: ", accuracy(y_kmeans, y)*100, "%")