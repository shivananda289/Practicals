import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans 
from sklearn.datasets import make_blobs 
from sklearn.preprocessing import StandardScaler 
X, y = make_blobs (n_samples=300, centers=4, cluster_std=0.6, random_state=42) 
scaler = StandardScaler() 
X_scaled = scaler.fit_transform(X) 
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c='gray', marker='o', edgecolor='k') 
plt.title("Data Distribution") 
plt.xlabel("Feature 1") 
plt.ylabel("Feature 2") 
plt.show()
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(X_scaled)
cluster_labels = kmeans.labels_
cluster_centers = kmeans.cluster_centers_
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=cluster_labels, cmap='viridis' , marker='o', edgecolor='k')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend ()
plt.show()
print(f"Inertia: {kmeans.inertia_}")
