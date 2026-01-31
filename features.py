import numpy as np
from skimage.feature import graycomatrix, graycoprops

def basic_stats(img):
    return {
        "mean": np.mean(img),
        "std": np.std(img),
        "var": np.var(img)
    }

def texture_features(img):
    img_q = ((img - img.min()) / (img.max() - img.min()) * 255).astype(np.uint8)
    glcm = graycomatrix(img_q, distances=[1], angles=[0], levels=256, symmetric=True)
    return {
        "contrast": graycoprops(glcm, 'contrast')[0,0],
        "entropy": -np.sum(glcm * np.log(glcm + 1e-9))
    }

def polarization_ratio(vv, vh):
    return np.mean(vv / (vh + 1e-6))
