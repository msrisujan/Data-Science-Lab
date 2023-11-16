#---------------------------KNN------------------------------------

import math

def euclidean_distance(point1, point2):
    distance = 0.0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return math.sqrt(distance)

def knn(train_data, test_instance, k):
    distances = []
    for train_instance in train_data:
        distance = euclidean_distance(train_instance[:-1], test_instance[:])
        distances.append((train_instance, distance))

    distances.sort(key=lambda x: x[1])
    
    neighbors = distances[:k]
    #print(neighbors)
    class_votes = []
    
    for neighbor in neighbors:
        label = neighbor[0][-1]
        class_votes.append(label)
        
    max_count = 0
    predicted_class = -1
    for i in range(len(class_votes)):
        count = 1
        for j in range(len(class_votes)):
            if i!=j and class_votes[i] == class_votes[j]:
                count += 1
                
        if count >= max_count:
            max_count = count
            predicted_class = class_votes[i]
    
    return predicted_class

# Example usage:
# Suppose we have a training dataset with three features and a class label (0 or 1)
train_data = [
    [1, 2, 1, 0],
    [2, 3, 1, 0],
    [4, 5, 1, 1],
    [1, 7, 5, 1],
    [5, 6, 1, 1]
]

# Suppose we have a test instance for which we want to predict the class
test_instance = [3, 4, 1]

# Choose the value of k
k_value = 3

# Predict the class using KNN
prediction = knn(train_data, test_instance, k_value)

print("Predicted class:", prediction)


#----------------------------kmeans--------------------------------------

import math
import random

def euclidean_distance(point1, point2):
    distance = 0.0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return math.sqrt(distance)

def initialize_centroids(data, k):
    centroids = []
    for _ in range(k):
        random_index = random.randint(0, len(data) - 1)
        centroids.append(data[random_index])
    return centroids

def kmeans(data, k, max_iterations=100):
    # Step 1: Initialize centroids randomly
    centroids = initialize_centroids(data, k)
    #print(centroids)

    for _ in range(max_iterations):
        # Step 2: Assign each data point to the nearest centroid
        clusters = [[] for _ in range(k)]

        for point in data:
            min_distance = float('inf')
            cluster_index = -1
            for i, centroid in enumerate(centroids):
                # print('centroid', centroid)
                distance = euclidean_distance(point, centroid)
                if distance < min_distance:
                    min_distance = distance
                    cluster_index = i
            clusters[cluster_index].append(point)

        # Step 3: Update centroids based on the mean of points in each cluster
        for i in range(k):
            if clusters[i]:
                centroid = [sum(x) / len(clusters[i]) for x in zip(*clusters[i])]
                centroids[i] = centroid

    return clusters, centroids

# Example usage:
# Suppose we have a dataset with two features
data = [
    [1, 2],
    [2, 3],
    [5, 6],
    [6, 7],
    [10, 12],
    [11, 13]
]

# Choose the value of k (number of clusters)
k_value = 2

# Run k-means clustering
clusters, final_centroids = kmeans(data, k_value)

# Display the clusters and final centroids
for i, cluster in enumerate(clusters):
    print(f"Cluster {i + 1}: {cluster}")

print("\nFinal centroids:")
for centroid in final_centroids:
    print(centroid)


#-------------------------PCA----------------------------------------

def covariance(X):
    mean = np.mean(X,axis=0)
    X = X - mean
    return np.dot(X.T, X)/(X.shape[0]-1)

class PCA:
    def __init__(self, n_components):
        self.components = None
        self.n_components = n_components
        
    def fit(self, X):
        # covariance matrix
        cov = covariance(X)
        # eigenvalues and eigenvectors
        eigenvalues, eigenvectors = np.linalg.eig(cov)
        # sort eigenvalues and eigenvectors
        idx = eigenvalues.argsort()[::-1]
        eigenvalues = eigenvalues[idx]
        eigenvectors = eigenvectors[:, idx]
        # components
        self.components = eigenvectors[:, :self.n_components]
    
    def transform(self, X):
        return np.dot(X, self.components)

pca = PCA(6)
pca.fit(X_train)
X_train1 = pca.transform(X_train.values)
X_test1 = pca.transform(X_test.values)








#----------------------------------eigenvalues&&eigenvectors--------------------------------------------

import numpy as np

# Define a matrix
A = np.array([[4, -2], [1, 1]])

# Function to calculate eigenvalues using the characteristic equation
def find_eigenvalues(matrix):
    # Calculate the determinant of the matrix
    det = np.linalg.det(matrix)
    
    # Solve the characteristic equation det(A - λI) = 0
    eigenvalues = np.roots([1, -np.trace(matrix), det])

    return eigenvalues

# Function to find eigenvectors given eigenvalues and the original matrix
def find_eigenvectors(matrix, eigenvalues):
    eigenvectors = []
    for eigenvalue in eigenvalues:
        # Solve the equation (A - λI)x = 0 for each eigenvalue
        eigenvector = np.linalg.solve(matrix - eigenvalue * np.eye(matrix.shape[0]), np.zeros(matrix.shape[0]))
        eigenvectors.append(eigenvector)

    return np.array(eigenvectors)

# Calculate eigenvalues
eigenvalues = find_eigenvalues(A)

# Calculate eigenvectors
eigenvectors = find_eigenvectors(A, eigenvalues)

# Display the results
print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)
