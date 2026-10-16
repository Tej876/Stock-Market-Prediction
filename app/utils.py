"""
Model loading and prediction helper functions.
Equipped with Streamlit caching for sub-millisecond real-time inference.
"""

import os
import json
import joblib
import numpy as np
import pandas as pd
import streamlit as st

MODELS_DIR_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), "models")
MODELS_DIR_LOCAL = os.path.join(os.path.dirname(__file__), "models")
MODELS_DIR = MODELS_DIR_LOCAL if os.path.exists(MODELS_DIR_LOCAL) else MODELS_DIR_ROOT

@st.cache_resource
def load_regression_bundle():
    bundle_path = os.path.join(MODELS_DIR, "regression_bundle.joblib")
    if not os.path.exists(bundle_path):
        return None
    return joblib.load(bundle_path)

@st.cache_resource
def load_classification_bundle():
    bundle_path = os.path.join(MODELS_DIR, "classification_bundle.joblib")
    if not os.path.exists(bundle_path):
        return None
    return joblib.load(bundle_path)

@st.cache_resource
def load_clustering_bundle():
    bundle_path = os.path.join(MODELS_DIR, "clustering_bundle.joblib")
    if not os.path.exists(bundle_path):
        return None
    return joblib.load(bundle_path)

@st.cache_data
def load_benchmark_metrics():
    path = os.path.join(MODELS_DIR, "benchmark_metrics.json")
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def run_regression_prediction(bundle, model_name, input_data):
    """
    Takes bundle, model name, and a dictionary of inputs.
    Returns: predicted_return, direction, rmse_bound, transformed_features
    """
    models = bundle["models"]
    preprocessor = bundle["preprocessor"]
    poly = bundle["poly"]
    feature_cols = bundle["feature_cols"]
    
    # Construct 1-row DataFrame
    input_df = pd.DataFrame([input_data])[feature_cols]
    
    # Preprocess
    proc = preprocessor.transform(input_df)
    
    model = models.get(model_name, list(models.values())[0])
    
    if "Polynomial" in model_name:
        proc_poly = poly.transform(proc)
        pred = float(model.predict(proc_poly)[0])
    else:
        pred = float(model.predict(proc)[0])
        
    direction = "BULLISH" if pred > 0 else "BEARISH"
    pct_return = pred * 100
    
    # Typical RMSE bound from benchmark for confidence band
    rmse_bound = 0.0126
    
    return {
        "model_name": model_name,
        "model_class": model.__class__.__name__,
        "predicted_log_return": pred,
        "predicted_pct_return": pct_return,
        "direction": direction,
        "confidence_low": (pred - rmse_bound) * 100,
        "confidence_high": (pred + rmse_bound) * 100,
        "rmse_bound": rmse_bound * 100,
        "raw_features": input_data,
        "processed_features": proc[0].tolist() if not "Polynomial" in model_name else proc_poly[0].tolist()[:10]
    }

def run_classification_prediction(bundle, model_name, use_smote, input_data, threshold=0.5):
    """
    Takes classification bundle, model name, SMOTE toggle, inputs, and decision threshold.
    Returns: predicted_class, probability, signal_label, confidence, diagnostics
    """
    models = bundle["models_smote"] if use_smote else bundle["models"]
    scaler = bundle["scaler"]
    feature_names = bundle["feature_names"]
    
    input_df = pd.DataFrame([input_data])[feature_names]
    input_scaled = scaler.transform(input_df)
    
    model = models.get(model_name, list(models.values())[0])
    
    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(input_scaled)[0]
        prob_class_1 = float(probs[1])
        prob_class_0 = float(probs[0])
    else:
        pred_raw = model.predict(input_scaled)[0]
        prob_class_1 = 1.0 if pred_raw == 1 else 0.0
        prob_class_0 = 1.0 - prob_class_1
        
    predicted_class = 1 if prob_class_1 >= threshold else 0
    signal_label = "BUY / LONG" if predicted_class == 1 else "HOLD / NEUTRAL / EXIT"
    confidence = prob_class_1 if predicted_class == 1 else prob_class_0
    
    return {
        "model_name": model_name,
        "model_class": model.__class__.__name__,
        "predicted_class": predicted_class,
        "signal_label": signal_label,
        "prob_class_1": prob_class_1,
        "prob_class_0": prob_class_0,
        "confidence": confidence * 100,
        "threshold": threshold,
        "raw_features": input_data,
        "scaled_features": input_scaled[0].tolist()
    }

def run_clustering_assignment(bundle, input_data):
    """
    Projects new point into existing scaler + PCA space and identifies assigned cluster.
    """
    kmeans = bundle["kmeans"]
    scaler = bundle["scaler"]
    pca = bundle["pca"]
    features = bundle["features"]
    regime_names = bundle["regime_names"]
    cluster_means = bundle["cluster_means"]
    
    # Copy & log-transform Volume
    val_dict = dict(input_data)
    val_dict["Volume"] = np.log1p(float(val_dict["Volume"]))
    
    input_df = pd.DataFrame([val_dict])[features]
    scaled_pt = scaler.transform(input_df)
    
    # Assigned KMeans cluster
    cluster_id = int(kmeans.predict(scaled_pt)[0])
    
    # 2D PCA coordinates
    pca_coords = pca.transform(scaled_pt)[0]
    
    # Distance to each centroid
    centroids = kmeans.cluster_centers_
    distances = np.linalg.norm(centroids - scaled_pt, axis=1)
    
    regime_title = regime_names.get(cluster_id, f"Cluster {cluster_id}")
    
    return {
        "cluster_id": cluster_id,
        "regime_name": regime_title,
        "pca_x": float(pca_coords[0]),
        "pca_y": float(pca_coords[1]),
        "distances": {f"Cluster {i}": float(dist) for i, dist in enumerate(distances)},
        "centroid_comparison": cluster_means.get(str(cluster_id), cluster_means.get(cluster_id, {})),
        "raw_features": input_data,
        "scaled_features": scaled_pt[0].tolist()
    }
