from sklearn.decomposition import NMF
from sklearn.preprocessing import Normalizer, MaxAbsScaler
from sklearn.pipeline import make_pipeline
import pandas as pd
import numpy as np

np.random.seed(0)
artists = np.abs(np.random.rand(10, 1000))

scaler = MaxAbsScaler()
nmf = NMF(n_components=20, random_state=42)
normalizer = Normalizer()
pipeline = make_pipeline(scaler, nmf, normalizer)

norm_features = pipeline.fit_transform(artists)

print("Norm_features shape:", norm_features.shape)
print(norm_features[:2])
