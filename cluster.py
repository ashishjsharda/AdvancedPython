from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons
from sklearn.metrics import adjusted_rand_score
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
features,true_labels=make_moons(n_samples=300,noise=0.05,random_state=42)
scaled_features=scaler.fit_transform(features)
print(scaled_features)
