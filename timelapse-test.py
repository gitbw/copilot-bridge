import cv2
import os
import numpy as np

def detect_drift(frames):
    drift_values = []
    for i in range(1, len(frames)):
        prev = cv2.imread(frames[i-1], cv2.IMREAD_GRAYSCALE)
        curr = cv2.imread(frames[i], cv2.IMREAD_GRAYSCALE)
        shift = cv2.phaseCorrelate(np.float32(prev), np.float32(curr))[0]
        drift_values.append(shift)
    return drift_values

def stabilize_frames(frames, drift_values):
    stabilized = []
    for i, frame in enumerate(frames):
        img = cv2.imread(frame)
        dx, dy = drift_values[i-1] if i > 0 else (0, 0)
        transform = np.float32([[1, 0, -dx], [0, 1, -dy]])
        stabilized_img = cv2.warpAffine(img, transform, (img.shape[1], img.shape[0]))
        stabilized.append(stabilized_img)
    return stabilized
