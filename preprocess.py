import rasterio
import numpy as np
import cv2

def load_sar(path):
    with rasterio.open(path) as src:
        img = src.read(1).astype(np.float32)
        profile = src.profile
    return img, profile

def speckle_filter(img, ksize=5):
    return cv2.GaussianBlur(img, (ksize, ksize), 0)

def normalize_incidence(img):
    img = np.clip(img, -25, 5)   # typical SAR range (dB)
    return (img - img.mean()) / img.std()

def preprocess_sar(path):
    img, profile = load_sar(path)
    img = speckle_filter(img)
    img = normalize_incidence(img)
    return img, profile
